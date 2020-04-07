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
        option.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36")
        option.add_argument("Accept-Encoding=gzip, deflate")
        option.add_argument("Accept=text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8")
        option.add_argument("DNT=1")
        option.add_argument("Connection=close")
        option.add_argument("Upgrade-Insecure-Requests=1")
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

def after_scenario(context, scenario):
    if scenario.status == 'failed':
        # take_screenshot_on_failure(context, scenario)
        context.browser.close()
    else:
        context.browser.close()
