from selenium import webdriver
import time
from behave import *


@given('I go to 4davanceboy to add item')
def step(context):
    context.driver = webdriver.Chrome(executable_path="C:/Users/HP_Owner/PycharmProjects/bdd_demo/chromedriver.exe")
    context.driver.get("https://lambdatest.github.io/sample-todo-app/")
    time.sleep(2)


@then('I Click on first checkbox and second checkbox')
def click_on_checkbox_one(context):
    context.driver.find_element_by_xpath("/html/body/div/div/div/ul/li[1]/input").click()
    context.driver.find_element_by_xpath("/html/body/div/div/div/ul/li[2]/input").click()
    time.sleep(2)


@when('I enter item to add')
def enter_item_name(context):
    context.driver.find_element_by_id("sampletodotext").send_keys("Yey, Let's add it to list")
    time.sleep(2)

@when('I click add button')
def click_on_add_button(context):
    context.driver.find_element_by_id("addbutton").click()
    time.sleep(2)


@then('I should verify the added item')
def see_login_message(context):
    added_item = context.driver.find_element_by_xpath("//span[@class='done-false']").text
    time.sleep(5)
    if added_item in "Yey, Let's add it to list":
        return True
    else:
        return False
