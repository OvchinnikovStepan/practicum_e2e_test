from pages.main_page import Main
import pytest
@pytest.mark.regression
class TestLogin:
    def test_user_login(self, browser):
        m = Main(browser)
        m.user_login()