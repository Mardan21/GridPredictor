# GridPredictor
F1 analytics platform with real-time and historical race prediction capabilities.

## 🏎️ Overview

GridPredictor leverages machine learning and historical F1 data to provide accurate race predictions, season simulations, and comparative analysis. The platform combines real-time telemetry from FastF1 with historical data from Ergast API to deliver insights through interactive dashboards.

### ✨ Key Features

- **Race Prediction Engine**: XGBoost-powered predictions for upcoming races with probability distributions
- **Monte Carlo Simulation**: 10,000 simulated seasons to forecast championship outcomes
- **Interactive Dashboards**: Real-time stats, historical comparisons, and performance visualizations
- **Historical Comparison Tools**: Compare drivers, teams, and eras across Formula 1 history

## 🛠️ Tech Stack

- **Frontend**: Next.js 14 (App Router), React, Tailwind CSS
- **Data Visualization**: Recharts + D3.js
- **Backend**: Python with FastAPI
- **Machine Learning**: XGBoost for predictions, SHAP for feature attribution
- **Database**: Supabase (PostgreSQL)
- **External APIs**: FastF1 (live telemetry), Ergast API (historical data)
- **Hosting**: Vercel (frontend + API), AWS Lambda (optional for ML workloads)

## 📋 Prerequisites

- Node.js 18+ and npm
- Python 3.9+
- Supabase account and project
- FastF1 API access
- Ergast API access (no key required)
- Vercel account (for deployment)

## 🚀 Getting Started

### Environment Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/racecast-pro.git
   cd racecast-pro
   ```

2. Set up frontend environment:
   ```bash
   cd frontend
   npm install
   cp .env.example .env.local
   # Fill in the required API keys and endpoints in .env.local
   ```

3. Set up backend environment:
   ```bash
   cd ../backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   cp .env.example .env
   # Fill in the required API keys and endpoints in .env
   ```

4. Initialize Supabase:
   ```bash
   cd ../infrastructure
   # Execute the schema SQL against your Supabase instance
   # Either through the Supabase UI or using their CLI
   ```

### Running Locally

1. Start the backend:
   ```bash
   cd backend
   uvicorn app.main:app --reload
   ```

2. Start the frontend:
   ```bash
   cd frontend
   npm run dev
   ```

3. Access the application:
   - Frontend: http://localhost:3000
   - API docs: http://localhost:8000/docs

## 🗂️ Project Structure

```
/frontend                  # Next.js frontend application
  /app                     # App Router pages and layouts
    /dashboard             # Dashboard pages
    /predict               # Prediction tools
    /compare               # Historical comparison tools
  /components              # Reusable React components
  /lib                     # Utility functions and API clients
  
/backend                   # Python FastAPI application
  /app                     # API endpoints and routing
  /ml                      # Machine learning models and utilities
  
/infrastructure            # Deployment and database configuration
  aws_lambda_config.json   # AWS Lambda configuration
  supabase_schema.sql      # Supabase schema definitions
```

## 🧪 Testing

### Frontend
```bash
cd frontend
npm test         # Run Jest tests
npm run e2e      # Run Playwright E2E tests
```

### Backend
```bash
cd backend
pytest           # Run all Python tests
pytest -xvs app/ml/tests/test_prediction.py  # Run specific tests
```

## 📊 Data Sources

- **FastF1**: Telemetry data from current and recent Formula 1 races
- **Ergast API**: Historical race data, results, and statistics (1950-present)
- **Supabase**: Cached results and pre-computed predictions

## 🚢 Deployment

### Frontend Deployment (Vercel)
```bash
cd frontend
vercel
```

### Backend Deployment
1. Deploy the FastAPI service to Vercel:
   ```bash
   cd backend
   vercel
   ```

2. (Optional) Deploy CPU-intensive ML functions to AWS Lambda:
   ```bash
   cd backend/ml
   # Follow AWS Lambda deployment instructions in the infrastructure directory
   ```

## 📄 License

MIT License - See LICENSE file for details.
