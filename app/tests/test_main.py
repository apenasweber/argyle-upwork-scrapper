from black import main
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from main import UpworkScraper
import requests
from decouple import config

chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_prefs = {}
chrome_options.experimental_options["prefs"] = chrome_prefs
chrome_prefs["profile.default_content_settings"] = {"images": 2}


driver = webdriver.Chrome(options=chrome_options)


class TestMain:
    def test_target_url():
        response = driver.get(config("PORTAL_LINK"))
        assert response.status_code == 200

    def test_do_login_(self):
        UpworkScraper.do_login()
        assert driver.current_url == "https://www.upwork.com/nx/find-work/best-matches"

    def test_get_data(self):
        pass
