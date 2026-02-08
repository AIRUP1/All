"""
Add Property Owner Information from Texas County Appraisal Districts
Uses official public records from county appraisal district APIs/websites

LEGAL NOTICE: This uses PUBLIC RECORDS only. Property data is public in Texas.
However, use of this data for unsolicited contact may be regulated by state/federal law.
"""
import pandas as pd
import requests
from time import sleep
import json

print("=" * 70)
print("TEXAS COUNTY PROPERTY RECORDS MATCHER")
print("=" * 70)
print("\nIMPORTANT LEGAL NOTICES:")
print("  ✓ Property records are PUBLIC in Texas")
print("  ✓ County Appraisal Districts provide this data")
print("  ⚠ TCPA/DNC laws apply for phone/text contact")
print("  ⚠ CAN-SPAM Act applies for email marketing")
print("  ⚠ Always follow applicable solicitation laws")
print("=" * 70)

# Load your hail events
df = pd.read_csv('hail_events_dfw_2024_2025_neighborhoods.csv')
df = df[(df['LAT'].notna()) & (df['LON'].notna())].copy()

print(f"\nLoaded {len(df)} hail events with coordinates")

# ==================================================================
# TEXAS COUNTY APPRAISAL DISTRICTS - OFFICIAL SOURCES
# ==================================================================

COUNTY_APPRAISAL_DISTRICTS = {
    'COLLIN': {
        'name': 'Collin County Appraisal District',
        'website': 'https://www.collincad.org',
        'data_portal': 'https://www.collincad.org/propertysearch',
        'cities': ['McKinney', 'Plano', 'Frisco', 'Allen', 'Wylie', 'Anna', 'Melissa', 
                  'Prosper', 'Celina', 'Princeton', 'Murphy', 'Parker', 'Lucas']
    },
    'DALLAS': {
        'name': 'Dallas Central Appraisal District',
        'website': 'https://www.dallascad.org',
        'data_portal': 'https://www.dallascad.org/PropertySearch.aspx',
        'cities': ['Dallas', 'Garland', 'Irving', 'Mesquite', 'Richardson', 'Carrollton',
                  'Grand Prairie', 'Rowlett', 'DeSoto', 'Cedar Hill']
    },
    'TARRANT': {
        'name': 'Tarrant Appraisal District',
        'website': 'https://www.tad.org',
        'data_portal': 'https://www.tad.org/property-search/',
        'cities': ['Fort Worth', 'Arlington', 'Grapevine', 'Hurst', 'Bedford', 'Euless',
                  'Mansfield', 'North Richland Hills', 'Keller', 'Southlake', 'Colleyville']
    },
    'DENTON': {
        'name': 'Denton Central Appraisal District',
        'website': 'https://www.dentoncad.com',
        'data_portal': 'https://www.dentoncad.com/property-search/',
        'cities': ['Denton', 'Flower Mound', 'Lewisville', 'The Colony', 'Little Elm',
                  'Corinth', 'Highland Village', 'Trophy Club', 'Argyle', 'Roanoke']
    },
    'ROCKWALL': {
        'name': 'Rockwall Central Appraisal District',
        'website': 'https://www.rockwallcad.com',
        'data_portal': 'https://www.rockwallcad.com/property-search/',
        'cities': ['Rockwall', 'Rowlett', 'Heath', 'Fate', 'Royse City']
    }
}

print("\n" + "=" * 70)
print("ACCESSING OFFICIAL COUNTY APPRAISAL DISTRICTS")
print("=" * 70)

for county, info in COUNTY_APPRAISAL_DISTRICTS.items():
    county_events = len(df[df['COUNTY'] == county])
    print(f"\n{county:str} COUNTY:")
    print(f"  District: {info['name']}")
    print(f"  Website: {info['website']}")
    print(f"  Data Portal: {info['data_portal']}")
    print(f"  Hail Events: {county_events}")
    print(f"  Cities: {', '.join(info['cities'][:5])}...")

# ==================================================================
# GUIDE: HOW TO GET PROPERTY OWNER DATA
# ==================================================================

print("\n" + "=" * 70)
print("HOW TO OBTAIN PROPERTY OWNER INFORMATION")
print("=" * 70)

