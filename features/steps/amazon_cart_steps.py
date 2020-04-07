from behave import *
from nose.tools import assert_equals
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from features.object import Singleton
from features.pages.home_page import HomePage
from selenium.webdriver.common.keys import Keys
import time

@when(u'I search for the {product}')
def click_on_sign_in(context, product):
  home_page = Singleton.getInstance(context,HomePage)
  search_field = context.browser.find_element(By.XPATH, home_page.locators['search_field'])
  search_field.send_keys(product, Keys.ENTER)


@then('I validate if the {products} are found in the result page')
def validate_result_page(context, products):
  home_page = Singleton.getInstance(context,HomePage)
  if (products in context.browser.page_source):
    pass
  else:
      message = "Test Failed. The results not returned the searched product."

@when(u'I click on the {wanted} product in the page')
def select_product(context, wanted):
  home_page = Singleton.getInstance(context,HomePage)
  select_product = context.browser.find_element_by_xpath("//*[contains(text(), '"+wanted+"')]")
  select_product.click()
