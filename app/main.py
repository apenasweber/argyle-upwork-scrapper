from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-extensions")
chrome_options.headless = True

chromedriver = "chromedriver.exe"
driver = webdriver.Chrome(chromedriver)

class UpworkScraper:
    
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


    def get_data(self):
        """
        Function to get the data from the user profile
        """
        driver.get("https://www.upwork.com/freelancers/settings/contactInfo")
        user_id = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[2]/div/main/div[1]/section/div[1]/div[2]').text
        name = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[2]/div/main/div[1]/section/div[2]/div[2]').text
        timezone = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[2]/div/main/div[3]/section/div[1]/div[2]').text
        address = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[2]/div/main/div[3]/section/div[2]/div[2]').text
        phone = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[2]/div/main/div[3]/section/div[3]/div[2]').text
        print("User ID: " + user_id)
        print("Name: " + name)
        print("Timezone: " + timezone)
        print("Address: " + address)
        print("Phone: " + phone)