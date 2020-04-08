from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def run_gmail(context):
  context.browser.execute_script("window.open('');")
  context.browser.switch_to.window(context.browser.window_handles[1])
  context.browser.get("https://gmail.com/")
  context.browser.find_element(By.ID, "identifierId").send_keys("amazon.test.jessica@gmail.com")
  context.browser.find_element(By.CLASS_NAME, "CwaK9").click()
  context.browser.find_element(By.CSS_SELECTOR, "[name='password']").send_keys("amazontest123")
  context.browser.find_element(By.ID, "passwordNext").click()
  unreademail = context.browser.find_elements(By.CLASS_NAME,"zA")
  unreademail[0].click()

  time.sleep(3)

  path = "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/table/tr/td[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div[3]/div[3]/div/div[2]/table/tbody/tr/td/table/tbody/tr[2]/td/p[2]"
  verification_email = context.browser.find_element(By.XPATH, path).text

  print(verification_email)
  
  # context.browser.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w') 
  context.browser.close()
  context.browser.switch_to.window(context.browser.window_handles[0])
  return verification_email




