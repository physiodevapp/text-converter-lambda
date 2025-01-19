from fastapi import FastAPI
from mangum import Mangum
from routers.text import router as text_router
from utils.logger import get_logger
import os

logger = get_logger(__name__)

app = FastAPI()

app.include_router(text_router)

if os.getenv("AWS_EXECUTION_ENV"):
    handler = Mangum(app)

if __name__ == "__main__":
    import uvicorn
    logger.info("Running locally with Uvicorn...")
    uvicorn.run(app, host="0.0.0.0", port=8080)
