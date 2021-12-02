import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Constants




# Scenarios

scenarios('../features/Amazon.feature')


# Fixtures

@pytest.fixture
def browser():
    b = webdriver.Chrome('C:/Users/HP_Owner/PycharmProjects/Pytest_Amazon/chromedriver.exe')
   # b=webdriver.Chrome()
    b.implicitly_wait(10)
    yield b
    b.quit()
@given('visit amazon website')
def step(browser):

    browser.get("https://www.amazon.in/")
    browser.maximize_window()

@then('Search for an item')
def search_item(browser):
    browser.find_element_by_id("twotabsearchtextbox").send_keys("lipstick")

    browser.find_element_by_id("nav-search-submit-button").click()

@when('item found')
def item(browser):
    browser.find_element_by_id("nav-search-submit-button").click()

@then('select item')
def select_item(browser):
    browser.find_element_by_xpath("//html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[1]/span/div/div/div[1]/div[2]/div[1]/div/div[1]/a/div/img").click()

@then('order item')
def order(browser):
    browser.find_element_by_id("add-to-cart-button").click()
