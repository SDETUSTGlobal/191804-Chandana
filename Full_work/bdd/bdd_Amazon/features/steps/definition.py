from selenium import webdriver
import time
from behave import *
@given('visit amazon website')
def step(context):
    context.driver = webdriver.Chrome(executable_path="C:/Users/HP_Owner/PycharmProjects/bdd_Amazon/chromedriver.exe")
    context.driver.get("https://www.amazon.in/")
    context.driver.maximize_window()
    time.sleep(2)
@then('Search for an item')
def search_item(context):
    context.driver.find_element_by_id("twotabsearchtextbox").send_keys("lipstick")
    time.sleep(2)
    context.driver.find_element_by_id("nav-search-submit-button").click()

@when('item found')
def item(context):
    context.driver.find_element_by_id("nav-search-submit-button").click()

@then('select item')
def select_item(context):
    context.driver.find_element_by_xpath("//html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[1]/span/div/div/div[1]/div[2]/div[1]/div/div[1]/a/div/img").click()
    time.sleep(2)
@then('order item')
def order(context):
    context.driver.find_element_by_id("add-to-cart-button").click()
    time.sleep(3)




