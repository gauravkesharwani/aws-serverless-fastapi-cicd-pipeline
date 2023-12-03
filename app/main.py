from fastapi import FastAPI
from mangum import Mangum
import time
from fastapi.responses import StreamingResponse

from api.v1.api import router as api_router

app = FastAPI(title='Serverless Lambda FastAPI')

app.include_router(api_router, prefix="/api/v1")


@app.get("/",  tags=["Endpoint Test"])
def main_endpoint_test():
    return {"message": "Welcome CI/CD Pipeline with GitHub Actions!"}

async def fake_streamer():
    for i in range(10):
        yield "some fake video bytes"
        time.sleep(.5)


@app.get("/stream")
async def main():
    return StreamingResponse(fake_streamer())




# to make it work with Amazon Lambda, we create a handler object
handler = Mangum(app=app)

