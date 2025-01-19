from fastapi import APIRouter
from pydantic import BaseModel
from services.text_processing import process_text as process_word
from services.ml_model import classify_word

router = APIRouter()

class TextRequest(BaseModel):
    text: str

@router.post("/convert")
async def convert_text(request: TextRequest):
    converted_word = process_word(request.text)
    category = classify_word(request.text)
    return {
        "converted_word": converted_word,
        "category": category
    }
