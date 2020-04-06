from selenium import webdriver

def browser_config(context, browser_name):

    if not browser_name != "firefox":
        option = webdriver.FirefoxOptions()
        option.add_argument("--start-maximized")
        option.add_argument("--disable-geolocation")
        option.add_argument("--ignore-certificate-errors")
        option.add_argument("--disable-popup-blocking")
        option.add_argument("--disable-translate")
        driver = webdriver.Firefox(firefox_options=option)
        return driver

    if not browser_name != "chrome":
        option = webdriver.ChromeOptions()
        option.add_argument("--start-maximized")
        option.add_argument("--disable-geolocation")
        option.add_argument("--ignore-certificate-errors")
        option.add_argument("--disable-popup-blocking")
        option.add_argument("--disable-translate")
        driver = webdriver.Chrome(chrome_options=option)
        return driver

    if not browser_name != "edge":
        driver = webdriver.Edge()
        return driver


def before_scenario(context, scenario):
    browser_name = context.config.userdata.get('browser')
    driver = browser_config(context, browser_name)
    context.browser = driver
    context.browser.implicitly_wait(10)
    context.browser.set_page_load_timeout(10)