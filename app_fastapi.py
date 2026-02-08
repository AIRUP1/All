#!/usr/bin/env python3
"""
StormBuster Web Application - FastAPI Version
FastAPI backend for the StormBuster storm damage lead generation system
"""

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import pandas as pd
import json
import os
from datetime import datetime, timedelta
from typing import Optional, List, Dict
import uvicorn

# Import your existing modules
from nationwide_property_search_engine import NationwidePropertySearchEngine
from spokeo_integration import SpokeoAPI
from ai_chat_integration import ai_chat, AIProvider
from results_roofing_integration import RoofingIntegration
from vendor_registration_system import VendorRegistrationSystem

# Create FastAPI app
app = FastAPI(
    title="StormBuster API",
    description="Storm damage lead generation system",
    version="2.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the search engine
search_engine = NationwidePropertySearchEngine()
spokeo_api = SpokeoAPI("bolison10@gmail.com", "Bbusta10")
results_roofing = RoofingIntegration()
vendor_system = VendorRegistrationSystem()

# Global variables for caching
cached_leads = None
cached_stats = None
last_update = None

# Request Models
class SearchRequest(BaseModel):
    address: str = ""
    city: str = ""
    state: str = ""
    zipcode: str = ""

class GenerateLeadsRequest(BaseModel):
    years: List[int] = [2024, 2025]
    min_hail_size: float = 1.0

class AIChatRequest(BaseModel):
    message: str
    model: str = "gpt-3.5-turbo"
    tier: str = "basic"
    context: str = ""

class VendorRegistration(BaseModel):
    name: str
    type: str
    email: str
    phone: str
    service_areas: List[str]

# Routes
@app.get("/")
async def index():
    """Serve the main application"""
    try:
        return FileResponse('index.html')
    except:
        return HTMLResponse('<h1>StormBuster API</h1><p>Visit /docs for API documentation</p>')

@app.get("/hello")
async def hello(name: str = "FastAPI"):
    """Hello endpoint"""
    return {"message": f"Hello, {name}!"}

@app.get("/api/stats")
async def get_stats():
    """Get current statistics"""
    global cached_stats, last_update
    
    if cached_stats is None or (last_update is None or datetime.now() - last_update > timedelta(minutes=5)):
        try:
            leads_file = 'nationwide_leads_database.csv'
            if os.path.exists(leads_file):
                df = pd.read_csv(leads_file)
                cached_stats = {
                    'total_leads': len(df),
                    'high_priority_leads': len(df[df['lead_score'] >= 70]) if 'lead_score' in df.columns else 0,
                    'medium_priority_leads': len(df[(df['lead_score'] >= 40) & (df['lead_score'] < 70)]) if 'lead_score' in df.columns else 0,
                    'low_priority_leads': len(df[df['lead_score'] < 40]) if 'lead_score' in df.columns else 0,
                    'states_covered': df['state_name'].nunique() if 'state_name' in df.columns else 0,
                    'cities_covered': df['city'].nunique() if 'city' in df.columns else 0,
                    'avg_lead_score': df['lead_score'].mean() if 'lead_score' in df.columns else 0,
                    'last_updated': datetime.now().isoformat()
                }
            else:
                cached_stats = {
                    'total_leads': 11817,
                    'high_priority_leads': 1666,
                    'medium_priority_leads': 3151,
                    'low_priority_leads': 7000,
                    'states_covered': 43,
                    'cities_covered': 1,
                    'avg_lead_score': 29.3,
                    'last_updated': datetime.now().isoformat()
                }
            last_update = datetime.now()
        except Exception as e:
            print(f"Error generating stats: {e}")
            cached_stats = {
                'total_leads': 11817,
                'high_priority_leads': 1666,
                'medium_priority_leads': 3151,
                'low_priority_leads': 7000,
                'states_covered': 43,
                'cities_covered': 1,
                'avg_lead_score': 29.3,
                'last_updated': datetime.now().isoformat()
            }
    
    return cached_stats

@app.get("/api/leads")
async def get_leads():
    """Get leads data"""
    global cached_leads
    
    try:
        leads_file = 'nationwide_leads_database.csv'
        if os.path.exists(leads_file):
            df = pd.read_csv(leads_file)
            
            leads = []
            for idx, row in df.head(100).iterrows():
                lead = {
                    'id': idx + 1,
                    'name': row.get('property_owner_name', 'Unknown Owner'),
                    'address': f"{row.get('city', 'Unknown City')}, {row.get('state_name', 'Unknown State')}",
                    'phone': row.get('property_owner_phone', 'N/A'),
                    'email': row.get('property_owner_email', 'N/A'),
                    'property_value': row.get('property_value', '$0'),
                    'hail_size': f"{row.get('MAGNITUDE', 0)}\"",
                    'score': int(row.get('lead_score', 0)),
                    'priority': 'high' if row.get('lead_score', 0) >= 70 else 'medium' if row.get('lead_score', 0) >= 40 else 'low',
                    'date': row.get('BEGIN_DATE_TIME', datetime.now().strftime('%Y-%m-%d'))[:10]
                }
                leads.append(lead)
            
            cached_leads = leads
            return leads
        else:
            return []
    except Exception as e:
        print(f"Error loading leads: {e}")
        return []

@app.post("/api/search")
async def search_property(request: SearchRequest):
    """Search for property using Spokeo API"""
    try:
        result = spokeo_api.search_property_by_address(
            request.address, 
            request.city, 
            request.state, 
            request.zipcode
        )
        
        return {
            'success': True,
            'data': result
        }
    except Exception as e:
        print(f"Error in property search: {e}")
        return {
            'success': False,
            'error': str(e)
        }

@app.post("/api/generate-leads")
async def generate_leads(request: GenerateLeadsRequest):
    """Generate new leads using the search engine"""
    try:
        # This would ideally be run in background
        print("Starting lead generation...")
        
        events_df = search_engine.search_all_states(
            years=request.years, 
            min_hail_size=request.min_hail_size
        )
        
        if not events_df.empty:
            geo_df = search_engine.geocode_events(events_df)
            property_df = search_engine.search_property_data(
                geo_df, 
                "bolison10@gmail.com", 
                "Bbusta10"
            )
            leads_df = search_engine.create_lead_database(geo_df, property_df)
            summary = search_engine.generate_reports(leads_df)
            
            return {
                'success': True,
                'message': 'Lead generation complete',
                'summary': summary
            }
        else:
            return {
                'success': False,
                'message': 'No events found'
            }
    except Exception as e:
        print(f"Error in lead generation: {e}")
        return {
            'success': False,
            'error': str(e)
        }

@app.get("/api/recent-events")
async def get_recent_events():
    """Get recent hail events"""
    try:
        events_file = 'nationwide_leads_database.csv'
        if os.path.exists(events_file):
            df = pd.read_csv(events_file)
            
            recent_events = []
            for idx, row in df.head(10).iterrows():
                event = {
                    'location': f"{row.get('city', 'Unknown')}, {row.get('state_name', 'Unknown')}",
                    'hail_size': f"{row.get('MAGNITUDE', 0)}\"",
                    'date': row.get('BEGIN_DATE_TIME', datetime.now().strftime('%Y-%m-%d'))[:10]
                }
                recent_events.append(event)
            
            return recent_events
        else:
            return [
                {'location': 'Dallas, TX', 'hail_size': '2.5"', 'date': '2025-01-15'},
                {'location': 'Fort Worth, TX', 'hail_size': '1.8"', 'date': '2025-01-14'},
                {'location': 'Plano, TX', 'hail_size': '2.1"', 'date': '2025-01-13'},
                {'location': 'Arlington, TX', 'hail_size': '1.5"', 'date': '2025-01-12'}
            ]
    except Exception as e:
        print(f"Error loading recent events: {e}")
        return []

@app.get("/api/download/{filename}")
async def download_file(filename: str):
    """Download generated reports"""
    try:
        if os.path.exists(filename):
            return FileResponse(filename, media_type='application/octet-stream', filename=filename)
        else:
            return {"error": "File not found"}
    except Exception as e:
        print(f"Error downloading file: {e}")
        return {"error": str(e)}

@app.get("/api/spokeo-status")
async def get_spokeo_status():
    """Get Spokeo API connection status"""
    try:
        status = spokeo_api.login()
        
        return {
            'connected': status,
            'username': 'bolison10@gmail.com',
            'last_checked': datetime.now().isoformat()
        }
    except Exception as e:
        print(f"Error checking Spokeo status: {e}")
        return {
            'connected': False,
            'username': 'bolison10@gmail.com',
            'error': str(e),
            'last_checked': datetime.now().isoformat()
        }

@app.get("/api/vendor-types")
async def get_vendor_types():
    """Get list of available vendor types"""
    return vendor_system.get_vendor_types()

@app.get("/api/service-areas")
async def get_service_areas():
    """Get list of service areas"""
    return vendor_system.get_service_areas()

@app.get("/api/licensing-requirements/{vendor_type}")
async def get_licensing_requirements(vendor_type: str):
    """Get licensing requirements for specific vendor type"""
    return vendor_system.get_licensing_requirements(vendor_type)

@app.post("/api/vendor-register")
async def register_vendor(vendor_data: dict):
    """Register a new vendor"""
    try:
        result = vendor_system.register_vendor(vendor_data)
        return result
    except Exception as e:
        print(f"Error registering vendor: {e}")
        return {
            'success': False,
            'error': str(e)
        }

@app.get("/api/vendors")
async def get_vendors():
    """Get list of all vendors"""
    try:
        vendors = vendor_system.get_vendor_list()
        return vendors
    except Exception as e:
        print(f"Error getting vendors: {e}")
        return {'error': str(e)}

@app.post("/api/vendor-search")
async def search_vendors(criteria: dict):
    """Search vendors by criteria"""
    try:
        vendors = vendor_system.search_vendors(criteria)
        return vendors
    except Exception as e:
        print(f"Error searching vendors: {e}")
        return {'error': str(e)}

if __name__ == '__main__':
    import os
    
    print("🚀 Starting StormBuster FastAPI Application")
    print("=" * 50)
    print("🌩️  StormBuster - Strike While the Storm Rages")
    print("📊 Integrated with DFW Hail Pipeline")
    print("🔑 Spokeo API: bolison10@gmail.com")
    print("🌐 Domain: stormgods.us")
    print("=" * 50)
    
    port = int(os.environ.get('PORT', 8000))
    debug_mode = os.environ.get('FASTAPI_ENV', 'development') == 'development'
    
    print(f"🌐 Starting server on port {port}")
    print(f"🔧 Debug mode: {debug_mode}")
    print(f"📖 API Docs: http://localhost:{port}/docs")
    
    uvicorn.run("app_fastapi:app", host="0.0.0.0", port=port, reload=debug_mode)

