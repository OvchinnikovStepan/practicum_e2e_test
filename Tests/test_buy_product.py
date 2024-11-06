import pytest
from pages.market_main_page import MarketPage
from pages.basket_page import BasketPage
from pages.first_checkout_page import FirstCheckoutPage
from pages.second_checkout_page import SecondCheckoutPage
from pages.finish_page import FinishPage
@pytest.mark.regression
@pytest.mark.usefixtures('user_login')
class TestBuyProduct:
    def test_buy_product(self, browser):
        p = MarketPage(browser)
        p.add_or_remove_product()
        p.to_basket()
        p=BasketPage(browser)
        p.checkout()
        p=FirstCheckoutPage(browser)
        p.fill_and_contiune()
        p=SecondCheckoutPage(browser)
        p.finish()
        p=FinishPage(browser)
        p.is_succesful()
       