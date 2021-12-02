from selenium import webdriver
import time
from behave import *
@given('go to smartbear website')
def step(context):
    context.driver = webdriver.Chrome(executable_path="C:/Users/HP_Owner/PycharmProjects/bdd_smartbear/chromedriver.exe")
    context.driver.get("http://secure.smartbearsoftware.com/samples/testcomplete11/WebOrders/login.aspx")
    time.sleep(2)

@then('enter username and password')
def Login(context):
        context.driver.find_element_by_id("ctl00_MainContent_username").send_keys("Tester")
        context.driver.find_element_by_id("ctl00_MainContent_password").send_keys("test")
        time.sleep(2)
@then('click on login')
def Login_Button(context):
    context.driver.find_element_by_id("ctl00_MainContent_login_button").click()
    time.sleep(2)

@then('click on checkAll and click on uncheckAll')
def homepage_checkAll(context):
    context.driver.find_element_by_id("ctl00_MainContent_btnCheckAll").click()
    time.sleep(2)
    context.driver.find_element_by_id("ctl00_MainContent_btnUncheckAll").click()
    time.sleep(2)
@when('select on item')
def homepage_checkAll(context):
    context.driver.find_element_by_id("ctl00_MainContent_orderGrid_ctl06_OrderSelector").click()
    time.sleep(2)
@then('delete selected item')
def homepage_checkAll(context):
    context.driver.find_element_by_id("ctl00_MainContent_btnDelete").click()
    time.sleep(2)

@then('click on view all products')
def view_all_products(context):
    context.driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[1]/ul/li[2]/a").click()
    time.sleep(2)
@when('click on orders')
def orders(context):
    context.driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[1]/ul/li[3]/a").click()
    time.sleep(2)
@then('enter order purchase details')
def order_details(context):
    context.driver.find_element_by_id("ctl00_MainContent_fmwOrder_txtQuantity").send_keys("3")
    context.driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[2]/div[2]/table/tbody/tr/td/ol[1]/li[5]/input[2]").click()
    time.sleep(2)
    context.driver.find_element_by_id("ctl00_MainContent_fmwOrder_txtName").send_keys("chandana")
    context.driver.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox2").send_keys("abc")
    context.driver.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox3").send_keys("thrissur")
    context.driver.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox4").send_keys("kerala")
    context.driver.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox5").send_keys("680026")
    time.sleep(2)

    context.driver.find_element_by_id("ctl00_MainContent_fmwOrder_cardList_1").click()
    context.driver.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox6").send_keys("5678903454")
    context.driver.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox1").send_keys("12/22")
    time.sleep(2)
    context.driver.find_element_by_id("ctl00_MainContent_fmwOrder_InsertButton").click()
    time.sleep(2)

@then('click on logout')
def logout(context):
    context.driver.find_element_by_id("ctl00_logout").click()
    time.sleep(2)







