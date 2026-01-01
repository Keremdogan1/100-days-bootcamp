from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

lang_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".langSelectButton.title"))
)
lang_button.click()

cookie_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "bigCookie"))
)

count = 0
while(True):
    cookie_button.click()
    sleep(0.025)
    count += 1
    if count % 100 == 0:
        upgrades = driver.find_elements(By.CSS_SELECTOR, value=".crate.upgrade.enabled")
        if(len(upgrades) > 0):
            upgrades[0].click()
        availible_products = driver.find_elements(By.CLASS_NAME, value="enabled")
        if len(availible_products) > 0:
            availible_products[-1].click()