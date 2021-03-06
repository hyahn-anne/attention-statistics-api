import uvicorn
import logging
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from router.routers import router
from common.metadata import metadata


"""
# Set Debug Logger
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
"""


app = FastAPI(title=metadata.title,
        description=metadata.description,
        version=metadata.version,
        contact=metadata.contact,
        openapi_tags=metadata.tags)
app.include_router(router)


@app.get('/')
async def root():
    return RedirectResponse(url='/docs')


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=9000)
