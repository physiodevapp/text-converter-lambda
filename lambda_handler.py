from fastapi import FastAPI
from pydantic import BaseModel
from mangum import Mangum
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.post("/convert")
async def convert_text(request: TextRequest):
    logger.info(f"Received request: {request}")
    converted_text = request.text.upper()
    logger.info(f"Converted text: {converted_text}")
    return {"converted_value": converted_text}

if os.getenv("AWS_EXECUTION_ENV"):
    handler = Mangum(app)

if __name__ == "__main__":
    import uvicorn
    logger.info("Running locally with Uvicorn...")
    uvicorn.run(app, host="0.0.0.0", port=8080)
