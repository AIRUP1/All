# DFW Hail Pipeline - Full Stack Application

A complete full-stack application for identifying hail-damaged properties in the DFW area.

## Architecture

- **Backend**: FastAPI (Python) - RESTful API
- **Frontend**: React with Material-UI - Modern web interface
- **Core Logic**: dfw_pipeline Python package

## Project Structure

```
dfw_hail_pipeline/
├── backend/
│   ├── api.py              # FastAPI backend
│   └── requirements.txt    # Python dependencies
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.js          # Main React component
│   │   ├── App.css
│   │   ├── index.js
│   │   └── index.css
│   └── package.json        # Node.js dependencies
├── dfw_pipeline/           # Core pipeline package
└── README_FULLSTACK.md     # This file
```

## Installation

### Backend Setup

1. Navigate to backend directory:
```bash
cd backend
```

2. Create virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install dfw_pipeline dependencies (from root):
```bash
cd ..
pip install pandas requests pyyaml
```

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

## Running the Application

### Start Backend

From the `backend` directory:

```bash
python api.py
```

Or using uvicorn directly:

```bash
uvicorn api:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at: `http://localhost:8000`

API documentation: `http://localhost:8000/docs`

### Start Frontend

From the `frontend` directory:

```bash
npm start
```

The frontend will be available at: `http://localhost:3000`

## API Endpoints

### GET `/`
Root endpoint with API information

### GET `/api/stats`
Get statistics about properties and hail events

### POST `/api/match`
Run property matching with hail events
- Body: Configuration (min_hail_size_in, base_radius_mi, etc.)
- Returns: Match results and statistics

### GET `/api/properties`
Get properties with pagination
- Query params: `limit`, `offset`, `damaged_only`

### GET `/api/results/{filename}`
Download results CSV file

### GET `/api/health`
Health check endpoint

## Features

### Backend
- RESTful API with FastAPI
- Automatic API documentation (Swagger UI)
- CORS enabled for frontend integration
- Background task support
- File upload/download capabilities

### Frontend
- Modern React UI with Material-UI
- Real-time statistics dashboard
- Configurable matching parameters
- Property listing table
- CSV download functionality
- Responsive design

## Configuration

### Backend Configuration

Edit `backend/api.py` to modify:
- Upload/output directories
- CORS origins
- Default matching parameters

### Frontend Configuration

Edit `frontend/src/App.js` to modify:
- API base URL (set `REACT_APP_API_URL` environment variable)
- Default configuration values
- UI components

## Development

### Backend Development

```bash
cd backend
uvicorn api:app --reload
```

### Frontend Development

```bash
cd frontend
npm start
```

## Production Deployment

### Backend

1. Install production dependencies
2. Use a production ASGI server (e.g., Gunicorn with Uvicorn workers)
3. Set up reverse proxy (nginx)
4. Configure environment variables

### Frontend

1. Build the React app:
```bash
cd frontend
npm run build
```

2. Serve the `build` directory with a web server (nginx, Apache, etc.)

## Dependencies

### Backend
- fastapi>=0.104.0
- uvicorn[standard]>=0.24.0
- pandas>=2.0.0
- pydantic>=2.0.0
- python-multipart>=0.0.6

### Frontend
- react>=18.2.0
- react-dom>=18.2.0
- axios>=1.6.0
- @mui/material>=5.14.0
- @mui/icons-material>=5.14.0

## Troubleshooting

### Backend Issues

1. **Module not found**: Ensure dfw_pipeline is in Python path
2. **Port already in use**: Change port in `api.py` or kill existing process
3. **CORS errors**: Check CORS configuration in `api.py`

### Frontend Issues

1. **API connection failed**: Check `REACT_APP_API_URL` environment variable
2. **Build errors**: Clear `node_modules` and reinstall
3. **Port conflicts**: Change port in `package.json` scripts

## License

Part of the StormBuster project.