guide = """
OPTION 1: BULK DATA DOWNLOADS (RECOMMENDED)
--------------------------------------------
Most Texas CADs provide bulk data downloads:

1. COLLIN COUNTY:
   - Visit: https://www.collincad.org
   - Go to: Data Downloads or Public Records section
   - Download: Certified Property Data (CSV/Excel)
   - Contains: Owner names, addresses, property details

2. DALLAS COUNTY:
   - Visit: https://www.dallascad.org
   - Look for: Open Data Portal
   - Download: Property data files

3. TARRANT COUNTY:
   - Visit: https://www.tad.org
   - Section: Data Products or Public Information
   - Request: Bulk property data

4. DENTON COUNTY:
   - Visit: https://www.dentoncad.com
   - Navigate to: Public Records Request
   - Download available datasets

OPTION 2: API ACCESS (TECHNICAL)
---------------------------------
Some counties offer GIS/API services:
- Collin County: ArcGIS REST Services
- Dallas County: Open Data Portal API
- May require registration

OPTION 3: INDIVIDUAL LOOKUPS
-----------------------------
For smaller campaigns:
1. Go to county appraisal website
2. Use property search by address/coordinates
3. Export individual property records

OPTION 4: COMMERCIAL DATA SERVICES (PAID)
------------------------------------------
Licensed providers with pre-matched data:
- CoreLogic
- LexisNexis
- DataTree by First American
- Black Knight
- Melissa Data

These services provide:
✓ Pre-cleaned property owner data
✓ Contact information (when available)
✓ DNC scrubbing
✓ Legal compliance tools
"""

print(guide)

# ==================================================================
# CREATE PROPERTY LOOKUP TEMPLATE
# ==================================================================

print("\n" + "=" * 70)
print("CREATING PROPERTY LOOKUP TEMPLATE")
print("=" * 70)

# Create a template file for manual or automated property lookups
lookup_df = df[['EVENT_ID', 'BEGIN', 'COUNTY', 'city', 'neighborhood', 
                'postcode', 'LAT', 'LON', 'HAIL_SIZE_IN']].copy()

# Add empty columns for property data
lookup_df['property_address'] = ''
lookup_df['owner_name'] = ''
lookup_df['owner_mailing_address'] = ''
lookup_df['property_type'] = ''
lookup_df['year_built'] = ''
lookup_df['appraisal_value'] = ''
lookup_df['account_number'] = ''
lookup_df['data_source'] = ''
lookup_df['lookup_url'] = ''

# Add direct lookup URLs for each county
def create_lookup_url(row):
    county = row['COUNTY']
    lat = row['LAT']
    lon = row['LON']
    
    # Create county-specific URLs
    if county == 'COLLIN':
        return f"https://www.collincad.org/propertysearch"
    elif county == 'DALLAS':
        return f"https://www.dallascad.org/PropertySearch.aspx"
    elif county == 'TARRANT':
        return f"https://www.tad.org/property-search/"
    elif county == 'DENTON':
        return f"https://www.dentoncad.com/property-search/"
    elif county == 'ROCKWALL':
        return f"https://www.rockwallcad.com/property-search/"
    else:
        return ""

lookup_df['lookup_url'] = lookup_df.apply(create_lookup_url, axis=1)

# Sort by county and city for easier batch lookup
lookup_df = lookup_df.sort_values(['COUNTY', 'city', 'postcode'])

# Save template
template_file = 'property_lookup_template.csv'
lookup_df.to_csv(template_file, index=False)
print(f"\n✓ Created: {template_file}")
print(f"  - {len(lookup_df)} events ready for property matching")
print(f"  - Includes direct links to county appraisal websites")
print(f"  - Fill in owner information from county records")

# ==================================================================
# CREATE COUNTY-SPECIFIC LISTS
# ==================================================================

print("\n" + "=" * 70)
print("CREATING COUNTY-SPECIFIC LOOKUP FILES")
print("=" * 70)

for county in df['COUNTY'].unique():
    county_df = lookup_df[lookup_df['COUNTY'] == county].copy()
    if len(county_df) > 0:
        county_file = f'property_lookup_{county.lower()}_county.csv'
        county_df.to_csv(county_file, index=False)
        print(f"✓ {county} County: {len(county_df)} events → {county_file}")

