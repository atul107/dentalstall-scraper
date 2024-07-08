from fastapi import FastAPI
from app.routes.scrape import router as scrape_router

app = FastAPI()

app.include_router(scrape_router, prefix="/scrape")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

