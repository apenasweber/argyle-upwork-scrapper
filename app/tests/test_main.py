import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from main import UpworkScraper
chrome_options = Options()
chrome_options.headless = True
chromedriver = "chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
import requests
class TestMain(unittest.TestCase):

    def test_target_url():
        response = requests.get("https://www.upwork.com/ab/account-security/login")
        assert response.status_code == 200

    def test_do_login_(self):
        assert driver.current_url == "https://www.upwork.com/nx/find-work/best-matches"

    def test_get_data(self):
        pass

    

    