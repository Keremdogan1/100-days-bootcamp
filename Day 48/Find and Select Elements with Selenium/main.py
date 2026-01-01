from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
""" driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")
driver.find_element(By.CLASS_NAME, value="a-button-text").click()


price_lira= driver.find_element(By.CSS_SELECTOR, ".olpWrapper.a-size-small")
price_string = price_lira.text.split()[4]
price = int(price_string.split(",")[0]) * 1000 + float(price_string.split(",")[1])

print(price) """


""" driver.get("https://www.python.org")

search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.get_attribute("placeholder"))
button = driver.find_element(By.ID, value="submit")
print(button.size)
documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text) """

driver.get("https://www.python.org")

bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

# driver.close()
driver.quit()