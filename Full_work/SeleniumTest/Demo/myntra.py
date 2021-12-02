from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
print("test case started")
driver = webdriver.Chrome()
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://www.myntra.com")
driver.find_element_by_xpath("/html/body/div[1]/div/div/header/div[2]/div[3]/input").send_keys("earing")


driver.find_element_by_xpath("/html/body/div[1]/div/div/header/div[2]/div[3]/a/span").click()
time.sleep(3)
#driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/main/div[3]/div[2]/div/div[2]/section/ul/li[2]/a/div[2]/div/span[1]").click()

driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/main/div[3]/div[2]/div/div[2]/section/ul/li[2]/a/div[2]").click()


driver.find_element_by_xpath("/html/body/div[2]/div/div/div/main/div[2]/div[2]/div[3]/div/div[1]").click()
time.sleep(3)
print("item added")
driver.close()
print("successfully completed")
