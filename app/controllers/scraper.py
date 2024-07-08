from typing import List, Dict
import requests
from bs4 import BeautifulSoup
import time
from ..utils.utils import download_image

class Scraper:
    def __init__(self, pages: int, proxy: str = None):
        self.base_url = "https://dentalstall.com/shop/"
        self.pages = pages
        self.proxy = proxy
        self.retry_attempts = 3
        self.retry_delay = 5  # seconds

    def fetch_page(self, url: str) -> requests.Response:
        for attempt in range(self.retry_attempts):
            try:
                response = requests.get(url, proxies={"http": self.proxy, "https": self.proxy})
                response.raise_for_status()
                return response
            except requests.RequestException as e:
                print(f"Error fetching {url}: {e}")
                if attempt < self.retry_attempts - 1:
                    time.sleep(self.retry_delay)
                else:
                    raise

    def scrape(self) -> List[Dict]:
        scraped_data = []
        for page in range(1, self.pages + 1):
            url = f"{self.base_url}page/{page}/"
            response = self.fetch_page(url)
            soup = BeautifulSoup(response.content, "html.parser")
            products = soup.find_all("li", class_="product")
            for product in products:
                title_element = product.find("h2", class_="woo-loop-product__title")
                title = title_element.text.strip() if title_element else "N/A"
                
                price_element = product.find("span", class_="woocommerce-Price-amount amount")
                price_text = price_element.text.strip() if price_element else "0"
                price = float(price_text.replace("₹", "").replace(",", ""))
                
                image_element = product.find("img", class_="attachment-woocommerce_thumbnail")
                image_url = ""
                if image_element:
                    image_url = image_element.get("src")
                    if "data:image" in image_url:
                        image_url = (
                            image_element.get("data-src") or
                            image_element.get("data-lazy-src") or
                            image_element.get("data-original") or
                            ""
                        )
                image_path = download_image(image_url) if image_url else ""

                scraped_data.append({
                    "product_title": title,
                    "product_price": price,
                    "path_to_image": image_path
                })
        return scraped_data
