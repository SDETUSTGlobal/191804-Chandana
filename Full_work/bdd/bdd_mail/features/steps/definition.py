from selenium import webdriver
import time
from behave import *
@given('visit gmail website')
def step(context):
    context.driver = webdriver.Chrome(executable_path="C:/Users/HP_Owner/PycharmProjects/bdd_mail/chromedriver.exe")
    context.driver.get("https://www.gmail.com/")
    context.driver.maximize_window()
    time.sleep(2)
@then('enter username')
def login(context):
    context.driver.find_element_by_id("identifierId").send_keys("chandanadivyan111@gmail.com")
    time.sleep(2)
@when('click next to enter password')
def login_button(context):
    context.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button").click()
    time.sleep(3)
@then('enter password')
def password(context):
    context.driver.find_element_by_name("password").send_keys("chandana1616")
@then('click on login')
def select_item(context):
    context.driver.find_element_by_xpath("//html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[1]/span/div/div/div[1]/div[2]/div[1]/div/div[1]/a/div/img").click()
    time.sleep(2)
