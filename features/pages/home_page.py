from features.pages.base_page import BasePage


class HomePage(BasePage):

    project_url = "https://www.amazon.com.br/"

    locators = {
        "login": "//*[@id='nav-link-accountList']",
    }
