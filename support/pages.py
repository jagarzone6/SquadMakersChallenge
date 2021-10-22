from pages.cart_checkout_page import CartCheckOut
from pages.menu_page import MenuPage
from selenium.webdriver.remote.webdriver import WebDriver
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

login: LoginPage = None
products: ProductsPage = None
menu: MenuPage = None
car_check_out: CartCheckOut = None


def with_driver(driver: WebDriver):
    global login, products, menu, car_check_out
    login = LoginPage(driver)
    products = ProductsPage(driver)
    menu = MenuPage(driver)
    car_check_out = CartCheckOut(driver)
