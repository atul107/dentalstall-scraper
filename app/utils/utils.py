import requests
import os

def download_image(url: str) -> str:
    response = requests.get(url)
    image_name = os.path.basename(url)
    image_path = os.path.join("images", image_name)
    os.makedirs(os.path.dirname(image_path), exist_ok=True)
    with open(image_path, "wb") as f:
        f.write(response.content)
    return image_path

def notify(updated_count: int):
    print(f"Scraped and updated {updated_count} products in the database.")
