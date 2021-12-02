from selenium import webdriver
import time
from behave import *
@given('go to my website')
def step1(context):
    context.driver = webdriver.Chrome(executable_path="C:/Users/HP_Owner/PycharmProjects/final_project/chromedriver.exe")
    context.driver.get("http://127.0.0.1:5000/")
    context.driver.maximize_window()
    time.sleep(2)
@then('enter name,email,uid and company name')
def step2(context):
    context.driver.find_element_by_id("uname").send_keys("Rahul")
    context.driver.find_element_by_id("uid").send_keys("1236")
    context.driver.find_element_by_id("cname").send_keys("ust")
    context.driver.find_element_by_id("email").send_keys("Rahul1@gmail.com")
    time.sleep(3)
@when('click on submit')
def step3(context):
    context.driver.find_element_by_id("sumit").click()
@then('display the given details')
def step4(context):
    time.sleep(5);
