@echo off
echo 🌩️ STORMBUSTER DEPLOYMENT TO STORMGODS.US
echo ============================================================

if not exist "stormgods_deployment" (
    echo ❌ Deployment package not found. Run 'python deploy_stormgods.py' first.
    pause
    exit /b 1
)

echo ✅ Deployment package found: stormgods_deployment/
echo.
echo 🚀 DEPLOYMENT OPTIONS:
echo 1. Vercel (Recommended)
echo 2. Netlify (Easiest)
echo 3. Railway
echo 4. Manual Upload
echo.
set /p choice="Select option (1-4): "

if "%choice%"=="1" (
    echo.
    echo 🚀 Vercel Deployment:
    echo 1. Install Node.js and npm if not installed
    echo 2. Run: npm install -g vercel
    echo 3. Navigate to: stormgods_deployment folder
    echo 4. Run: vercel login
    echo 5. Run: vercel
    echo 6. Add domain: vercel domains add stormgods.us
) else if "%choice%"=="2" (
    echo.
    echo 🌐 Netlify Deployment:
    echo 1. Go to: https://app.netlify.com/drop
    echo 2. Drag stormgods_deployment folder to the page
    echo 3. Get your URL
    echo 4. Add custom domain: stormgods.us
) else if "%choice%"=="3" (
    echo.
    echo 🚂 Railway Deployment:
    echo 1. Go to: https://railway.app
    echo 2. Create new project
    echo 3. Upload stormgods_deployment folder
    echo 4. Configure domain: stormgods.us
) else if "%choice%"=="4" (
    echo.
    echo 📤 Manual Upload:
    echo 1. Upload all files from stormgods_deployment to your hosting
    echo 2. Set up Python environment
    echo 3. Configure environment variables
    echo 4. Point stormgods.us to your hosting
) else (
    echo ❌ Invalid choice
)

echo.
echo 📁 Deployment folder:
cd
echo %CD%\stormgods_deployment

echo.
echo 📋 Environment Variables to Set:
echo SPOKEO_EMAIL=bolison10@gmail.com
echo SPOKEO_PASSWORD=your_password
echo STRIPE_PUBLIC_KEY=your_stripe_key
echo OPENAI_API_KEY=your_openai_key

echo.
echo 🎉 Ready to deploy StormBuster to stormgods.us!
pause
