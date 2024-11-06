from pages.base import Base
from data.assertions import Assertions
from playwright.sync_api import Page
from Locators.finish_page import Finish

class FinishPage(Base):
    def __init__(self, page: Page):
        super().__init__(page)
        self.assertion = Assertions(page)

    def is_succesful(self):
        self.assertion.have_text(Finish.FINAL_TEXT, "Checkout: Complete!", "no")