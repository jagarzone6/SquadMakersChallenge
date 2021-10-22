from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage, Locator


class CartCheckOut(BasePage):
    __checkout_button: Locator = Locator(By.ID, 'checkout')
    __first_name_field: Locator = Locator(By.ID, 'first-name')
    __last_name_field: Locator = Locator(By.ID, 'last-name')
    __zip_code_field: Locator = Locator(By.ID, 'postal-code')
    __continue_button: Locator = Locator(By.ID, 'continue')
    __finish_button: Locator = Locator(By.ID, 'finish')
    __order_completed_header: Locator = Locator(By.XPATH, "//h2[@class='complete-header'and contains(text(), 'THANK YOU FOR YOUR ORDER')]")


    def __init__(self, driver: WebDriver):
        self.driver = driver
        super().__init__(driver)

    def click_checkout(self):
        self._wait_for_element_visible(CartCheckOut.__checkout_button, 3)
        self._click(CartCheckOut.__checkout_button)


    def click_continue(self):
        self._wait_for_element_visible(CartCheckOut.__continue_button, 3)
        self._click(CartCheckOut.__continue_button)

    def click_finish(self):
        self._wait_for_element_visible(CartCheckOut.__finish_button, 3)
        self._click(CartCheckOut.__finish_button)


    def send_first_name(self, first_name:str):
        self._wait_for_element_visible(CartCheckOut.__first_name_field, 3)
        self._send_keys(CartCheckOut.__first_name_field, first_name)

    def send_last_name(self, last_name:str):
        self._wait_for_element_visible(CartCheckOut.__last_name_field, 3)
        self._send_keys(CartCheckOut.__last_name_field, last_name)

    def send_zip_code(self, zip_code:str):
        self._wait_for_element_visible(CartCheckOut.__zip_code_field, 3)
        self._send_keys(CartCheckOut.__zip_code_field, zip_code)

    def wait_for_successfull_order(self):
        self._wait_for_element_visible(CartCheckOut.__order_completed_header, 10)