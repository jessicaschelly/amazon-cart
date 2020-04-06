from features.pages.base_page import BasePage


class GmailPage(BasePage):

    project_url = "https://www.gmail.com/"

    locators = {
        "login": "//*[@id='nav-link-accountList']",
    }
