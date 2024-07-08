from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from app.controllers.scraper import Scraper
from app.storage.sqlite_storage import SQLiteStorage
from app.utils.utils import notify
from app.utils.config import TOKEN
from app.storage.json_storage import JSONStorage

router = APIRouter()
security = HTTPBasic()

def get_current_token(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.password != TOKEN:
        raise HTTPException(status_code=403, detail="Invalid token")
    return credentials.password

@router.get("/")
def scrape_catalogue(pages: int = 1, proxy: str = None):# token: str = Depends(get_current_token)):
    scraper_instance = Scraper(pages, proxy)
    scraped_data = scraper_instance.scrape()
    storage = SQLiteStorage()
    updated_count = storage.save(scraped_data)
    notify(updated_count)
    return {"status": "success", "updated_count": updated_count}


