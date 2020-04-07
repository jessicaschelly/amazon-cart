from features.pages.base_page import BasePage


class HomePage(BasePage):

    project_url = "https://www.amazon.com.br/?ref_=nav_ya_signin&&"

    locators = {
        "login": "//*[@id='nav-link-accountList']",
        "hover_menu":"//*[@id='nav-link-accountList']",
        "search_field": "//*[@id='twotabsearchtextbox']",
        "add_cart_button": "add-to-cart-button",
        "continue_to_cart": "hlb-view-cart-announce",
        "expected_price": "priceblock_ourprice",
        "actual_price": "//*[@id='sc-subtotal-amount-buybox']/span",
        "actual_quantity": "sc-subtotal-label-buybox",
        "cart_icon": "nav-cart",
        "cart_count": "nav-cart-count",
        "home_page_icon": "nav-logo",
        "delete_item": "[value='Excluir']",
    }
