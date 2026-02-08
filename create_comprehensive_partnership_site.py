"""
Comprehensive Partnership Website
Incorporates Realtors, Property Managers, Builders, and Insurance
Creates a complete ecosystem for property services
"""
import os

def create_comprehensive_partnership_website():
    """
    Create enhanced website with all partnership types
    """
    
    # Comprehensive landing page HTML
    landing_page = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hail Damage Assessment & Property Services - Complete Solutions</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        
        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
        }
        
        .header {
            background: rgba(255,255,255,0.95);
            padding: 30px;
            border-radius: 15px;
            margin-bottom: 30px;
            box-shadow: 0 15px 50px rgba(0,0,0,0.1);
            text-align: center;
        }
        
        .header h1 {
            color: #2E86AB;
            font-size: 3em;
            margin-bottom: 15px;
        }
        
        .header p {
            font-size: 1.3em;
            color: #666;
            margin-bottom: 20px;
        }
        
        .partnership-banner {
            background: linear-gradient(45deg, #FF6B6B, #4ECDC4, #45B7D1, #96CEB4);
            color: white;
            padding: 25px;
            border-radius: 15px;
            margin-bottom: 30px;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }
        
        .partnership-banner h2 {
            font-size: 2em;
            margin-bottom: 15px;
        }
        
        .partnership-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }
        
        .partnership-card {
            background: rgba(255,255,255,0.95);
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            transition: transform 0.3s;
            border-left: 5px solid #2E86AB;
        }
        
        .partnership-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.15);
        }
        
        .partnership-icon {
            font-size: 3em;
            margin-bottom: 15px;
            text-align: center;
        }
        
        .partnership-title {
            font-size: 1.5em;
            font-weight: bold;
            color: #2E86AB;
            margin-bottom: 10px;
            text-align: center;
        }
        
        .partnership-benefits {
            list-style: none;
            padding: 0;
        }
        
        .partnership-benefits li {
            margin-bottom: 8px;
            padding-left: 20px;
            position: relative;
        }
        
        .partnership-benefits li:before {
            content: "✓";
            position: absolute;
            left: 0;
            color: #06A77D;
            font-weight: bold;
        }
        
        .main-content {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            margin-bottom: 30px;
        }
        
        .info-section {
            background: rgba(255,255,255,0.95);
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 15px 50px rgba(0,0,0,0.1);
        }
        
        .form-section {
            background: rgba(255,255,255,0.95);
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 15px 50px rgba(0,0,0,0.1);
        }
        
        .form-section h2 {
            color: #2E86AB;
            margin-bottom: 20px;
            font-size: 1.8em;
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        .form-group label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
            color: #333;
        }
        
        .form-group input,
        .form-group select,
        .form-group textarea {
            width: 100%;
            padding: 12px;
            border: 2px solid #ddd;
            border-radius: 8px;
            font-size: 16px;
            transition: border-color 0.3s;
        }
        
        .form-group input:focus,
        .form-group select:focus,
        .form-group textarea:focus {
            outline: none;
            border-color: #2E86AB;
        }
        
        .checkbox-group {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }
        
        .checkbox-item {
            display: flex;
            align-items: center;
            margin-right: 20px;
        }
        
        .checkbox-item input[type="checkbox"] {
            width: auto;
            margin-right: 8px;
        }
        
        .btn {
            background: linear-gradient(45deg, #F18F01, #A23B72);
            color: white;
            padding: 15px 30px;
            border: none;
            border-radius: 8px;
            font-size: 18px;
            font-weight: bold;
            cursor: pointer;
            width: 100%;
            transition: transform 0.3s;
            margin-bottom: 10px;
        }
        
        .btn:hover {
            transform: translateY(-2px);
        }
        
        .btn-secondary {
            background: linear-gradient(45deg, #2E86AB, #06A77D);
        }
        
        .btn-tertiary {
            background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        }
        
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }
        
        .stat-card {
            background: rgba(255,255,255,0.9);
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }
        
        .stat-number {
            font-size: 2.5em;
            font-weight: bold;
            color: #2E86AB;
        }
        
        .stat-label {
            color: #666;
            margin-top: 5px;
        }
        
        .tabs {
            display: flex;
            margin-bottom: 20px;
            border-bottom: 2px solid #eee;
            flex-wrap: wrap;
        }
        
        .tab {
            padding: 12px 20px;
            cursor: pointer;
            border-bottom: 3px solid transparent;
            transition: all 0.3s;
            margin-right: 10px;
            margin-bottom: 10px;
        }
        
        .tab.active {
            border-bottom-color: #2E86AB;
            color: #2E86AB;
            font-weight: bold;
        }
        
        .tab-content {
            display: none;
        }
        
        .tab-content.active {
            display: block;
        }
        
        .testimonials {
            background: rgba(255,255,255,0.95);
            padding: 30px;
            border-radius: 15px;
            margin-top: 30px;
            box-shadow: 0 15px 50px rgba(0,0,0,0.1);
        }
        
        .testimonial {
            margin-bottom: 20px;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 10px;
            border-left: 4px solid #2E86AB;
        }
        
        .testimonial-text {
            font-style: italic;
            margin-bottom: 10px;
        }
        
        .testimonial-author {
            font-weight: bold;
            color: #2E86AB;
        }
        
        .footer {
            text-align: center;
            margin-top: 40px;
            padding: 30px;
            background: rgba(255,255,255,0.9);
            border-radius: 15px;
        }
        
        @media (max-width: 768px) {
            .main-content {
                grid-template-columns: 1fr;
            }
            
            .header h1 {
                font-size: 2.2em;
            }
            
            .partnership-grid {
                grid-template-columns: 1fr;
            }
            
            .tabs {
                flex-direction: column;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🌩️ Complete Property Solutions</h1>
            <p>Hail Damage Assessment, Insurance, Real Estate, Property Management & Construction</p>
        </div>
        
        <div class="partnership-banner">
            <h2>🤝 Comprehensive Partnership Network</h2>
            <p>We connect you with trusted professionals across all property services</p>
        </div>
        
        <div class="partnership-grid">
            <div class="partnership-card">
                <div class="partnership-icon">🏠</div>
                <div class="partnership-title">Real Estate Agents</div>
                <ul class="partnership-benefits">
                    <li>Property value assessments</li>
                    <li>Pre-sale inspections</li>
                    <li>Market analysis</li>
                    <li>Buyer representation</li>
                    <li>Seller consultations</li>
                </ul>
            </div>
            
            <div class="partnership-card">
                <div class="partnership-icon">🏢</div>
                <div class="partnership-title">Property Managers</div>
                <ul class="partnership-benefits">
                    <li>Multi-unit inspections</li>
                    <li>Tenant damage assessments</li>
                    <li>Maintenance coordination</li>
                    <li>Insurance claims management</li>
                    <li>Vendor referrals</li>
                </ul>
            </div>
            
            <div class="partnership-card">
                <div class="partnership-icon">🔨</div>
                <div class="partnership-title">Builders & Contractors</div>
                <ul class="partnership-benefits">
                    <li>New construction inspections</li>
                    <li>Warranty assessments</li>
                    <li>Quality control checks</li>
                    <li>Subcontractor referrals</li>
                    <li>Project management</li>
                </ul>
            </div>
            
            <div class="partnership-card">
                <div class="partnership-icon">🛡️</div>
                <div class="partnership-title">Insurance Partners</div>
                <ul class="partnership-benefits">
                    <li>Claims processing</li>
                    <li>Policy reviews</li>
                    <li>Coverage optimization</li>
                    <li>Bundle discounts</li>
                    <li>Claims advocacy</li>
                </ul>
            </div>
        </div>
        
        <div class="stats">
            <div class="stat-card">
                <div class="stat-number">515</div>
                <div class="stat-label">Hail Events Tracked</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">47</div>
                <div class="stat-label">Severe Events (2"+ hail)</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">50+</div>
                <div class="stat-label">Partner Network</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">$0</div>
                <div class="stat-label">Inspection Cost</div>
            </div>
        </div>
        
        <div class="main-content">
            <div class="info-section">
                <div class="tabs">
                    <div class="tab active" onclick="switchTab('inspection')">Free Inspection</div>
                    <div class="tab" onclick="switchTab('realestate')">Real Estate</div>
                    <div class="tab" onclick="switchTab('propertymgmt')">Property Management</div>
                    <div class="tab" onclick="switchTab('construction')">Construction</div>
                    <div class="tab" onclick="switchTab('insurance')">Insurance</div>
                </div>
                
                <div id="inspection" class="tab-content active">
                    <h2>Why Choose Our Hail Damage Assessment?</h2>
                    <ul style="list-style: none; padding: 0;">
                        <li style="margin-bottom: 15px; padding-left: 25px; position: relative;">
                            <span style="position: absolute; left: 0; color: #2E86AB; font-weight: bold;">✓</span>
                            <strong>FREE Inspection:</strong> No cost to you for initial assessment
                        </li>
                        <li style="margin-bottom: 15px; padding-left: 25px; position: relative;">
                            <span style="position: absolute; left: 0; color: #2E86AB; font-weight: bold;">✓</span>
                            <strong>Multi-Service Network:</strong> Connect with all property professionals
                        </li>
                        <li style="margin-bottom: 15px; padding-left: 25px; position: relative;">
                            <span style="position: absolute; left: 0; color: #2E86AB; font-weight: bold;">✓</span>
                            <strong>Comprehensive Solutions:</strong> One-stop for all property needs
                        </li>
                        <li style="margin-bottom: 15px; padding-left: 25px; position: relative;">
                            <span style="position: absolute; left: 0; color: #2E86AB; font-weight: bold;">✓</span>
                            <strong>Licensed & Insured:</strong> Fully certified professionals
                        </li>
                    </ul>
                </div>
                
                <div id="realestate" class="tab-content">
                    <h2>Real Estate Services</h2>
                    <ul style="list-style: none; padding: 0;">
                        <li style="margin-bottom: 15px; padding-left: 25px; position: relative;">
                            <span style="position: absolute; left: 0; color: #2E86AB; font-weight: bold;">✓</span>
                            <strong>Pre-Listing Inspections:</strong> Identify issues before they affect sale price
                        </li>
                        <li style="margin-bottom: 15px; padding-left: 25px; position: relative;">
                            <span style="position: absolute; left: 0; color: #2E86AB; font-weight: bold;">✓</span>
                            <strong>Buyer Representation:</strong> Protect your clients' interests
                        </li>
                        <li style="margin-bottom: 15px; padding-left: 25px; position: relative;">
                            <span style="position: absolute; left: 0; color: #2E86AB; font-weight: bold;">✓</span>
                            <strong>Market Analysis:</strong> Accurate property valuations
                        </li>
                        <li style="margin-bottom: 15px; padding-left: 25px; position: relative;">
                            <span style="position: absolute; left: 0; color: #2E86AB; font-weight: bold;">✓</span>
                            <strong>Negotiation Support:</strong> Expert damage assessments for negotiations
                        </li>
                    </ul>
                </div>
                
                <div id="propertymgmt" class="tab-content">
                    <h2>Property Management Services</h2>
                    <ul style="list-style: none; padding: 0;">
                        <li style="margin-bottom: 15px; padding-left: 25px; position: relative;">
                            <span style="position: absolute; left: 0; color: #2E86AB; font-weight: bold;">✓</span>
                            <strong>Multi-Unit Inspections:</strong> Efficient assessment of entire properties
                        </li>
                        <li style="margin-bottom: 15px; padding-left: 25px; position: relative;">
                            <span style="position: absolute; left: 0; color: #2E86AB; font-weight: bold;">✓</span>
                            <strong>Tenant Damage Assessment:</strong> Clear documentation for security deposits
                        </li>
                        <li style="margin-bottom: 15px; padding-left: 25px; position: relative;">
                            <span style="position: absolute; left: 0; color: #2E86AB; font-weight: bold;">✓</span>
                            <strong>Maintenance Coordination:</strong> Streamlined repair processes
                        </li>
                        <li style="margin-bottom: 15px; padding-left: 25px; position: relative;">
                            <span style="position: absolute; left: 0; color: #2E86AB; font-weight: bold;">✓</span>
                            <strong>Insurance Claims:</strong> Maximize coverage for property damage
                        </li>
                    </ul>
                </div>
                
                <div id="construction" class="tab-content">
                    <h2>Construction & Building Services</h2>
                    <ul style="list-style: none; padding: 0;">
                        <li style="margin-bottom: 15px; padding-left: 25px; position: relative;">
                            <span style="position: absolute; left: 0; color: #2E86AB; font-weight: bold;">✓</span>
                            <strong>New Construction Inspections:</strong> Quality control during building
                        </li>
                        <li style="margin-bottom: 15px; padding-left: 25px; position: relative;">
                            <span style="position: absolute; left: 0; color: #2E86AB; font-weight: bold;">✓</span>
                            <strong>Warranty Assessments:</strong> Identify covered vs. non-covered damage
                        </li>
                        <li style="margin-bottom: 15px; padding-left: 25px; position: relative;">
                            <span style="position: absolute; left: 0; color: #2E86AB; font-weight: bold;">✓</span>
                            <strong>Subcontractor Quality:</strong> Ensure work meets standards
                        </li>
                        <li style="margin-bottom: 15px; padding-left: 25px; position: relative;">
                            <span style="position: absolute; left: 0; color: #2E86AB; font-weight: bold;">✓</span>
                            <strong>Project Management:</strong> Coordinate all aspects of repairs
                        </li>
                    </ul>
                </div>
                
                <div id="insurance" class="tab-content">
                    <h2>Insurance Partnership Benefits</h2>
                    <ul style="list-style: none; padding: 0;">
                        <li style="margin-bottom: 15px; padding-left: 25px; position: relative;">
                            <span style="position: absolute; left: 0; color: #2E86AB; font-weight: bold;">✓</span>
                            <strong>Pre-negotiated Rates:</strong> Better coverage at lower costs
                        </li>
                        <li style="margin-bottom: 15px; padding-left: 25px; position: relative;">
                            <span style="position: absolute; left: 0; color: #2E86AB; font-weight: bold;">✓</span>
                            <strong>Faster Claims:</strong> Streamlined process with our partners
                        </li>
                        <li style="margin-bottom: 15px; padding-left: 25px; position: relative;">
                            <span style="position: absolute; left: 0; color: #2E86AB; font-weight: bold;">✓</span>
                            <strong>Expert Support:</strong> Dedicated claims specialists
                        </li>
                        <li style="margin-bottom: 15px; padding-left: 25px; position: relative;">
                            <span style="position: absolute; left: 0; color: #2E86AB; font-weight: bold;">✓</span>
                            <strong>Bundle Discounts:</strong> Save on home and auto insurance
                        </li>
                    </ul>
                </div>
            </div>
            
            <div class="form-section">
                <h2>Get Your FREE Assessment</h2>
                <form id="comprehensiveForm" action="#" method="POST">
                    <div class="form-group">
                        <label for="firstName">First Name *</label>
                        <input type="text" id="firstName" name="firstName" required>
                    </div>
                    
                    <div class="form-group">
                        <label for="lastName">Last Name *</label>
                        <input type="text" id="lastName" name="lastName" required>
                    </div>
                    
                    <div class="form-group">
                        <label for="email">Email Address *</label>
                        <input type="email" id="email" name="email" required>
                    </div>
                    
                    <div class="form-group">
                        <label for="phone">Phone Number *</label>
                        <input type="tel" id="phone" name="phone" required>
                    </div>
                    
                    <div class="form-group">
                        <label for="address">Property Address *</label>
                        <input type="text" id="address" name="address" required>
                    </div>
                    
                    <div class="form-group">
                        <label for="city">City *</label>
                        <input type="text" id="city" name="city" required>
                    </div>
                    
                    <div class="form-group">
                        <label for="zipcode">ZIP Code *</label>
                        <input type="text" id="zipcode" name="zipcode" required>
                    </div>
                    
                    <div class="form-group">
                        <label for="propertyType">Property Type *</label>
                        <select id="propertyType" name="propertyType" required>
                            <option value="">Select Property Type</option>
                            <option value="single-family">Single Family Home</option>
                            <option value="townhouse">Townhouse</option>
                            <option value="condo">Condominium</option>
                            <option value="multi-family">Multi-Family (2-4 units)</option>
                            <option value="apartment">Apartment Complex (5+ units)</option>
                            <option value="commercial">Commercial Building</option>
                            <option value="new-construction">New Construction</option>
                            <option value="other">Other</option>
                        </select>
                    </div>
                    
                    <div class="form-group">
                        <label for="propertyRole">Your Role *</label>
                        <select id="propertyRole" name="propertyRole" required>
                            <option value="">Select Your Role</option>
                            <option value="homeowner">Homeowner</option>
                            <option value="realtor">Real Estate Agent</option>
                            <option value="property-manager">Property Manager</option>
                            <option value="builder">Builder/Contractor</option>
                            <option value="investor">Real Estate Investor</option>
                            <option value="tenant">Tenant</option>
                            <option value="other">Other</option>
                        </select>
                    </div>
                    
                    <div class="form-group">
                        <label for="currentInsurance">Current Insurance Carrier</label>
                        <select id="currentInsurance" name="currentInsurance">
                            <option value="">Select Current Carrier</option>
                            <option value="state-farm">State Farm</option>
                            <option value="allstate">Allstate</option>
                            <option value="progressive">Progressive</option>
                            <option value="geico">GEICO</option>
                            <option value="farmers">Farmers</option>
                            <option value="usaa">USAA</option>
                            <option value="liberty-mutual">Liberty Mutual</option>
                            <option value="travelers">Travelers</option>
                            <option value="nationwide">Nationwide</option>
                            <option value="american-family">American Family</option>
                            <option value="other">Other</option>
                            <option value="none">No Current Insurance</option>
                        </select>
                    </div>
                    
                    <div class="form-group">
                        <label>Services Needed (check all that apply)</label>
                        <div class="checkbox-group">
                            <div class="checkbox-item">
                                <input type="checkbox" id="hail-inspection" name="servicesNeeded" value="hail-inspection">
                                <label for="hail-inspection">Hail Damage Inspection</label>
                            </div>
                            <div class="checkbox-item">
                                <input type="checkbox" id="insurance-quote" name="servicesNeeded" value="insurance-quote">
                                <label for="insurance-quote">Insurance Quote</label>
                            </div>
                            <div class="checkbox-item">
                                <input type="checkbox" id="real-estate" name="servicesNeeded" value="real-estate">
                                <label for="real-estate">Real Estate Services</label>
                            </div>
                            <div class="checkbox-item">
                                <input type="checkbox" id="property-management" name="servicesNeeded" value="property-management">
                                <label for="property-management">Property Management</label>
                            </div>
                            <div class="checkbox-item">
                                <input type="checkbox" id="construction" name="servicesNeeded" value="construction">
                                <label for="construction">Construction/Repair</label>
                            </div>
                            <div class="checkbox-item">
                                <input type="checkbox" id="claims-assistance" name="servicesNeeded" value="claims-assistance">
                                <label for="claims-assistance">Claims Assistance</label>
                            </div>
                        </div>
                    </div>
                    
                    <div class="form-group">
                        <label for="hailSize">What size hail did you see? (optional)</label>
                        <select id="hailSize" name="hailSize">
                            <option value="">Select Hail Size</option>
                            <option value="pea">Pea size (1/4 inch)</option>
                            <option value="quarter">Quarter size (1 inch)</option>
                            <option value="golf-ball">Golf ball size (1.75 inches)</option>
                            <option value="baseball">Baseball size (2.75 inches)</option>
                            <option value="softball">Softball size (4 inches)</option>
                            <option value="unknown">Not sure</option>
                        </select>
                    </div>
                    
                    <div class="form-group">
                        <label>When did the hail occur? (check all that apply)</label>
                        <div class="checkbox-group">
                            <div class="checkbox-item">
                                <input type="checkbox" id="recent" name="hailTime" value="recent">
                                <label for="recent">Within last 7 days</label>
                            </div>
                            <div class="checkbox-item">
                                <input type="checkbox" id="month" name="hailTime" value="month">
                                <label for="month">Within last month</label>
                            </div>
                            <div class="checkbox-item">
                                <input type="checkbox" id="year" name="hailTime" value="year">
                                <label for="year">Within last year</label>
                            </div>
                        </div>
                    </div>
                    
                    <div class="form-group">
                        <label>What type of damage are you concerned about? (check all that apply)</label>
                        <div class="checkbox-group">
                            <div class="checkbox-item">
                                <input type="checkbox" id="roof" name="damageType" value="roof">
                                <label for="roof">Roof damage</label>
                            </div>
                            <div class="checkbox-item">
                                <input type="checkbox" id="siding" name="damageType" value="siding">
                                <label for="siding">Siding damage</label>
                            </div>
                            <div class="checkbox-item">
                                <input type="checkbox" id="windows" name="damageType" value="windows">
                                <label for="windows">Window damage</label>
                            </div>
                            <div class="checkbox-item">
                                <input type="checkbox" id="gutters" name="damageType" value="gutters">
                                <label for="gutters">Gutter damage</label>
                            </div>
                            <div class="checkbox-item">
                                <input type="checkbox" id="auto-damage" name="damageType" value="auto">
                                <label for="auto-damage">Vehicle damage</label>
                            </div>
                            <div class="checkbox-item">
                                <input type="checkbox" id="unknown" name="damageType" value="unknown">
                                <label for="unknown">Not sure - need inspection</label>
                            </div>
                        </div>
                    </div>
                    
                    <div class="form-group">
                        <label for="urgency">How urgent is this inspection?</label>
                        <select id="urgency" name="urgency">
                            <option value="">Select Urgency</option>
                            <option value="immediate">Immediate - same day</option>
                            <option value="urgent">Urgent - within 24 hours</option>
                            <option value="soon">Soon - within a week</option>
                            <option value="flexible">Flexible - whenever convenient</option>
                        </select>
                    </div>
                    
                    <div class="form-group">
                        <label for="comments">Additional Comments (optional)</label>
                        <textarea id="comments" name="comments" rows="3" placeholder="Tell us more about your situation..."></textarea>
                    </div>
                    
                    <button type="submit" class="btn">Get My FREE Assessment</button>
                    <button type="button" class="btn btn-secondary" onclick="requestServiceQuote()">Request Service Quote</button>
                    <button type="button" class="btn btn-tertiary" onclick="becomePartner()">Become a Partner</button>
                </form>
            </div>
        </div>
        
        <div class="testimonials">
            <h2 style="text-align: center; margin-bottom: 30px; color: #2E86AB;">What Our Partners & Customers Say</h2>
            <div class="testimonial">
                <div class="testimonial-text">"As a real estate agent, their pre-listing inspections have helped me close deals faster and avoid surprises. The comprehensive reports give my clients confidence."</div>
                <div class="testimonial-author">- Maria S., Realtor, Plano</div>
            </div>
            <div class="testimonial">
                <div class="testimonial-text">"Managing 50+ units, I need reliable partners. Their multi-unit inspection process is efficient and their damage assessments are thorough."</div>
                <div class="testimonial-author">- David L., Property Manager, Dallas</div>
            </div>
            <div class="testimonial">
                <div class="testimonial-text">"We've partnered with them for quality control on new construction. Their attention to detail ensures our homes meet the highest standards."</div>
                <div class="testimonial-author">- Robert K., Builder, Frisco</div>
            </div>
        </div>
        
        <div class="footer">
            <p><strong>Licensed & Insured</strong> | Serving DFW Metroplex | Free Inspections | Comprehensive Partnerships</p>
            <p>© 2025 Complete Property Solutions. All rights reserved.</p>
        </div>
    </div>
    
    <script>
        function switchTab(tabName) {
            // Hide all tab contents
            document.querySelectorAll('.tab-content').forEach(content => {
                content.classList.remove('active');
            });
            
            // Remove active class from all tabs
            document.querySelectorAll('.tab').forEach(tab => {
                tab.classList.remove('active');
            });
            
            // Show selected tab content
            document.getElementById(tabName).classList.add('active');
            
            // Add active class to clicked tab
            event.target.classList.add('active');
        }
        
        function requestServiceQuote() {
            alert('Service quote request will be processed with your assessment. Our partners will contact you within 24 hours.');
        }
        
        function becomePartner() {
            alert('Thank you for your interest in becoming a partner! We will contact you within 48 hours to discuss partnership opportunities.');
        }
        
        // Form submission handling
        document.getElementById('comprehensiveForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Collect form data
            const formData = new FormData(this);
            const data = Object.fromEntries(formData.entries());
            
            // Add timestamp
            data.timestamp = new Date().toISOString();
            
            // Add lead score
            data.leadScore = calculateComprehensiveLeadScore(data);
            
            // Add service flags
            data.hasHailInspection = data.servicesNeeded && data.servicesNeeded.includes('hail-inspection');
            data.hasInsuranceInterest = data.servicesNeeded && data.servicesNeeded.includes('insurance-quote');
            data.hasRealEstateInterest = data.servicesNeeded && data.servicesNeeded.includes('real-estate');
            data.hasPropertyMgmtInterest = data.servicesNeeded && data.servicesNeeded.includes('property-management');
            data.hasConstructionInterest = data.servicesNeeded && data.servicesNeeded.includes('construction');
            data.hasClaimsInterest = data.servicesNeeded && data.servicesNeeded.includes('claims-assistance');
            
            // Save to localStorage (in real implementation, send to server)
            const leads = JSON.parse(localStorage.getItem('comprehensiveLeads') || '[]');
            leads.push(data);
            localStorage.setItem('comprehensiveLeads', JSON.stringify(leads));
            
            // Show success message
            alert('Thank you! We will contact you within 24 hours to schedule your FREE assessment and connect you with our partner network.');
            
            // Reset form
            this.reset();
        });
        
        function calculateComprehensiveLeadScore(data) {
            let score = 0;
            
            // Hail size scoring
            if (data.hailSize === 'baseball' || data.hailSize === 'softball') score += 30;
            else if (data.hailSize === 'golf-ball') score += 20;
            else if (data.hailSize === 'quarter') score += 10;
            
            // Time urgency
            if (data.urgency === 'immediate') score += 25;
            else if (data.urgency === 'urgent') score += 15;
            else if (data.urgency === 'soon') score += 5;
            
            // Property role scoring
            if (data.propertyRole === 'realtor') score += 20;
            else if (data.propertyRole === 'property-manager') score += 25;
            else if (data.propertyRole === 'builder') score += 20;
            else if (data.propertyRole === 'investor') score += 15;
            else if (data.propertyRole === 'homeowner') score += 10;
            
            // Property type scoring
            if (data.propertyType === 'apartment') score += 30;
            else if (data.propertyType === 'multi-family') score += 25;
            else if (data.propertyType === 'commercial') score += 20;
            else if (data.propertyType === 'new-construction') score += 15;
            
            // Insurance status
            if (data.currentInsurance === 'none') score += 20;
            else if (data.currentInsurance) score += 10;
            
            // Services needed scoring
            const services = data.servicesNeeded || [];
            if (services.includes('hail-inspection')) score += 15;
            if (services.includes('property-management')) score += 20;
            if (services.includes('real-estate')) score += 15;
            if (services.includes('construction')) score += 15;
            if (services.includes('insurance-quote')) score += 10;
            if (services.includes('claims-assistance')) score += 10;
            
            // Damage types
            const damageTypes = data.damageType || [];
            if (damageTypes.includes('roof')) score += 20;
            if (damageTypes.includes('siding')) score += 10;
            if (damageTypes.includes('windows')) score += 10;
            if (damageTypes.includes('auto')) score += 15;
            
            return score;
        }
    </script>
</body>
</html>"""
    
    # Create the comprehensive file
    with open('comprehensive_partnership_website.html', 'w', encoding='utf-8') as f:
        f.write(landing_page)
    
    print("✅ Created: comprehensive_partnership_website.html")   
    
    # Create comprehensive lead management system
    create_comprehensive_lead_management()

def create_comprehensive_lead_management():
    """
    Create comprehensive lead management with all partnership types
    """
    
    lead_manager = """<!DOCTYPE html>
<htm   l lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Comprehensive Lead Management Dashboard</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background: #f5f5f5;
        }
        
        .container {
            max-width: 1600px;
            margin: 0 auto;
        }
        
        .header {
            background: white;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        
        .stat-card {
            background: white;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        .stat-number {
            font-size: 2em;
            font-weight: bold;
            color: #2E86AB;
        }
        
        .stat-label {
            color: #666;
            margin-top: 5px;
        }
        
        .partnership-stats {
            background: white;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        .partnership-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin-top: 15px;
        }
        
        .partnership-stat-card {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            text-align: center;
            border-left: 4px solid #2E86AB;
        }
        
        .leads-table {
            background: white;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
        }
        
        th, td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #eee;
        }
        
        th {
            background: #2E86AB;
            color: white;
            font-weight: bold;
        }
        
        .priority-high {
            background: #ffebee;
            color: #c62828;
            font-weight: bold;
        }
        
        .priority-medium {
            background: #fff3e0;
            color: #ef6c00;
        }
        
        .priority-low {
            background: #e8f5e8;
            color: #2e7d32;
        }
        
        .service-badge {
            display: inline-block;
            background: #e3f2fd;
            color: #1565c0;
            padding: 2px 8px;
            border-radius: 12px;
            font-size: 0.8em;
            margin: 2px;
        }
        
        .role-badge {
            display: inline-block;
            background: #f3e5f5;
            color: #7b1fa2;
            padding: 2px 8px;
            border-radius: 12px;
            font-size: 0.8em;
            margin: 2px;
        }
        
        .btn {
            background: #2E86AB;
            color: white;
            padding: 8px 16px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            margin: 2px;
        }
        
        .btn:hover {
            background: #1e5f7a;
        }
        
        .btn-realtor {
            background: #4CAF50;
        }
        
        .btn-property-mgmt {
            background: #FF9800;
        }
        
        .btn-construction {
            background: #9C27B0;
        }
        
        .btn-insurance {
            background: #2196F3;
        }
        
        .filters {
            background: white;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        .filter-group {
            display: inline-block;
            margin-right: 20px;
        }
        
        .filter-group label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        
        .filter-group select {
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎯 Comprehensive Lead Management Dashboard</h1>
            <p>Manage leads across all partnership types: Real Estate, Property Management, Construction, and Insurance</p>
        </div>
        
        <div class="stats" id="stats">
            <!-- Stats will be populated by JavaScript -->
        </div>
        
        <div class="partnership-stats">
            <h3>Partnership Service Analysis</h3>
            <div class="partnership-grid" id="partnershipStats">
                <!-- Partnership stats will be populated by JavaScript -->
            </div>
        </div>
        
        <div class="filters">
            <div class="filter-group">
                <label>Priority Level:</label>
                <select id="priorityFilter">
                    <option value="">All Priorities</option>
                    <option value="high">High Priority (70+)</option>
                    <option value="medium">Medium Priority (40-69)</option>
                    <option value="low">Low Priority (<40)</option>
                </select>
            </div>
            
            <div class="filter-group">
                <label>Property Role:</label>
                <select id="roleFilter">
                    <option value="">All Roles</option>
                    <option value="realtor">Real Estate Agent</option>
                    <option value="property-manager">Property Manager</option>
                    <option value="builder">Builder/Contractor</option>
                    <option value="investor">Real Estate Investor</option>
                    <option value="homeowner">Homeowner</option>
                    <option value="tenant">Tenant</option>
                </select>
            </div>
            
            <div class="filter-group">
                <label>Service Type:</label>
                <select id="serviceFilter">
                    <option value="">All Services</option>
                    <option value="hail-inspection">Hail Inspection</option>
                    <option value="insurance-quote">Insurance Quote</option>
                    <option value="real-estate">Real Estate</option>
                    <option value="property-management">Property Management</option>
                    <option value="construction">Construction</option>
                    <option value="claims-assistance">Claims Assistance</option>
                </select>
            </div>
            
            <div class="filter-group">
                <label>Property Type:</label>
                <select id="propertyTypeFilter">
                    <option value="">All Types</option>
                    <option value="single-family">Single Family</option>
                    <option value="multi-family">Multi-Family</option>
                    <option value="apartment">Apartment Complex</option>
                    <option value="commercial">Commercial</option>
                    <option value="new-construction">New Construction</option>
                </select>
            </div>
            
            <div class="filter-group">
                <label>City:</label>
                <select id="cityFilter">
                    <option value="">All Cities</option>
                </select>
            </div>
            
            <button class="btn" onclick="exportLeads()">Export All Leads</button>
            <button class="btn" onclick="exportByService()">Export by Service</button>
            <button class="btn" onclick="refreshData()">Refresh</button>
        </div>
        
        <div class="leads-table">
            <table id="leadsTable">
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Contact</th>
                        <th>Role</th>
                        <th>Property</th>
                        <th>Services</th>
                        <th>Priority</th>
                        <th>Score</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody id="leadsTableBody">
                    <!-- Leads will be populated by JavaScript -->
                </tbody>
            </table>
        </div>
    </div>
    
    <script>
        let leads = [];
        
        function loadLeads() {
            // Load leads from localStorage
            leads = JSON.parse(localStorage.getItem('comprehensiveLeads') || '[]');
            updateStats();
            updatePartnershipStats();
            updateTable();
            updateFilters();
        }
        
        function updateStats() {
            const total = leads.length;
            const high = leads.filter(l => l.leadScore >= 70).length;
            const medium = leads.filter(l => l.leadScore >= 40 && l.leadScore < 70).length;
            const low = leads.filter(l => l.leadScore < 40).length;
            
            // Count by role
            const realtors = leads.filter(l => l.propertyRole === 'realtor').length;
            const propertyMgrs = leads.filter(l => l.propertyRole === 'property-manager').length;
            const builders = leads.filter(l => l.propertyRole === 'builder').length;
            const homeowners = leads.filter(l => l.propertyRole === 'homeowner').length;
            
            document.getElementById('stats').innerHTML = `
                <div class="stat-card">
                    <div class="stat-number">${total}</div>
                    <div>Total Leads</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">${high}</div>
                    <div>High Priority</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">${realtors}</div>
                    <div>Real Estate Agents</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">${propertyMgrs}</div>
                    <div>Property Managers</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">${builders}</div>
                    <div>Builders/Contractors</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">${homeowners}</div>
                    <div>Homeowners</div>
                </div>
            `;
        }
        
        function updatePartnershipStats() {
            const hailInspection = leads.filter(l => l.hasHailInspection).length;
            const insurance = leads.filter(l => l.hasInsuranceInterest).length;
            const realEstate = leads.filter(l => l.hasRealEstateInterest).length;
            const propertyMgmt = leads.filter(l => l.hasPropertyMgmtInterest).length;
            const construction = leads.filter(l => l.hasConstructionInterest).length;
            const claims = leads.filter(l => l.hasClaimsInterest).length;
            
            document.getElementById('partnershipStats').innerHTML = `
                <div class="partnership-stat-card">
                    <div class="stat-number">${hailInspection}</div>
                    <div>Hail Inspections</div>
                </div>
                <div class="partnership-stat-card">
                    <div class="stat-number">${insurance}</div>
                    <div>Insurance Quotes</div>
                </div>
                <div class="partnership-stat-card">
                    <div class="stat-number">${realEstate}</div>
                    <div>Real Estate Services</div>
                </div>
                <div class="partnership-stat-card">
                    <div class="stat-number">${propertyMgmt}</div>
                    <div>Property Management</div>
                </div>
                <div class="partnership-stat-card">
                    <div class="stat-number">${construction}</div>
                    <div>Construction Services</div>
                </div>
                <div class="partnership-stat-card">
                    <div class="stat-number">${claims}</div>
                    <div>Claims Assistance</div>
                </div>
            `;
        }
        
        function updateTable() {
            const tbody = document.getElementById('leadsTableBody');
            const priorityFilter = document.getElementById('priorityFilter').value;
            const roleFilter = document.getElementById('roleFilter').value;
            const serviceFilter = document.getElementById('serviceFilter').value;
            const propertyTypeFilter = document.getElementById('propertyTypeFilter').value;
            const cityFilter = document.getElementById('cityFilter').value;
            
            let filteredLeads = leads;
            
            // Apply filters
            if (priorityFilter) {
                if (priorityFilter === 'high') {
                    filteredLeads = filteredLeads.filter(l => l.leadScore >= 70);
                } else if (priorityFilter === 'medium') {
                    filteredLeads = filteredLeads.filter(l => l.leadScore >= 40 && l.leadScore < 70);
                } else if (priorityFilter === 'low') {
                    filteredLeads = filteredLeads.filter(l => l.leadScore < 40);
                }
            }
            
            if (roleFilter) {
                filteredLeads = filteredLeads.filter(l => l.propertyRole === roleFilter);
            }
            
            if (serviceFilter) {
                filteredLeads = filteredLeads.filter(l => {
                    const services = l.servicesNeeded || [];
                    return services.includes(serviceFilter);
                });
            }
            
            if (propertyTypeFilter) {
                filteredLeads = filteredLeads.filter(l => l.propertyType === propertyTypeFilter);
            }
            
            if (cityFilter) {
                filteredLeads = filteredLeads.filter(l => l.city === cityFilter);
            }
            
            // Sort by lead score (highest first)
            filteredLeads.sort((a, b) => (b.leadScore || 0) - (a.leadScore || 0));
            
            tbody.innerHTML = filteredLeads.map(lead => {
                const priority = getPriority(lead.leadScore);
                const priorityClass = `priority-${priority}`;
                
                // Create service badges
                const services = lead.servicesNeeded || [];
                const serviceBadges = services.map(service => 
                    `<span class="service-badge">${service.replace('-', ' ')}</span>`
                ).join('');
                
                // Create role badge
                const roleBadge = `<span class="role-badge">${lead.propertyRole || 'Unknown'}</span>`;
                
                return `
                    <tr>
                        <td>${lead.firstName} ${lead.lastName}</td>
                        <td>
                            <div>${lead.email}</div>
                            <div>${lead.phone}</div>
                        </td>
                        <td>${roleBadge}</td>
                        <td>
                            <div>${lead.address}</div>
                            <div>${lead.city}, ${lead.zipcode}</div>
                            <div><small>${lead.propertyType || 'Unknown'}</small></div>
                        </td>
                        <td>${serviceBadges}</td>
                        <td class="${priorityClass}">${priority.toUpperCase()}</td>
                        <td>${lead.leadScore || 0}</td>
                        <td>
                            <button class="btn" onclick="contactLead('${lead.email}')">Contact</button>
                            <button class="btn" onclick="scheduleLead('${lead.email}')">Schedule</button>
                            ${lead.hasRealEstateInterest ? '<button class="btn btn-realtor" onclick="assignRealtor(\'' + lead.email + '\')">Realtor</button>' : ''}
                            ${lead.hasPropertyMgmtInterest ? '<button class="btn btn-property-mgmt" onclick="assignPropertyMgmt(\'' + lead.email + '\')">Prop Mgmt</button>' : ''}
                            ${lead.hasConstructionInterest ? '<button class="btn btn-construction" onclick="assignConstruction(\'' + lead.email + '\')">Construction</button>' : ''}
                            ${lead.hasInsuranceInterest ? '<button class="btn btn-insurance" onclick="assignInsurance(\'' + lead.email + '\')">Insurance</button>' : ''}
                        </td>
                    </tr>
                `;
            }).join('');
        }
        
        function getPriority(score) {
            if (score >= 70) return 'high';
            if (score >= 40) return 'medium';
            return 'low';
        }
        
        function updateFilters() {
            const cities = [...new Set(leads.map(l => l.city))].filter(Boolean);
            const citySelect = document.getElementById('cityFilter');
            
            citySelect.innerHTML = '<option value="">All Cities</option>' +
                cities.map(city => `<option value="${city}">${city}</option>`).join('');
        }
        
        function contactLead(email) {
            alert(`Contacting lead: ${email}`);
        }
        
        function scheduleLead(email) {
            alert(`Scheduling inspection for: ${email}`);
        }
        
        function assignRealtor(email) {
            alert(`Assigning to real estate partner: ${email}`);
        }
        
        function assignPropertyMgmt(email) {
            alert(`Assigning to property management partner: ${email}`);
        }
        
        function assignConstruction(email) {
            alert(`Assigning to construction partner: ${email}`);
        }
        
        function assignInsurance(email) {
            alert(`Assigning to insurance partner: ${email}`);
        }
        
        function exportLeads() {
            const csv = convertToCSV(leads);
            downloadCSV(csv, 'comprehensive_leads.csv');
        }
        
        function exportByService() {
            const service = prompt('Enter service type to export (hail-inspection, insurance-quote, real-estate, property-management, construction, claims-assistance):');
            if (service) {
                const filteredLeads = leads.filter(l => {
                    const services = l.servicesNeeded || [];
                    return services.includes(service);
                });
                const csv = convertToCSV(filteredLeads);
                downloadCSV(csv, `${service}_leads.csv`);
            }
        }
        
        function convertToCSV(data) {
            if (data.length === 0) return '';
            
            const headers = Object.keys(data[0]);
            const csvContent = [
                headers.join(','),
                ...data.map(row => headers.map(header => `"${row[header] || ''}"`).join(','))
            ].join('\\n');
            
            return csvContent;
        }
        
        function downloadCSV(csv, filename) {
            const blob = new Blob([csv], { type: 'text/csv' });
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = filename;
            a.click();
            window.URL.revokeObjectURL(url);
        }
        
        function refreshData() {
            loadLeads();
        }
        
        // Event listeners
        document.getElementById('priorityFilter').addEventListener('change', updateTable);
        document.getElementById('roleFilter').addEventListener('change', updateTable);
        document.getElementById('serviceFilter').addEventListener('change', updateTable);
        document.getElementById('propertyTypeFilter').addEventListener('change', updateTable);
        document.getElementById('cityFilter').addEventListener('change', updateTable);
        
        // Load data on page load
        loadLeads();
    </script>
</body>
</html>"""
    
    with open('comprehensive_lead_management_dashboard.html', 'w', encoding='utf-8') as f:
        f.write(lead_manager)
    
    print("✅ Created: comprehensive_lead_management_dashboard.html")

if __name__ == "__main__":
    create_comprehensive_partnership_website()
    print("\n🎉 Comprehensive partnership website created!")
    print("\nFiles created:")
    print("  - comprehensive_partnership_website.html (main landing page)")
    print("  - comprehensive_lead_management_dashboard.html (admin dashboard)")
    print("\nPartnership Types Included:")
    print("  ✓ Real Estate Agents")
    print("  ✓ Property Managers")
    print("  ✓ Builders & Contractors")
    print("  ✓ Insurance Partners")
    print("\nFeatures:")
    print("  ✓ Multi-service lead capture")
    print("  ✓ Role-based lead scoring")
    print("  ✓ Service-specific filtering")
    print("  ✓ Partnership assignment tools")
    print("  ✓ Comprehensive reporting")
    print("\nTo use:")
    print("  1. Open comprehensive_partnership_website.html in browser")
    print("  2. Test the enhanced form with all partnership types")
    print("  3. Open comprehensive_lead_management_dashboard.html to view leads")
    print("  4. Deploy both files to your web server")
