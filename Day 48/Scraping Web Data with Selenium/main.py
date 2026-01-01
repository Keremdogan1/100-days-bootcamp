from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.python.org")
raw_dates = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/time')
names = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/a')

time_list = [{"time":raw_date.get_attribute("datetime").split("T")[0]} for raw_date in raw_dates]
name_list = [name.text for name in names]

event_dict = {}
for index, element in enumerate(time_list):
    event_dict[index] = element
    event_dict[index] = {**event_dict[index], "name": name_list[index]}

print(event_dict)

driver.quit()

