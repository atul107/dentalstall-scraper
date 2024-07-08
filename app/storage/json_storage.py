import json
import os
from typing import List, Dict
import redis
from .base import Storage

class JSONStorage(Storage):
    def __init__(self, file_path="scraped_data.json"):
        self.file_path = file_path
        self.redis_client = redis.Redis(host='localhost', port=6379, db=0)

    def save(self, data: List[Dict]) -> int:
        updated_count = 0
        existing_data = self.load()
        for item in data:
            cache_key = item["product_title"]
            cached_price = self.redis_client.get(cache_key)
            if not cached_price or float(cached_price) != item["product_price"]:
                existing_data[cache_key] = item
                self.redis_client.set(cache_key, item["product_price"])
                updated_count += 1
        with open(self.file_path, "w") as f:
            json.dump(list(existing_data.values()), f, indent=4)
        return updated_count

    def load(self) -> Dict[str, Dict]:
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as f:
                data = json.load(f)
                return {item["product_title"]: item for item in data}
        return {}
