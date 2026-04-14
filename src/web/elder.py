from fastapi import APIRouter
router=APIRouter()


@router.get("/")
def testing():
    return{
        "message": "lets get started!"
    }