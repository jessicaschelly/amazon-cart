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

@when(u'I add the {wanted} product to the cart with {quantity} and {options}')
def put_product_in_cart(context, quantity, options, wanted):
  home_page = Singleton.getInstance(context,HomePage)
  select_options = context.browser.find_element_by_xpath("//*[contains(text(), '"+options+"')]")
  select_options.click()
  select_quantity = context.browser.find_element_by_xpath("//select[@name='quantity']/option[@value='"+quantity+"']").click()

@then('I validate if the {wanted} is in the cart and if the quantity in the cart is {quantity}')
def validate_cart_page(context, quantity, wanted):
  home_page = Singleton.getInstance(context,HomePage)
  expected_price = context.browser.find_element(By.ID, home_page.locators['expected_price']).text
  quantity_selected = context.browser.find_element_by_xpath("//select[@name='quantity']/option[@value='"+quantity+"']").text
  click_on_cart = context.browser.find_element(By.ID, home_page.locators['add_cart_button'])
  click_on_cart.click()
  continue_to_cart = context.browser.find_element(By.ID, home_page.locators['continue_to_cart'])
  continue_to_cart.click()
  actual_price = context.browser.find_element(By.XPATH, home_page.locators['actual_price']).text
  actual_quantity = context.browser.find_element_by_xpath("//*[contains(text(), '("+quantity+"')]").text
  if(int(quantity) > 1):
    actual_price = float(actual_price.replace('R$','').replace('.',''). replace(',', '.'))
    expected_price = expected_price.replace('R$', '').replace('.',''). replace(',', '.')
    expected_price = float(expected_price) * int(quantity);
  assert_equals(expected_price, actual_price)
  if(actual_quantity != " "):
    pass
  else:
    message = "The test failed. The quantity expected is no the same in the cart."
  
  remove_from_cart(context)

@then('I remove the product from my cart')
@when(u'I remove the product from my cart')
def remove_from_cart(context):
  home_page = Singleton.getInstance(context,HomePage)
  click_on_cart_icon = context.browser.find_element(By.ID, home_page.locators['cart_icon']).click()
  remove_from_cart = context.browser.find_element_by_xpath("//*[contains(text(), 'Excluir')]")
  remove_from_cart.click()

@then('I see my cart empty')
def validate_empty_cart(context):
  message = "Seu carrinho de compras da Amazon está vazio."
  empty_cart_message = context.browser.find_element_by_xpath("//*[contains(text(), '"+message+"')]").text
  assert_equals(message, empty_cart)
  