# ==================================================================
# CREATE INSTRUCTIONS DOCUMENT
# ==================================================================

instructions = f"""
PROPERTY OWNER DATA COLLECTION INSTRUCTIONS
============================================

YOUR HAIL EVENTS DATA:
- Total Events: {len(df)}
- Events by County:
"""

for county in sorted(df['COUNTY'].unique()):
    count = len(df[df['COUNTY'] == county])
    instructions += f"  • {county}: {count} events\n"

instructions += """

STEP-BY-STEP PROCESS:
=====================

METHOD 1: BULK DATA DOWNLOAD (FASTEST)
---------------------------------------
1. Visit your target county's appraisal website
2. Navigate to "Data Downloads" or "Public Records"
3. Download the complete property owner database
4. Use Excel VLOOKUP or Python to match by coordinates/address
5. Merge with your hail events file

EXAMPLE: Collin County
- Go to: https://www.collincad.org
- Download: Property Owner Data (usually free)
- Match: Use zip code + approximate address matching

METHOD 2: MANUAL LOOKUP (SMALLER CAMPAIGNS)
--------------------------------------------
1. Open: property_lookup_[county]_county.csv
2. For each row:
   a. Click the 'lookup_url'
   b. Search by address or coordinates
   c. Copy owner name and mailing address
   d. Paste into the CSV
3. Save completed file

METHOD 3: HIRE A DATA SERVICE (RECOMMENDED FOR LARGE CAMPAIGNS)
----------------------------------------------------------------
Contact a licensed data provider:
- Melissa Data: https://www.melissa.com
- CoreLogic: https://www.corelogic.com
- DataTree: https://www.datatree.com

They can provide:
✓ Pre-matched property owners for your coordinates
✓ Verified mailing addresses
✓ Phone numbers (where legally available)
✓ DNC scrubbing
✓ Legal compliance

Cost: Usually $0.10-$0.50 per record

METHOD 4: API AUTOMATION (TECHNICAL)
-------------------------------------
If you have programming skills:
1. Register for county GIS/API access
2. Write script to query by coordinates
3. Auto-populate owner information
4. Respect rate limits and terms of service

LEGAL REMINDERS:
================
✓ Property records are PUBLIC in Texas
✓ You CAN use this for direct mail
✓ You CAN use for in-person visits (with permits)
✗ CANNOT make unsolicited calls without prior relationship
✗ CANNOT send unsolicited texts without consent
✗ MUST comply with CAN-SPAM for emails
✗ MUST honor Do Not Contact requests

NEXT STEPS:
===========
1. Choose your method above
2. Start with one county as a test
3. Match 10-20 properties to verify data quality
4. Scale up once process is working
5. Import completed data back into your marketing system

FILES CREATED:
==============
- property_lookup_template.csv (all events)
- property_lookup_[county]_county.csv (split by county)

SUPPORT RESOURCES:
==================
- Texas Property Code: https://statutes.capitol.texas.gov
- TCPA Compliance: https://www.fcc.gov/tcpa
- TDNC List: https://www.texasnocall.com
"""

instruction_file = 'PROPERTY_DATA_INSTRUCTIONS.txt'
with open(instruction_file, 'w', encoding='utf-8') as f:
    f.write(instructions)

print(f"\n✓ Created: {instruction_file}")

print("\n" + "=" * 70)
print("✓ PROPERTY LOOKUP SETUP COMPLETE!")
print("=" * 70)
print("\nFiles Created:")
print(f"  1. {template_file} - Master template")
for county in sorted(df['COUNTY'].unique()):
    if len(df[df['COUNTY'] == county]) > 0:
        print(f"  2. property_lookup_{county.lower()}_county.csv")
print(f"  3. {instruction_file} - Detailed instructions")

print("\nRECOMMENDED NEXT STEPS:")
print("  1. Read PROPERTY_DATA_INSTRUCTIONS.txt")
print("  2. Visit county appraisal websites for bulk data")
print("  3. OR hire a licensed data service for fastest results")
print("  4. Match property owners to your hail events")
print("  5. Launch your targeted marketing campaign!")

print("\n⚠️  IMPORTANT: Always comply with TCPA, CAN-SPAM, and local laws!")

