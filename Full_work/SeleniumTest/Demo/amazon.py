from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
print("test case started")
driver = webdriver.Chrome()
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://www.amazon.in")
driver.find_element_by_id("twotabsearchtextbox").send_keys("lipstick")
time.sleep(2)

driver.find_element_by_id("nav-search-submit-button").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[1]/span/div/div/div[1]/div[2]/div[1]/div/div[2]/div/a/div").click()
time.sleep(2)
driver.find_element_by_id("add-to-cart-button").click()
time.sleep(3)
print("item added")
driver.close()
print("successfully completed")
