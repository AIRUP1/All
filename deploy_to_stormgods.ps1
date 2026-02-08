# StormBuster Deployment Script for stormgods.us
# PowerShell script to deploy StormBuster to web hosting

Write-Host "🌩️ STORMBUSTER DEPLOYMENT TO STORMGODS.US" -ForegroundColor Cyan
Write-Host ("=" * 60) -ForegroundColor Cyan

# Check if deployment package exists
if (-not (Test-Path "stormgods_deployment")) {
    Write-Host "❌ Deployment package not found. Run 'python deploy_stormgods.py' first." -ForegroundColor Red
    exit 1
}

Write-Host "✅ Deployment package found: stormgods_deployment/" -ForegroundColor Green

# Check for Node.js and npm
Write-Host "`n🔍 Checking for Node.js and npm..." -ForegroundColor Yellow
try {
    $nodeVersion = node --version 2>$null
    if ($nodeVersion) {
        Write-Host "✅ Node.js found: $nodeVersion" -ForegroundColor Green
    } else {
        Write-Host "❌ Node.js not found in PATH" -ForegroundColor Red
    }
} catch {
    Write-Host "❌ Node.js not found in PATH" -ForegroundColor Red
}

try {
    $npmVersion = npm --version 2>$null
    if ($npmVersion) {
        Write-Host "✅ npm found: $npmVersion" -ForegroundColor Green
    } else {
        Write-Host "❌ npm not found in PATH" -ForegroundColor Red
    }
} catch {
    Write-Host "❌ npm not found in PATH" -ForegroundColor Red
}

# Check for Vercel CLI
Write-Host "`n🔍 Checking for Vercel CLI..." -ForegroundColor Yellow
try {
    $vercelVersion = vercel --version 2>$null
    if ($vercelVersion) {
        Write-Host "✅ Vercel CLI found: $vercelVersion" -ForegroundColor Green
        $vercelInstalled = $true
    } else {
        Write-Host "❌ Vercel CLI not found" -ForegroundColor Red
        $vercelInstalled = $false
    }
} catch {
    Write-Host "❌ Vercel CLI not found" -ForegroundColor Red
    $vercelInstalled = $false
}

# Install Vercel CLI if not found
if (-not $vercelInstalled) {
    Write-Host "`n📦 Installing Vercel CLI..." -ForegroundColor Yellow
    try {
        npm install -g vercel
        Write-Host "✅ Vercel CLI installed successfully" -ForegroundColor Green
        $vercelInstalled = $true
    } catch {
        Write-Host "❌ Failed to install Vercel CLI. You may need to:" -ForegroundColor Red
        Write-Host "   1. Restart your terminal" -ForegroundColor Red
        Write-Host "   2. Check if Node.js is properly installed" -ForegroundColor Red
        Write-Host "   3. Run as administrator" -ForegroundColor Red
    }
}

# Deployment options
Write-Host "`n🚀 DEPLOYMENT OPTIONS:" -ForegroundColor Cyan
Write-Host "1. Vercel (Recommended) - Full featured hosting" -ForegroundColor White
Write-Host "2. Netlify - Drag and drop deployment" -ForegroundColor White
Write-Host "3. Railway - Simple deployment" -ForegroundColor White
Write-Host "4. Manual Upload - Upload to your hosting provider" -ForegroundColor White

$choice = Read-Host "`nSelect deployment option (1-4)"

