from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from dataclasses import dataclass
from selenium.webdriver.support import expected_conditions as ec


@dataclass
class Locator:
    by: By
    locator: str


class BasePage:
    __error_msg: Locator = Locator(By.XPATH, "//*[@data-test='error' and contains(text(), '{}')]")
    __any_msg: Locator = Locator(By.XPATH, "//*[contains(text(), '{}')]")


    def __init__(self, driver: WebDriver):
        self.driver = driver

    def _send_keys(self, locator: Locator, keys: str):
        elem = self.driver.find_element(locator.by, locator.locator)
        elem.clear()
        elem.send_keys(keys)

    def _click(self, locator: Locator):
        elem = self.driver.find_element(locator.by, locator.locator)
        elem.click()

    def _is_element_visible(self, locator: Locator):
        elem = self.driver.find_element(locator.by, locator.locator)
        return elem.is_displayed()

    def _wait_for_element_visible(self, locator: Locator, seconds: int):
        wait = WebDriverWait(self.driver, seconds)
        elem = wait.until(ec.visibility_of_element_located((locator.by, locator.locator)))
        return elem

    def wait_for_error_visible(self, error: str):
        wait = WebDriverWait(self.driver, 10)
        elem = wait.until(ec.visibility_of_element_located((self.__error_msg.by, self.__error_msg.locator.format(error))))
        return elem

    def wait_for_message_visible(self, message: str):
        wait = WebDriverWait(self.driver, 10)
        elem = wait.until(ec.visibility_of_element_located((self.__any_msg.by, self.__any_msg.locator.format(message))))
        return elem
