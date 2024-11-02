from pages.main_page import Main
from data.constants import Constants
import pytest
@pytest.mark.regression
class TestLoginEmpty:
    def test_user_login(self, browser):
        m = Main(browser)
        m.user_login_custom()
        m.check_error(Constants.empty_login_error_msg)