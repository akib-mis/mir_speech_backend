from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from transcribe.utils import LangType
from typing import Union
from transcribe.service import TranscribeService
from transcribe.schemas import TranscribeRead

transcribe_router = APIRouter(
    prefix="/transcribe",
    tags=["summerize"],
    responses={404: {"description": "Not found"}},
)


@transcribe_router.post("", status_code=status.HTTP_200_OK)
async def transcribe(tr_read: TranscribeRead):
    transcribe_service = TranscribeService(sentence=tr_read.message, lang=tr_read.lang)
    try:
        output = transcribe_service.transcribe()
        return output
    except Exception as e:
        return JSONResponse(
                content={"Message": "Transcription error", "Error": f"{e}"}, status_code=status.HTTP_400_BAD_REQUEST
            )