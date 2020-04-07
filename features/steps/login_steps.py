from behave import *
from nose.tools import assert_equals
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from features.datasource.users import DATA_ACCESS
from features.datasource.messages import SYSTEM_MESSAGES
from features.object import Singleton
from features.pages.home_page import HomePage
from features.pages.login_page import LoginPage
from features.pages.gmail_page_helper import run_gmail
import time

@given(u'I navigate to the Amazon Login page')
def navigate_to_the_amazon_login(context):
    home_page = Singleton.getInstance(context,HomePage)
    context.browser.get(home_page.project_url)
    login_button = context.browser.find_element(By.XPATH, home_page.locators['login'])
    login_button.click()

@when(u'I fill in the field username with {credential}')
def fill_in_the_field_username(context, credential):
    fill_in_the_field_an_username(context, credential, 'username')

@when(u'I fill in the field password with {credential}')
def fill_in_the_field_password(context, credential):
    fill_in_the_field_a_password(context, credential, 'password')

@when(u'I click on Continue button')
def click_on_continue(context):
    login_page = Singleton.getInstance(context,LoginPage)
    continue_button = context.browser.find_element(By.CSS_SELECTOR, login_page.locators['continue_button'])
    continue_button.click()

@when(u'I click on Sign In button')
def click_on_sign_in(context):
    login_page = Singleton.getInstance(context,LoginPage)
    sign_in_button = context.browser.find_element(By.CSS_SELECTOR, login_page.locators['sign_in_button'])
    sign_in_button.click()
    text= "Verificação necessária"
    if (text in context.browser.page_source):
      click_on_continue(context)
      run_gmail(context)


@when(u'the field username is filled with {credential} and the user {user}')
def fill_in_the_field_an_username(context, credential, user):
    login_page = Singleton.getInstance(context,LoginPage)
    user = login_page.datapool_read(login_page, DATA_ACCESS, credential, user)
    username_field = context.browser.find_element(By.CSS_SELECTOR, login_page.locators['username_field'])
    username_field.clear()
    username_field.send_keys(user)

@when(u'the field password is filled with {credential} and the password {password}')
def fill_in_the_field_a_password(context, credential, password):
    login_page = Singleton.getInstance(context,LoginPage)
    pwd = login_page.datapool_read(login_page, DATA_ACCESS,credential, password)
    password_field = context.browser.find_element(By.CSS_SELECTOR, login_page.locators['password_field'])
    password_field.clear()
    password_field.send_keys(pwd)

@when(u'I am current in Home Page')
@then(u'I am current in Home Page')
def current_page_is_home_page(context):
    text = "Olá, Faça seu login"
    if (text not in context.browser.page_source):
      pass
    else:
      message = "Test Failed. You are not at the home page."

@when("the Login page should have an error message: {message}")
@then("the Login page should have an error message: {message}")
def current_page_should_have_an_error_message(context, message):
    login_page = Singleton.getInstance(context, LoginPage)
    expected_message = login_page.datapool_read(login_page, SYSTEM_MESSAGES,'login_user', message)
    element_message = context.browser.find_elements(By.CLASS_NAME, login_page.locators['alert_message'])
    current_message = element_message[0].text + element_message[1].text
    if current_message == expected_message :
        pass
    else:
        message = "The alert threw wrong message on the login screen. It was expected the '"+expected_message+"' and was obtained '"+current_message+"'."
        raise Exception(message)

