import os
import unittest
from app.storage.sqlite_storage import SQLiteStorage
from app.storage.json_storage import JSONStorage

class TestSQLiteStorage(unittest.TestCase):
    def test_save_and_load(self):
        storage = SQLiteStorage()
        data = [{
            "product_title": "Test Product",
            "product_price": 99.99,
            "path_to_image": "images/test.jpg"
        }]
        storage.save(data)
        loaded_data = storage.load()
        self.assertTrue(any(product.product_title == "Test Product" for product in loaded_data))


class TestJSONStorage(unittest.TestCase):
    def test_save_and_load(self):
        storage = JSONStorage(file_path="test_data.json")
        data = [{
            "product_title": "Test Product",
            "product_price": 99.99,
            "path_to_image": "images/test.jpg"
        }]
        storage.save(data)
        loaded_data = storage.load()
        # self.assertIn("Test Product", loaded_data)
        os.remove("test_data.json")

if __name__ == '__main__':
    unittest.main()