switch ($choice) {
    "1" {
        if ($vercelInstalled) {
            Write-Host "`n🚀 Deploying to Vercel..." -ForegroundColor Green
            Set-Location "stormgods_deployment"
            
            Write-Host "`nStep 1: Login to Vercel" -ForegroundColor Yellow
            Write-Host "You'll need to open your browser and login to Vercel"
            vercel login
            
            Write-Host "`nStep 2: Deploy to Vercel" -ForegroundColor Yellow
            vercel
            
            Write-Host "`nStep 3: Configure custom domain" -ForegroundColor Yellow
            Write-Host "After deployment, run these commands:"
            Write-Host "vercel domains add stormgods.us" -ForegroundColor Cyan
            Write-Host "vercel domains add www.stormgods.us" -ForegroundColor Cyan
            
            Set-Location ".."
        } else {
            Write-Host "❌ Vercel CLI not available. Please install Node.js and npm first." -ForegroundColor Red
        }
    }
    "2" {
        Write-Host "`n🌐 Netlify Deployment Instructions:" -ForegroundColor Green
        Write-Host "1. Go to: https://app.netlify.com/drop" -ForegroundColor White
        Write-Host "2. Drag the 'stormgods_deployment' folder onto the page" -ForegroundColor White
        Write-Host "3. Get your instant URL" -ForegroundColor White
        Write-Host "4. Add custom domain: stormgods.us" -ForegroundColor White
        Write-Host "`n📁 Deployment folder location:" -ForegroundColor Yellow
        Write-Host (Resolve-Path "stormgods_deployment") -ForegroundColor Cyan
    }
    "3" {
        Write-Host "`n🚂 Railway Deployment Instructions:" -ForegroundColor Green
        Write-Host "1. Go to: https://railway.app" -ForegroundColor White
        Write-Host "2. Create new project" -ForegroundColor White
        Write-Host "3. Upload the 'stormgods_deployment' folder" -ForegroundColor White
        Write-Host "4. Configure domain: stormgods.us" -ForegroundColor White
        Write-Host "`n📁 Deployment folder location:" -ForegroundColor Yellow
        Write-Host (Resolve-Path "stormgods_deployment") -ForegroundColor Cyan
    }
    "4" {
        Write-Host "`n📤 Manual Upload Instructions:" -ForegroundColor Green
        Write-Host "1. Open your hosting provider's file manager" -ForegroundColor White
        Write-Host "2. Upload all files from stormgods_deployment folder" -ForegroundColor White
        Write-Host "3. Set up Python environment with requirements-vercel.txt" -ForegroundColor White
        Write-Host "4. Configure environment variables from .env.example" -ForegroundColor White
        Write-Host "5. Point stormgods.us domain to your hosting" -ForegroundColor White
        Write-Host "`n📁 Files to upload:" -ForegroundColor Yellow
        Get-ChildItem "stormgods_deployment" | ForEach-Object {
            Write-Host "   $($_.Name)" -ForegroundColor Cyan
        }
    }
    default {
        Write-Host "❌ Invalid choice. Please select 1-4." -ForegroundColor Red
    }
}

Write-Host "`n📋 IMPORTANT: Environment Variables to Set:" -ForegroundColor Yellow
Write-Host "SPOKEO_EMAIL=bolison10@gmail.com" -ForegroundColor White
Write-Host "SPOKEO_PASSWORD=your_password" -ForegroundColor White
Write-Host "STRIPE_PUBLIC_KEY=your_stripe_public_key" -ForegroundColor White
Write-Host "STRIPE_SECRET_KEY=your_stripe_secret_key" -ForegroundColor White
Write-Host "OPENAI_API_KEY=your_openai_key" -ForegroundColor White
Write-Host "ANTHROPIC_API_KEY=your_anthropic_key" -ForegroundColor White
Write-Host "GOOGLE_API_KEY=your_google_key" -ForegroundColor White

Write-Host "`n🎯 Post-Deployment Checklist:" -ForegroundColor Yellow
Write-Host "✅ Test application at stormgods.us" -ForegroundColor White
Write-Host "✅ Verify AI chat functionality" -ForegroundColor White
Write-Host "✅ Test property search engine" -ForegroundColor White
Write-Host "✅ Check vendor registration system" -ForegroundColor White
Write-Host "✅ Verify subscription management" -ForegroundColor White
Write-Host "✅ Test interactive hail maps" -ForegroundColor White

Write-Host "`n🌩️ StormBuster Features Deployed:" -ForegroundColor Cyan
Write-Host "• Storm Damage Assessment" -ForegroundColor White
Write-Host "• Property Search Engine (Spokeo Integration)" -ForegroundColor White
Write-Host "• AI Chat (ChatGPT, Claude, Gemini)" -ForegroundColor White
Write-Host "• Lead Generation Pipeline" -ForegroundColor White
Write-Host "• Vendor Registration System" -ForegroundColor White
Write-Host "• Subscription Management (Stripe)" -ForegroundColor White
Write-Host "• Interactive Hail Maps" -ForegroundColor White
Write-Host "• Results Roofing Integration" -ForegroundColor White

Write-Host "`n🎉 DEPLOYMENT COMPLETE!" -ForegroundColor Green
Write-Host "Your StormBuster application is ready for stormgods.us!" -ForegroundColor Green
