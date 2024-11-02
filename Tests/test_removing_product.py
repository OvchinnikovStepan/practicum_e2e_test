import pytest
from pages.market_main_page import MarketPage

@pytest.mark.regression
@pytest.mark.usefixtures('user_login')
class TestRemoveProduct:
    def test_remove_product(self, browser):
        p = MarketPage(browser)
        p.add_or_remove_product([0,1,2])
        p.add_or_remove_product([1,2])
        p.check_number_of_product_in_busket(1)