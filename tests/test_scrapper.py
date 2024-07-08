import unittest
from app.controllers.scraper import Scraper

class TestScraper(unittest.TestCase):
    def test_scrape(self):
        scraper = Scraper(pages=1)
        data = scraper.scrape()
        self.assertTrue(len(data) > 0)
        self.assertIn("product_title", data[0])
        self.assertIn("product_price", data[0])
        self.assertIn("path_to_image", data[0])

if __name__ == '__main__':
    unittest.main()
