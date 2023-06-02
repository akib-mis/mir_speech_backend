from typing import Optional, Union

from pydantic import UUID4, BaseModel
from transcribe.utils import LangType

class TranscribeRead(BaseModel):
    message: str
    lang: Union[LangType, None] = LangType.en