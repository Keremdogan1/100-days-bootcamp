from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import os
from dotenv import load_dotenv
from time import sleep

load_dotenv()

TINDER_URL = "https://tinder.onelink.me/9K8a/3d4abb81"
PHONE_NUMBER = os.getenv("DAY50_PHONE_NUMBER")
PASSWORD = os.getenv("DAY50_FACEBOOK_PASSWORD")
MAX_RETRIES = 5
MAX_CLICKS = 100
rejected_women_count = 0

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--disable-infobars")      
chrome_options.add_argument("--disable-popup-blocking")

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)
driver.get(TINDER_URL)

facebook_login = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="c-79007885"]/div/div[1]/div/div[2]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div[2]/div/div'))
)
facebook_login.click()

driver.switch_to.window(driver.window_handles[-1])
sleep(5)

for attempt in range(MAX_RETRIES):
    try:
        phone_number_form = wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="email"]'))
        )
        phone_number_form.send_keys(PHONE_NUMBER)

        password_form = wait.until(
            EC.visibility_of_element_located((By.ID, "pass"))
        )
        password_form.send_keys(PASSWORD)

        print(f"Attempt {attempt + 1} for Facebook registeration: Success!")
        break
    except Exception as e:
        print(f"Attempt {attempt + 1} for Facebook registeration: Failure, error code:", e)
        if attempt == MAX_RETRIES - 1:
            raise

popup_login_button = wait.until(
    EC.element_to_be_clickable((By.ID, "loginbutton"))
)
popup_login_button.click()

sleep(7.5)

facebook_continue_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Kerem Olarak Devam Et']"))
)                                         
facebook_continue_button.click()

driver.switch_to.window(driver.window_handles[0])
sleep(5)

for attempt in range(MAX_RETRIES):
    try:
        phone_input = wait.until(
            EC.element_to_be_clickable((By.ID, "phone_number"))
        )
        phone_input.send_keys(PHONE_NUMBER)
        print(f"Attempt {attempt + 1} for phone number enterance: Success!")
        break
    except Exception as e:
        print(f"Attempt {attempt + 1} for phone number enterance: Failure, error code:", e)

tinder_continue_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="c-79007885"]/div/div[1]/div[2]/div/div[3]/button/div[2]/div[2]/div'))
)
tinder_continue_button.click()

sms_code = input("Enter the SMS code: ")

sms_validate_form = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "input[aria-label='Tek seferlik pin kodu 1']"))
)
sms_validate_form.send_keys(sms_code)

final_verify_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="c-79007885"]/div/div[1]/div[2]/div[2]/div[4]/button/div[2]/div[2]/div'))
)
final_verify_button.click()

for attempt in range(MAX_RETRIES):
    try:
        location_accept = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[text()='İzin ver']"))
        )
        location_accept.click()
        print("Location permission accepted!")
        break
    except StaleElementReferenceException:
        print(f"Attempt {attempt+1}: Stale element error, trying again...")

for attempt in range(MAX_RETRIES):
    try:
        notifications_deny = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[text()='Fırsatlar kaçsın']"))
        )
        notifications_deny.click()
        print(f"Attempt {attempt+1}: Success! Notification permission rejected.")
        break
    except StaleElementReferenceException:
        print(f"Attempt {attempt+1}: Stale element error, trying again...")
        continue
    except Exception as e:
        print(f"Attempt {attempt+1}: Failure, error code:", e)
        if attempt == MAX_RETRIES - 1:
            raise

for attempt in range(MAX_RETRIES):
    try:
        reject_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[text()='Reddediyorum']"))
        )
        reject_button.click()
        print(f"Attempt {attempt+1}: Success! Cookies rejected.")
        break
    except StaleElementReferenceException:
        print(f"Attempt {attempt+1}: Stale element error, trying again...")
        continue
    except Exception as e:
        print(f"Attempt {attempt+1}: Failure, error code:", e)
        if attempt == MAX_RETRIES - 1:
            raise

for i in range(MAX_CLICKS):
    try:
        dont_add_to_main_page_button = driver.find_elements(By.XPATH, value="//div[text()='İlgilenmiyorum']")
        if len(dont_add_to_main_page_button) > 0:
            try:
                dont_add_to_main_page_button[0].click()
            except Exception as e:
                print(f"Error: {e}")

        nope_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Hayır']]"))
        )
        nope_button.click()
        print(f"Click {i+1}: Success!")
    except StaleElementReferenceException:
        print(f"Click {i+1}: Stale element, trying again...")
        continue
    except Exception as e:
        print(f"Click {i+1}: Failure, error code: {e}")
        continue
    else:
        rejected_women_count += 1
    finally:
        sleep(0.5)


print(f"{rejected_women_count} women rejected. What a waste!")