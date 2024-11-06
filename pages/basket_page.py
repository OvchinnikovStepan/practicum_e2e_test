from pages.base import Base
from Locators.basket_page import Basket
from data.assertions import Assertions
from playwright.sync_api import Page


class BasketPage(Base):
    def __init__(self, page: Page):
        super().__init__(page)
        self.assertion = Assertions(page)

    def checkout(self): 
        self.click(Basket.CHECKOUT_BTN)