from pages.main_page import Main
import pytest
from data.site_data import Errors
@pytest.mark.regression
class TestLogin:
    def test_user_login(self, browser):
        m = Main(browser)
        m.user_login()
    def test_user_login_empty(self, browser):
        m = Main(browser)
        m.user_login_custom()
        m.check_error(Errors.empty_login_error_text)