import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys




# Scenarios
scenarios('../features/web.feature')

@pytest.fixture
def browser():
    b = webdriver.Chrome('C:/Users/HP_Owner/PycharmProjects/pytest_smartbear/chromedriver.exe')
   # b=webdriver.Chrome()
    b.implicitly_wait(5)
    yield b
    b.quit()

@given('go to smartbear website')
def step(browser):

   browser.get("http://secure.smartbearsoftware.com/samples/testcomplete11/WebOrders/login.aspx")


@then('enter username and password')
def Login(browser):
        browser.find_element_by_id("ctl00_MainContent_username").send_keys("Tester")
        browser.find_element_by_id("ctl00_MainContent_password").send_keys("test")

@then('click on login')
def Login_Button(browser):
    browser.find_element_by_id("ctl00_MainContent_login_button").click()


@then('click on checkAll and click on uncheckAll')
def homepage_checkAll(browser):
   browser.find_element_by_id("ctl00_MainContent_btnCheckAll").click()
   browser.find_element_by_id("ctl00_MainContent_btnUncheckAll").click()

@when('select on item')
def homepage_checkAll(browser):
   browser.find_element_by_id("ctl00_MainContent_orderGrid_ctl06_OrderSelector").click()

@then('delete selected item')
def homepage_checkAll(browser):
   browser.find_element_by_id("ctl00_MainContent_btnDelete").click()


@then('click on view all products')
def view_all_products(browser):
    browser.find_element_by_xpath("/html/body/form/table/tbody/tr/td[1]/ul/li[2]/a").click()

@when('click on orders')
def orders(browser):
   browser.find_element_by_xpath("/html/body/form/table/tbody/tr/td[1]/ul/li[3]/a").click()

@then('enter order purchase details')
def order_details(browser):
   browser.find_element_by_id("ctl00_MainContent_fmwOrder_txtQuantity").send_keys("3")
   browser.find_element_by_xpath("/html/body/form/table/tbody/tr/td[2]/div[2]/table/tbody/tr/td/ol[1]/li[5]/input[2]").click()
   browser.find_element_by_id("ctl00_MainContent_fmwOrder_txtName").send_keys("chandana")
   browser.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox2").send_keys("abc")
   browser.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox3").send_keys("thrissur")
   browser.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox4").send_keys("kerala")
   browser.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox5").send_keys("680026")
   browser.find_element_by_id("ctl00_MainContent_fmwOrder_cardList_1").click()
   browser.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox6").send_keys("5678903454")
   browser.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox1").send_keys("12/22")
   browser.find_element_by_id("ctl00_MainContent_fmwOrder_InsertButton").click()


@then('click on logout')
def logout(browser):
   browser.find_element_by_id("ctl00_logout").click()



