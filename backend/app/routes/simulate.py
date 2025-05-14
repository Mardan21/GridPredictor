from fastapi import APIRouter

router = APIRouter()

@router.get("/simulate")
def get_simulation():
    return {"message": "Simulation endpoint"}