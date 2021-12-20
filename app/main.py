import uvicorn
import logging
from typing import Optional
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from database.db import engine
from router.routers import router
from common.metadata import metadata


logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

app = FastAPI(title=metadata.title,
        description=metadata.description,
        version=metadata.version,
        contact=metadata.contact,
        openapi_tags=metadata.tags)
app.include_router(router)


@app.get("/")
async def root():
    return RedirectResponse(url='/docs')


if __name__ == '__main__':
    uvicorn.run("main:app", port=9000, log_level="debug", reload=True)
