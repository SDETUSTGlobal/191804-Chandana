from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
print("test case started")
driver = webdriver.Chrome()
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://www.flipkart.com")
driver.find_element_by_xpath("/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input").send_keys("lipstick")
driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()

driver.find_element_by_xpath("/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/button").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/div/a[2]").click()
time.sleep(3)
print("item added")
driver.close()
print("successfully completed")
