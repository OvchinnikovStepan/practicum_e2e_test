from pages.base import Base
from Locators.first_checkout_page import Checkout1
from data.assertions import Assertions
from playwright.sync_api import Page


class FirstCheckoutPage(Base):
    def __init__(self, page: Page):
        super().__init__(page)
        self.assertion = Assertions(page)

    def fill_and_contiune(self): 
        self.input(Checkout1.FIRST_NAME, "Ivan")
        self.input(Checkout1.LAST_NAME, "Ivanov")
        self.input(Checkout1.ZIP, "123456")
        self.click(Checkout1.CNT_BTN)
        