from features.pages.base_page import BasePage


class HomePage(BasePage):

    project_url = "https://www.amazon.com/"

    locators = {
        "login": "//*[@id='nav-link-accountList']",
    }
