from fastapi import APIRouter

router = APIRouter()

@router.get("/compare")
def get_comparison():
    return {"message": "Comparison endpoint"}