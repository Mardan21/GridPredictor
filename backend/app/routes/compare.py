from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Optional, Any
import logging

# Setup logging
logger = logging.getLogger(__name__)

# Initialize router
router = APIRouter()

# Model schemas
class ComparisonItem(BaseModel):
    id: str
    type: str  # "driver", "team", "season", "circuit"
    year: Optional[int] = None
    name: str
    color: Optional[str] = None

class ComparisonRequest(BaseModel):
    items: List[ComparisonItem]
    metrics: List[str]
    normalize: bool = False

class DataPoint(BaseModel):
    x: Any  # Can be string, number, or date
    y: float
    itemId: str
    
class ComparisonSeries(BaseModel):
    id: str
    metric: str
    name: str
    data: List[DataPoint]
    color: Optional[str] = None

class ComparisonResult(BaseModel):
    series: List[ComparisonSeries]
    summary: Dict[str, Any]
    metadata: Dict[str, Any]

@router.post("/compare", response_model=ComparisonResult)
async def compare_items(request: ComparisonRequest):
    """
    Compare drivers, teams, seasons, or circuits using selected metrics.
    """
    try:
        # Validate the request
        if not request.items or len(request.items) < 1:
            raise HTTPException(status_code=400, detail="At least one item is required for comparison")
            
        if not request.metrics or len(request.metrics) < 1:
            raise HTTPException(status_code=400, detail="At least one metric is required for comparison")
        
        # Generate mock comparison data
        series = []
        summary = {}
        metadata = {
            "type": request.items[0].type,
            "metrics": request.metrics,
            "itemCount": len(request.items)
        }
        
        # Generate mock data based on comparison type
        if request.items[0].type == "driver":
            # Mock driver data
            for metric in request.metrics:
                for item in request.items:
                    # Sample data points
                    data_points = [
                        DataPoint(x=2020, y=5, itemId=item.id),
                        DataPoint(x=2021, y=7, itemId=item.id),
                        DataPoint(x=2022, y=9, itemId=item.id),
                        DataPoint(x=2023, y=12, itemId=item.id),
                        DataPoint(x=2024, y=8, itemId=item.id),
                    ]
                    
                    series.append(
                        ComparisonSeries(
                            id=f"{item.id}_{metric}",
                            metric=metric,
                            name=f"{item.name} - {metric.capitalize()}",
                            data=data_points,
                            color=item.color
                        )
                    )
            
            # Mock summary data
            summary = {
                "totalWins": {
                    "hamilton": 103,
                    "verstappen": 60,
                    "leclerc": 5
                }
            }
        
        # Return comparison result
        return ComparisonResult(
            series=series,
            summary=summary,
            metadata=metadata
        )
        
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Error in comparison: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error running comparison: {str(e)}")