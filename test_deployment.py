import requests
import unittest

class TestPortfolioDeployment(unittest.TestCase):
    BASE_URL = "http://localhost:8000"
    
    def test_index_page(self):
        response = requests.get(f"{self.BASE_URL}/index.html")
        self.assertEqual(response.status_code, 200, "index.html should be accessible")

    def test_hero_image(self):
        response = requests.get(f"{self.BASE_URL}/ansh_pic.jpeg")
        self.assertEqual(response.status_code, 200, "Hero image should be accessible")

if __name__ == "__main__":
    print("Ensure the local server is running at http://localhost:8000 before running this test.")
    unittest.main()
