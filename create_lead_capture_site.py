"""
Professional Lead Capture Website
Creates a high-converting landing page with survey forms
"""
import os

def create_lead_capture_website():
    """
    Create a professional lead capture website
    """
    
    # Main landing page HTML
    landing_page = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hail Damage Assessment - Free Property Inspection</title>
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
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        .header {
            background: rgba(255,255,255,0.95);
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 30px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        }
        
        .header h1 {
            color: #2E86AB;
            font-size: 2.5em;
            margin-bottom: 10px;
            text-align: center;
        }
        
        .header p {
            font-size: 1.2em;
            text-align: center;
            color: #666;
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
            border-radius: 10px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        }
        
        .form-section {
            background: rgba(255,255,255,0.95);
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.1);
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
            border-radius: 5px;
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
            border-radius: 5px;
            font-size: 18px;
            font-weight: bold;
            cursor: pointer;
            width: 100%;
            transition: transform 0.3s;
        }
        
        .btn:hover {
            transform: translateY(-2px);
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
            border-radius: 10px;
            text-align: center;
            box-shadow: 0 5px 20px rgba(0,0,0,0.1);
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
        
        .testimonials {
            background: rgba(255,255,255,0.95);
            padding: 30px;
            border-radius: 10px;
            margin-top: 30px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        }
        
        .testimonial {
            margin-bottom: 20px;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 5px;
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
            padding: 20px;
            background: rgba(255,255,255,0.9);
            border-radius: 10px;
        }
        
        @media (max-width: 768px) {
            .main-content {
                grid-template-columns: 1fr;
            }
            
            .header h1 {
                font-size: 2em;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🌩️ Hail Damage Assessment</h1>
            <p>Get a FREE property inspection and damage estimate</p>
        </div>
        
        <div class="stats">
            <div class="stat-card">
                <div class="stat-number">515</div>
                <div class="stat-label">Hail Events in DFW</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">47</div>
                <div class="stat-label">Severe Events (2"+ hail)</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">158</div>
                <div class="stat-label">Affected Zip Codes</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">$0</div>
                <div class="stat-label">Inspection Cost</div>
            </div>
        </div>
        
        <div class="main-content">
            <div class="info-section">
                <h2>Why Choose Our Hail Damage Assessment?</h2>
                <ul style="list-style: none; padding: 0;">
                    <li style="margin-bottom: 15px; padding-left: 25px; position: relative;">
                        <span style="position: absolute; left: 0; color: #2E86AB; font-weight: bold;">✓</span>
                        <strong>FREE Inspection:</strong> No cost to you for initial assessment
                    </li>
                    <li style="margin-bottom: 15px; padding-left: 25px; position: relative;">
                        <span style="position: absolute; left: 0; color: #2E86AB; font-weight: bold;">✓</span>
                        <strong>Insurance Expertise:</strong> We work directly with your insurance company
                    </li>
                    <li style="margin-bottom: 15px; padding-left: 25px; position: relative;">
                        <span style="position: absolute; left: 0; color: #2E86AB; font-weight: bold;">✓</span>
                        <strong>Local Knowledge:</strong> We know your area and recent storm patterns
                    </li>
                    <li style="margin-bottom: 15px; padding-left: 25px; position: relative;">
                        <span style="position: absolute; left: 0; color: #2E86AB; font-weight: bold;">✓</span>
                        <strong>Quick Response:</strong> Same-day or next-day inspection available
                    </li>
                    <li style="margin-bottom: 15px; padding-left: 25px; position: relative;">
                        <span style="position: absolute; left: 0; color: #2E86AB; font-weight: bold;">✓</span>
                        <strong>Licensed & Insured:</strong> Fully certified roofing contractors
                    </li>
                </ul>
                
                <h3 style="margin-top: 30px; color: #2E86AB;">Recent Hail Events in Your Area:</h3>
                <p>Our data shows recent hail activity in your region. Don't wait - hail damage can worsen over time and may not be immediately visible.</p>
            </div>
            
            <div class="form-section">
                <h2>Get Your FREE Assessment</h2>
                <form id="leadForm" action="#" method="POST">
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
                            <option value="commercial">Commercial Building</option>
                            <option value="other">Other</option>
                        </select>
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
                                <input type="checkbox" id="unknown" name="damageType" value="unknown">
                                <label for="unknown">Not sure - need inspection</label>
                            </div>
                        </div>
                    </div>
                    
                    <div class="form-group">
                        <label for="insurance">Do you have homeowners insurance?</label>
                        <select id="insurance" name="insurance">
                            <option value="">Select Option</option>
                            <option value="yes">Yes, I have insurance</option>
                            <option value="no">No, I don't have insurance</option>
                            <option value="unsure">Not sure</option>
                        </select>
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
                </form>
            </div>
        </div>
        
        <div class="testimonials">
            <h2 style="text-align: center; margin-bottom: 30px; color: #2E86AB;">What Our Customers Say</h2>
            <div class="testimonial">
                <div class="testimonial-text">"They found hail damage I didn't even know was there. The insurance claim process was smooth and they handled everything."</div>
                <div class="testimonial-author">- Sarah M., Plano</div>
            </div>
            <div class="testimonial">
                <div class="testimonial-text">"Professional, honest, and thorough. They saved me thousands on my roof replacement through proper insurance coverage."</div>
                <div class="testimonial-author">- Mike R., Frisco</div>
            </div>
            <div class="testimonial">
                <div class="testimonial-text">"Quick response and excellent communication. They made the whole process stress-free."</div>
                <div class="testimonial-author">- Jennifer L., Arlington</div>
            </div>
        </div>
        
        <div class="footer">
            <p><strong>Licensed & Insured</strong> | Serving DFW Metroplex | Free Inspections</p>
            <p>© 2025 Hail Damage Assessment. All rights reserved.</p>
        </div>
    </div>
    
    <script>
        // Form submission handling
        document.getElementById('leadForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Collect form data
            const formData = new FormData(this);
            const data = Object.fromEntries(formData.entries());
            
            // Add timestamp
            data.timestamp = new Date().toISOString();
            
            // Add lead score
            data.leadScore = calculateLeadScore(data);
            
            // Save to localStorage (in real implementation, send to server)
            const leads = JSON.parse(localStorage.getItem('leads') || '[]');
            leads.push(data);
            localStorage.setItem('leads', JSON.stringify(leads));
            
            // Show success message
            alert('Thank you! We will contact you within 24 hours to schedule your FREE inspection.');
            
            // Reset form
            this.reset();
        });
        
        function calculateLeadScore(data) {
            let score = 0;
            
            // Hail size scoring
            if (data.hailSize === 'baseball' || data.hailSize === 'softball') score += 30;
            else if (data.hailSize === 'golf-ball') score += 20;
            else if (data.hailSize === 'quarter') score += 10;
            
            // Time urgency
            if (data.urgency === 'immediate') score += 25;
            else if (data.urgency === 'urgent') score += 15;
            else if (data.urgency === 'soon') score += 5;
            
            // Insurance status
            if (data.insurance === 'yes') score += 15;
            
            // Damage types
            const damageTypes = data.damageType || [];
            if (damageTypes.includes('roof')) score += 20;
            if (damageTypes.includes('siding')) score += 10;
            if (damageTypes.includes('windows')) score += 10;
            
            return score;
        }
    </script>
</body>
</html>"""
    
    # Create the file
    with open('lead_capture_website.html', 'w', encoding='utf-8') as f:
        f.write(landing_page)
    
    print("✅ Created: lead_capture_website.html")
    
    # Create lead management system
    create_lead_management_system()

def create_lead_management_system():
    """
    Create a lead management system to organize survey responses
    """
    
    lead_manager = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lead Management Dashboard</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background: #f5f5f5;
        }
        
        .container {
            max-width: 1400px;
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
            <h1>🎯 Lead Management Dashboard</h1>
            <p>Manage and organize your hail damage leads</p>
        </div>
        
        <div class="stats" id="stats">
            <!-- Stats will be populated by JavaScript -->
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
                <label>City:</label>
                <select id="cityFilter">
                    <option value="">All Cities</option>
                </select>
            </div>
            
            <div class="filter-group">
                <label>Status:</label>
                <select id="statusFilter">
                    <option value="">All Statuses</option>
                    <option value="new">New</option>
                    <option value="contacted">Contacted</option>
                    <option value="scheduled">Scheduled</option>
                    <option value="completed">Completed</option>
                </select>
            </div>
            
            <button class="btn" onclick="exportLeads()">Export CSV</button>
            <button class="btn" onclick="refreshData()">Refresh</button>
        </div>
        
        <div class="leads-table">
            <table id="leadsTable">
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Contact</th>
                        <th>Location</th>
                        <th>Hail Size</th>
                        <th>Priority</th>
                        <th>Score</th>
                        <th>Status</th>
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
            leads = JSON.parse(localStorage.getItem('leads') || '[]');
            updateStats();
            updateTable();
            updateFilters();
        }
        
        function updateStats() {
            const total = leads.length;
            const high = leads.filter(l => l.leadScore >= 70).length;
            const medium = leads.filter(l => l.leadScore >= 40 && l.leadScore < 70).length;
            const low = leads.filter(l => l.leadScore < 40).length;
            
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
                    <div class="stat-number">${medium}</div>
                    <div>Medium Priority</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">${low}</div>
                    <div>Low Priority</div>
                </div>
            `;
        }
        
        function updateTable() {
            const tbody = document.getElementById('leadsTableBody');
            const priorityFilter = document.getElementById('priorityFilter').value;
            const cityFilter = document.getElementById('cityFilter').value;
            const statusFilter = document.getElementById('statusFilter').value;
            
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
            
            if (cityFilter) {
                filteredLeads = filteredLeads.filter(l => l.city === cityFilter);
            }
            
            if (statusFilter) {
                filteredLeads = filteredLeads.filter(l => (l.status || 'new') === statusFilter);
            }
            
            // Sort by lead score (highest first)
            filteredLeads.sort((a, b) => (b.leadScore || 0) - (a.leadScore || 0));
            
            tbody.innerHTML = filteredLeads.map(lead => {
                const priority = getPriority(lead.leadScore);
                const priorityClass = `priority-${priority}`;
                
                return `
                    <tr>
                        <td>${lead.firstName} ${lead.lastName}</td>
                        <td>
                            <div>${lead.email}</div>
                            <div>${lead.phone}</div>
                        </td>
                        <td>
                            <div>${lead.address}</div>
                            <div>${lead.city}, ${lead.zipcode}</div>
                        </td>
                        <td>${lead.hailSize || 'Unknown'}</td>
                        <td class="${priorityClass}">${priority.toUpperCase()}</td>
                        <td>${lead.leadScore || 0}</td>
                        <td>${lead.status || 'New'}</td>
                        <td>
                            <button class="btn" onclick="contactLead('${lead.email}')">Contact</button>
                            <button class="btn" onclick="scheduleLead('${lead.email}')">Schedule</button>
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
            // In real implementation, open email client or CRM
        }
        
        function scheduleLead(email) {
            alert(`Scheduling inspection for: ${email}`);
            // In real implementation, open calendar or scheduling system
        }
        
        function exportLeads() {
            const csv = convertToCSV(leads);
            downloadCSV(csv, 'hail_damage_leads.csv');
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
        document.getElementById('cityFilter').addEventListener('change', updateTable);
        document.getElementById('statusFilter').addEventListener('change', updateTable);
        
        // Load data on page load
        loadLeads();
    </script>
</body>
</html>"""
    
    with open('lead_management_dashboard.html', 'w', encoding='utf-8') as f:
        f.write(lead_manager)
    
    print("✅ Created: lead_management_dashboard.html")

if __name__ == "__main__":
    create_lead_capture_website()
    print("\n🎉 Lead capture website created!")
    print("\nFiles created:")
    print("  - lead_capture_website.html (main landing page)")
    print("  - lead_management_dashboard.html (admin dashboard)")
    print("\nTo use:")
    print("  1. Open lead_capture_website.html in browser")
    print("  2. Test the form submission")
    print("  3. Open lead_management_dashboard.html to view leads")
    print("  4. Deploy both files to your web server")
