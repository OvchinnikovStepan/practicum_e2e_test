from pages.base import Base
from Locators.basket_page import Basket
from Locators.market_page import Market
from data.assertions import Assertions
from playwright.sync_api import Page


class MarketPage(Base):
    def __init__(self, page: Page):
        super().__init__(page)
        self.assertion = Assertions(page)

    def add_or_remove_product(self,ids=[0]): 
        for id in ids:
            self.click_element_by_index(Market.ADD_OR_REMOVE_PRODUCT_BTN, id)
        
    def to_basket(self):
        self.click(Market.FOLLOW_TO_BASKET)

    def checkout(self): 
        self.click(Basket.CHECKOUT_BTN)
        self.input(Basket.FIRST_NAME, "Ivan")
        self.input(Basket.LAST_NAME, "Ivanov")
        self.input(Basket.ZIP, "123456")
        self.click(Basket.CNT_BTN)
        self.click(Basket.FINISH_BTN)
        self.assertion.have_text(Basket.FINAL_TEXT, "Checkout: Complete!", "no")

    def check_number_of_product_in_buscet(self,number):
        self.assertion.have_text(Market.NUMBER_OF_GOODS, str(number), "no")