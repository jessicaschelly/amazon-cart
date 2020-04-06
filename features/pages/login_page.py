from features.pages.base_page import BasePage


class LoginPage(BasePage):

    project_url = "https://www.amazon.com.br/"

    locators = {
        "username_field": "#ap_email",
        "continue_button": "#continue",
        "password_field": "#ap_password",
        "sign_in_button": "#signInSubmit",
        "alert_message": ".a-alert-content"
    }
