from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv
from time import sleep

load_dotenv()

PROMISED_DOWN = 100
PROMISED_UP = 15
TWITTER_EMAIL = os.getenv("DAY51_TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("DAY51_TWITTER_PASSWORD")
GOOGLE_PASSWORD = os.getenv("DAY51_GOOGLE_PASSWORD")
CHROME_PROFILE_PATH = r"C:\Users\kerem\AppData\Local\Google\Chrome\User Data\Profile 3"
TWITTER_URL = "https://twitter.com/home"
SPEEDTEST_URL ="https://www.speedtest.net/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument(
    r"--user-data-dir=C:\Users\Kerem\AppData\Local\Google\Chrome\User Data"
)
chrome_options.add_argument("--profile-directory=Profile 3")

class InternetSpeedTwitterBot():
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)
        self.message = ""
        self.down = 0
        self.up = 0

    def get_internet_Speed(self):
        self.driver.get(SPEEDTEST_URL)
        go_button = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "start-text"))
        )
        go_button.click()

        sleep(45)

        download = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "download-speed"))
        )         
        self.down = download.text

        upload = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "upload-speed"))
        )
        self.up = upload.text

        print(f"Internet speed data taken.\nDownload: {self.down}Mbps, Upload: {self.up}Mbps")
        self.message = f"Hey Internet Provider, why is my internet speed {self.down}Down/{self.up}Up when I pay for {PROMISED_DOWN}Down/{PROMISED_UP}Up"

    def tweet_at_provider(self):
        self.driver.get(TWITTER_URL)
        post_form = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "public-DraftStyleDefault-block"))
        )
        post_form.send_keys(self.message)
        post_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Post']"))
        )
        post_button.click()

        self.driver.quit()    

#----------------------------------------------------------------------------------------------------

twitter_bot = InternetSpeedTwitterBot()
twitter_bot.get_internet_Speed()

if float(twitter_bot.down) < PROMISED_DOWN or float(twitter_bot.up) < PROMISED_UP:
    twitter_bot.tweet_at_provider() 
