from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# 1. Arama ikonuna tıkla (çünkü input gizli)
search_icon = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "search-toggle"))
)
search_icon.click()

# 2. Arama kutusunu bul ve yaz
search_box = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "searchInput"))
)
search_box.send_keys("Python")

# 3. Enter tuşu ile arama yap
search_box.send_keys(Keys.RETURN)