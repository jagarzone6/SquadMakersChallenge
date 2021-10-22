from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage, Locator


class ProductsPage(BasePage):
    __inventory_container: Locator = Locator(By.ID, 'inventory_container')
    __add_product_button: Locator = Locator(By.XPATH, "//div[@class='inventory_item' and .//div[@class='inventory_item_name' and contains(text(), '{}')]]//button")

    def __init__(self, driver: WebDriver):
        self.driver = driver
        super().__init__(driver)

    def wait_for_inventory_container_visible(self) -> bool:
        return self._wait_for_element_visible(ProductsPage.__inventory_container, 5)

    def add_product(self, product_name:str):
        self._click(Locator(ProductsPage.__add_product_button.by, ProductsPage.__add_product_button.locator.format(product_name)))
