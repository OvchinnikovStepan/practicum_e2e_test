from pages.base import Base
from Locators.second_checkout_page import Checkout2
from data.assertions import Assertions
from playwright.sync_api import Page


class SecondCheckoutPage(Base):
    def __init__(self, page: Page):
        super().__init__(page)
        self.assertion = Assertions(page)

    def finish(self): 
        self.click(Checkout2.FINISH_BTN)