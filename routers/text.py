from fastapi import APIRouter
from pydantic import BaseModel
from services.text_processing import process_text

router = APIRouter()

class TextRequest(BaseModel):
    text: str

@router.post("/convert")
async def convert_text(request: TextRequest):
    converted_text = process_text(request.text)
    return {"converted_text": converted_text}
