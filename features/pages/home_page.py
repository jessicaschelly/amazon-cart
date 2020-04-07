from features.pages.base_page import BasePage


class HomePage(BasePage):

    project_url = "https://www.amazon.com.br/?ref_=nav_ya_signin&&"

    locators = {
        "login": "//*[@id='nav-link-accountList']",
        "hover_menu":"//*[@id='nav-link-accountList']",
        "sign_out_button": "#nav-item-signout",
        "search_field": "//*[@id='twotabsearchtextbox']",
        
    }
