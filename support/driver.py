from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Driver:
    driver: WebDriver = None

    @staticmethod
    def get_driver():
        if Driver.driver is None:
            Driver.driver = webdriver.Chrome(ChromeDriverManager().install())
        Driver.driver.maximize_window()
        return Driver.driver

    @staticmethod
    def quit_driver():
        Driver.driver.quit()


def go_to(url: str):
    Driver.driver.get(url)
