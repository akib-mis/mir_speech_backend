from fastapi import APIRouter
from transcribe.router import transcribe_router

app_router = APIRouter(
    prefix="/app",
    responses={404: {"description": "Not found"}},
)

app_router.include_router(
    transcribe_router
)