import requests
import beautifulsoup
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-extensions")
chrome_options.headless = True
chromedriver = "/Users/Downloads/chromedriver"
driver = webdriver.Chrome(chromedriver)


"""
LOGIN
Portal link: https://www.upwork.com/ab/account-security/login
>>> WAIT LOADING
Username: bobsuperworker (//*[@id="login_username"])
submit1: //*[@id="login_password_continue"]
>>> WAIT LOADING
Password: Argyleawesome123! (//*[@id="login_password"])
submit2: //*[@id="login_control_continue"]
>>> WAIT LOADING
Secret answer: number42 (//*[@id="login_answer"])
submit3: //*[@id="login_control_continue"]
>>> WAIT LOADING
"""
# https://limeproxies.netlify.app/blog/selenium-vs-beautifulsoup

class LoginUpwork:
    
    _url = "https://www.upwork.com/ab/account-security/login"
    
    def __init__(self , username, secret_word, password):
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
        driver.find_element_by_xpath(username_input).send_keys(self.username)
        driver.find_element_by_xpath(username_submit).click()
        # Insert password and submit
        password_input = '//*[@id="login_password"]'
        password_submit = '//*[@id="login_control_continue"]'
        driver.find_element_by_xpath(password_input).send_keys(self.password)
        driver.find_element_by_xpath(password_submit).click()
        # Insert secret word and submit
        secret_input = '//*[@id="login_answer"]'
        secret_submit = '//*[@id="login_control_continue"]'
        driver.find_element_by_xpath(secret_input).send_keys(self.secret_word)
        driver.find_element_by_xpath(secret_submit).click()
        # check if the login was successful
        if driver.current_url == "https://www.upwork.com/nx/find-work/best-matches":
            print("Login successful")

    """
    TAKE DATA
    access: https://www.upwork.com/freelancers/settings/contactInfo
    user_id: //*[@id="main"]/div[2]/div[2]/div/main/div[1]/section/div[1]/div[2]
    name: //*[@id="main"]/div[2]/div[2]/div/main/div[1]/section/div[2]/div[2]
    timezone: //*[@id="main"]/div[2]/div[2]/div/main/div[3]/section/div[1]/div[2]
    address: //*[@id="main"]/div[2]/div[2]/div/main/div[3]/section/div[2]/div[2]
    Phone: //*[@id="main"]/div[2]/div[2]/div/main/div[3]/section/div[3]/div[2]
    """