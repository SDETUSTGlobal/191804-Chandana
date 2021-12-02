import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Constants




# Scenarios

scenarios('../features/mail.feature')


# Fixtures

@pytest.fixture
def browser():
    b = webdriver.Chrome('C:/Users/HP_Owner/PycharmProjects/pytest_mail/chromedriver.exe')
   # b=webdriver.Chrome()
    b.implicitly_wait(10)
    yield b
    b.quit()
@given('visit gmail website')
def step(browser):
    browser.get("https://www.gmail.com/")
    browser.maximize_window()

@then('enter username')
def login(browser):
    browser.find_element_by_id("identifierId").send_keys("chandanadivyan111@gmail.com")

@when('click next to enter password')
def login_button(browser):
    browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button").click()

@then('enter password')
def password(browser):
   browser.find_element_by_name("password").send_keys("chandana1616")
@then('click on login')
def select_item(browser):
   browser.find_element_by_xpath("//html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[1]/span/div/div/div[1]/div[2]/div[1]/div/div[1]/a/div/img").click()
  