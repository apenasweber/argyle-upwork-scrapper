from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import json

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

class UpworkScraper:

    _url = "https://www.upwork.com/ab/account-security/login"

    def __init__(
        self,
        username=os.getenv("USERNAME"),
        secret_word=os.getenv("SECRET_WORD"),
        password=os.getenv("PASSWORD"),
    ):
        self.username = username
        self.secret_word = secret_word
        self.password = password

    def do_login(self):
        """
        Function to login in Upwork with the given credentials
        """
        # Insert username and submit
        driver.get(self._url)
        username_input = '//*[@id="login_username"]'
        username_submit = '//*[@id="login_password_continue"]'
        driver.find_element(By.XPATH, username_input).send_keys(self.username)
        driver.find_element(By.XPATH, username_submit).click()

        # Insert password and submit
        password_input = '//*[@id="login_password"]'
        password_submit = '//*[@id="login_control_continue"]'
        driver.find_element(By.XPATH, password_input).send_keys(self.password)
        driver.find_element(By.XPATH, password_submit).click()

        # Insert secret word and submit
        secret_input = '//*[@id="login_answer"]'
        secret_submit = '//*[@id="login_control_continue"]'
        driver.find_element(By.XPATH, secret_input).send_keys(self.secret_word)
        driver.find_element(By.XPATH, secret_submit).click()

        # check if the login was successful
        if driver.current_url == "https://www.upwork.com/nx/find-work/best-matches":
            print("Login successful")

    def get_data(self):
        """
        Function to get the data from the user profile
        """
        driver.get("https://www.upwork.com/freelancers/settings/contactInfo")
        user_id = driver.find_element(By.XPATH, 
            '//*[@id="main"]/div[2]/div[2]/div/main/div[1]/section/div[1]/div[2]'
        ).text
        name = driver.find_element(By.XPATH, 
            '//*[@id="main"]/div[2]/div[2]/div/main/div[1]/section/div[2]/div[2]'
        ).text
        timezone = driver.find_element(By.XPATH, 
            '//*[@id="main"]/div[2]/div[2]/div/main/div[3]/section/div[1]/div[2]'
        ).text
        address = driver.find_element(By.XPATH, 
            '//*[@id="main"]/div[2]/div[2]/div/main/div[3]/section/div[2]/div[2]'
        ).text
        phone = driver.find_element(By.XPATH, 
            '//*[@id="main"]/div[2]/div[2]/div/main/div[3]/section/div[3]/div[2]'
        ).text

        data_dict = {
            "user-id": user_id,
            "name": name,
            "timezone": timezone,
            "address": address,
            "phone": phone,
        }

        with open("upwork_data.txt", "w") as f:
            json.dump(data_dict, f)
        print("Data saved in upwork_data.txt")


if __name__ == "__main__":
    # Do stuff with your driver
    scraper = UpworkScraper()
    scraper.do_login()
    scraper.get_data()
    driver.close()
