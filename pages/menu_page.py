from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage, Locator


class MenuPage(BasePage):
    __menu_button: Locator = Locator(By.ID, 'react-burger-menu-btn')
    __logout_button: Locator = Locator(By.ID, 'logout_sidebar_link')
    __shopping_cart_button: Locator = Locator(By.ID, 'shopping_cart_container')

    def __init__(self, driver: WebDriver):
        self.driver = driver
        super().__init__(driver)

    def click_menu(self):
        self._wait_for_element_visible(MenuPage.__menu_button, 3)
        self._click(MenuPage.__menu_button)
    
    def click_logout(self):
        self._wait_for_element_visible(MenuPage.__logout_button, 3)
        self._click(MenuPage.__logout_button)

    def click_shopping_cart(self):
        self._wait_for_element_visible(MenuPage.__shopping_cart_button, 3)
        self._click(MenuPage.__shopping_cart_button)