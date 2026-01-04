from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, StaleElementReferenceException
import os
from dotenv import load_dotenv
from time import sleep
import random

load_dotenv()

SIMILIAR_ACCOUNT = "openai"
USERNAME = os.getenv("DAY52_INSTAGRAM_USERNAME")
PASSWORD = os.getenv("DAY52_INSTAGRAM_PASSWORD")
INSTAGRAM_URL = f"https://www.instagram.com/{SIMILIAR_ACCOUNT}/"

chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument(
    r"--user-data-dir=C:\Users\Kerem\AppData\Local\Google\Chrome\User Data"
)
chrome_options.add_argument("--profile-directory=Profile 5")

class InstaFollower():
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)
        self.followed_account_count = 0

    def login(self):
        self.driver.get(INSTAGRAM_URL)
        try:
            login_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, '//div[text()="Giriş yap"]'))
            )
            login_button.click()
            print("Clicked to enter button.")

        except Exception as e:
            print("Error while clicking enter button:", e)

        try:
            email_input = self.wait.until(
                EC.presence_of_element_located((By.NAME, "email"))
            )
        except Exception:
            try:
                email_input = self.wait.until(
                    EC.presence_of_element_located((By.NAME, "username"))
                )
            except Exception as e:
                print("Neither email nor username input found:", e)
            else:
                email_input.clear()
                email_input.send_keys(USERNAME)
                print("Email writed to 'username' area.")
        else:
            email_input.clear()
            email_input.send_keys(USERNAME)
            print("Email writed to 'email' area.")

        try:
            password_input = self.wait.until(
                EC.presence_of_element_located((By.NAME, "pass"))
            )
        except Exception:
            try:
                password_input = self.wait.until(
                    EC.presence_of_element_located((By.NAME, "password"))
                )
            except Exception as e:
                print("Neither 'pass' nor 'password' input found:", e)
            else:
                password_input.clear()
                password_input.send_keys(PASSWORD)
                print("Password writed to 'password' area.")
        else:
            password_input.clear()
            password_input.send_keys(PASSWORD)
            print("Password writed to 'pass' area.")

        try:
            login_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, '//span[text()="Giriş Yap"]'))
            )
        except Exception:
            try:
                login_button = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, '//div[text()="Giriş yap"]'))
                )
            except Exception as e:
                print("Login button not found:", e)
            else:
                self.driver.execute_script("arguments[0].scrollIntoView();", login_button)
                login_button.click()
                print("Clicked login button (div).")
        else:
            self.driver.execute_script("arguments[0].scrollIntoView();", login_button)
            login_button.click()
            print("Clicked login button (span).")

        try:
            save_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, '//button[text()="Bilgileri kaydet"]'))
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", save_button)
            save_button.click()
            print("Clicked to save button.")

        except Exception as e:
            print("Error while clicking save button/save button doesn't exists:", e)

    sleep(5)

    def find_followers(self):
        try:
            search_button = self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//span[normalize-space()='Ara']/ancestor::a")
                )
            )

            ActionChains(self.driver)\
                .move_to_element(search_button)\
                .pause(0.25)\
                .click()\
                .perform()

            search_input = self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//input[@placeholder='Ara']")
                )
            )
            self.driver.execute_script("arguments[0].focus();", search_input)

            search_input.clear()
            search_input.send_keys(SIMILIAR_ACCOUNT)

            print("Clicked search button.")

            sleep(5)

        except Exception as e:
            print("Error while clicking search button:", e)

        try:
            result_link = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, f'//span[text()="{SIMILIAR_ACCOUNT}"]/ancestor::a'))
            )
        except Exception:
            try:
                result_link = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, f'//span[text()="{SIMILIAR_ACCOUNT}"]/ancestor::div'))
                )
            except Exception as e:
                print("Error while clicking result:", e)
            else:
                self.driver.execute_script("arguments[0].scrollIntoView();", result_link)
                result_link.click()
                print(f"{SIMILIAR_ACCOUNT} result (div) clicked.")
        else:
            self.driver.execute_script("arguments[0].scrollIntoView();", result_link)
            result_link.click()
            print(f"{SIMILIAR_ACCOUNT} result (a) clicked.")

        try:
                close_button = self.wait.until(
                    EC.visibility_of_element_located(
                        (By.XPATH, "//button[normalize-space()='Kapat']")
                    )
                )

                self.driver.execute_script(
                    "arguments[0].click();", close_button
                )

                print("Close button clicked via JS.")

        except StaleElementReferenceException:
            print("Close button became stale, retrying once...")
            try:
                close_button = self.wait.until(
                    EC.visibility_of_element_located(
                        (By.XPATH, "//button[normalize-space()='Kapat']")
                    )
                )
                self.driver.execute_script(
                    "arguments[0].click();", close_button
                )
            except Exception as e:
                print("Retry failed:", e)
                return False

        except TimeoutException:
            print("Close button not found.")
            return False

        except Exception as e:
            print("Error while clicking close button:", e)
            return False

        try:
            followers_link = self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, f"//a[contains(@href, '/{SIMILIAR_ACCOUNT}/followers')]")
                )
            )

            ActionChains(self.driver)\
                .move_to_element(followers_link)\
                .pause(0.25)\
                .click()\
                .perform()

            print("Follower list opened successfully.")

        except ElementClickInterceptedException:
            try:
                self.driver.execute_script(
                    "arguments[0].click();", followers_link
                )
                print("Follower list opened via JS click.")

            except Exception as e:
                print("JS click failed:", e)

        except TimeoutException:
            print("Follower link not found (Timeout).")

        except Exception as e:
            print("Error while clicking follower count:", e)
        
    def follow(self):
        buttons = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, '//div[text()="Takip Et"]'))
        )
        for button in buttons:
            try:
                sleep(random.uniform(0.5, 2.0))
                self.driver.execute_script("arguments[0].scrollIntoView();", button)
                button.click()
                self.followed_account_count += 1
                print(f"Account followed, total count: {self.followed_account_count}")

                if random.random() < 0.1:
                    sleep(random.uniform(2.5, 5))
            except Exception as e:
                print("Error:", e)

follower_bot = InstaFollower()
follower_bot.login()
follower_bot.find_followers()
follower_bot.follow()