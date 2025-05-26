from fastapi import APIRouter, HTTPException, Path, Query
from matplotlib.tri import TriAnalyzer
from pydantic import BaseModel
from typing import List, Dict, Optional, Any
from datetime import datetime
import logging

# Setup logging
logger = logging.getLogger(__name__)

# Initialize router
router = APIRouter()

# Model Schemas
class Driver(BaseModel):
    id: str
    code: str
    name: str
    team: str
    teamColor: str
    probability: float
    predictedPosition: int

class Circuit(BaseModel):
    id: str
    name: str
    location: str
    country: str
    imageUrl: Optional[str] = None
  
class FeatureImportance(BaseModel):
    name: str
    importance: float
    direction: str # "positive" or "negative"
  
class RacePrediction(BaseModel):
    circuit: Circuit
    date: str
    predictions: List[Driver]
    confidence: str # "high", "medium", "low"
    topFactors: List[FeatureImportance]
    lastUpdated: str

class PredictionRequest(BaseModel):
    circuitId: str
    weather: Optional[str] = "dry"
    temperature: Optional[float] = None
    includeFeatureImportance: Optional[bool] = False

@router.get("/predictions/upcoming")
async def get_prediction():
    """
    Get predictions for upcoming races in the season
    """

    try:
        # Mock data for now
        mock_prediction = RacePrediction(
            circuit=Circuit(
                id="miami",
                name="Miami Grand Prix",
                location="Miami",
                country="United States",
                imageUrl="https://media.formula1.com/image/upload/f_auto,c_limit,w_1440,q_auto/f_auto/q_auto/content/dam/fom-website/2018-redesign-assets/Racehub%20header%20images%2016x9/Miami"
            ),
            date="2025-05-05T00:00:00Z",
            predictions=[
                Driver(
                    id="verstappen",
                    code="VER",
                    name="Max Verstappen",
                    team="Red Bull Racing",
                    teamColor="#0600EF",
                    probability=0.432,
                    predictedPosition=1
                ),
                Driver(
                    id="perez",
                    code="PER",
                    name="Sergio Perez",
                    team="Red Bull Racing",
                    teamColor="#0600EF",
                    probability=0.218,
                    predictedPosition=2
                ),
                Driver(
                    id="norris",
                    code="NOR",
                    name="Lando Norris",
                    team="McLaren",
                    teamColor="#FF8700",
                    probability=0.184,
                    predictedPosition=3
                ),
            ],
            confidence="high",
            topFactors=[
                FeatureImportance(name="Qualifying Performance", importance=85, direction="positive"),
                FeatureImportance(name="Historical Performance", importance=72, direction="positive"),
                FeatureImportance(name="Car Performance", importance=68, direction="positive"),
                FeatureImportance(name="Weather Adaptation", importance=45, direction="negative"),
            ],
            lastUpdated="2025-05-02T12:00:00Z"
        )

        return [mock_prediction]
    except Exception as e:
        logger.error(f"Error generating upcoming predictions: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error getting predictions: {str(e)}")
    
@router.post("/predictions/race", response_model=RacePrediction)
async def predict_race(request: PredictionRequest):
    """
    Generate a prediction for a specific race with optional parameters.
    """
    try:
        # Mock response for now
        prediction = RacePrediction(
            circuit=Circuit(
                id=request.circuitId,
                name=f"{request.circuitId.capitalize()} Grand Prix",
                location=request.circuitId.capitalize(),
                country="United States" if request.circuitId == "miami" else "Unknown",
                imageUrl="https://via.placeholder.com/800x300"
            ),
            date="2025-05-05T00:00:00Z",
            predictions=[
                Driver(
                    id="verstappen",
                    code="VER",
                    name="Max Verstappen",
                    team="Red Bull Racing",
                    teamColor="#0600EF",
                    probability=0.432,
                    predictedPosition=1
                ),
                Driver(
                    id="perez",
                    code="PER",
                    name="Sergio Perez",
                    team="Red Bull Racing",
                    teamColor="#0600EF",
                    probability=0.218,
                    predictedPosition=2
                ),
                Driver(
                    id="norris",
                    code="NOR",
                    name="Lando Norris",
                    team="McLaren",
                    teamColor="#FF8700",
                    probability=0.184,
                    predictedPosition=3
                ),
            ],
            confidence="high" if request.weather == "dry" else "medium",
            topFactors=[
                FeatureImportance(name="Qualifying Performance", importance=85, direction="positive"),
                FeatureImportance(name="Historical Performance", importance=72, direction="positive"),
                FeatureImportance(name="Car Performance", importance=68, direction="positive"),
                FeatureImportance(name="Weather Adaptation", importance=45, direction="negative"),
            ],
            lastUpdated=datetime.now().isoformat()
        )
        
        return prediction
    except Exception as e:
        logger.error(f"Error predicting race: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error predicting race: {str(e)}")
   