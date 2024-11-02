from pages.main_page import Main
from Locators.auth import Auth

class TestLogin:
    def test_user_login(self, browser):
        m = Main(browser)
        m.user_login_custom()
        m.assertion.have_text(Auth.LOGIN_ERROR_CASE_TEXT,"Epic sadface: Username is required","fail")