from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Optional, Any
import logging

# Setup logging
logger = logging.getLogger(__name__)

# Initialize router
router = APIRouter()

# Model Schemas
class SimulationParams(BaseModel):
    iterations: int = 10000
    scenarioType: Optional[str] = "normal"  # "normal", "dnf", "win", "weather"
    scenarioDriverId: Optional[str] = None
    scenarioRace: Optional[str] = None
    scenarioOutcome: Optional[str] = None

class DriverResult(BaseModel):
    championshipWinPercent: float
    top3Percent: float
    averagePosition: float
    medianPosition: Optional[float] = None

class TeamResult(BaseModel):
    championshipWinPercent: float
    top3Percent: float
    averagePosition: float

class SimulationResult(BaseModel):
    driverChampionship: Dict[str, DriverResult]
    constructorsChampionship: Dict[str, TeamResult]
    remainingSchedule: List[str]

@router.post("/simulate", response_model=SimulationResult)
async def simulate_season(params: SimulationParams):
    """
    Run a Monte Carlo simulation of the remaining F1 season.
    """
    try:
        # Validate parameters
        if params.iterations < 100 or params.iterations > 50000:
            raise HTTPException(status_code=400, detail="Iterations must be between 100 and 50,000")
        
        # Mock simulation results
        driver_results = {
            "verstappen": DriverResult(
                championshipWinPercent=60.5,
                top3Percent=92.3,
                averagePosition=1.4,
                medianPosition=1
            ),
            "perez": DriverResult(
                championshipWinPercent=12.8,
                top3Percent=65.7,
                averagePosition=3.1,
                medianPosition=3
            ),
            "leclerc": DriverResult(
                championshipWinPercent=15.6,
                top3Percent=71.3,
                averagePosition=2.8,
                medianPosition=2
            ),
            "sainz": DriverResult(
                championshipWinPercent=7.2,
                top3Percent=52.9,
                averagePosition=4.2,
                medianPosition=4
            ),
        }
        
        team_results = {
            "Red Bull Racing": TeamResult(
                championshipWinPercent=72.3,
                top3Percent=97.8,
                averagePosition=1.3
            ),
            "Ferrari": TeamResult(
                championshipWinPercent=21.5,
                top3Percent=96.2,
                averagePosition=2.1
            ),
            "Mercedes": TeamResult(
                championshipWinPercent=4.9,
                top3Percent=88.7,
                averagePosition=2.9
            ),
        }
        
        # Return simulation results
        return SimulationResult(
            driverChampionship=driver_results,
            constructorsChampionship=team_results,
            remainingSchedule=["Miami", "Imola", "Monaco", "Canada", "Barcelona"]
        )
        
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Error in season simulation: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error running simulation: {str(e)}")