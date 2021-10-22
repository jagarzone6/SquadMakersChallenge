from behave import use_step_matcher, step
from support.test_context import TestContext
import support.pages as pages

use_step_matcher('re')


@step('I log in with user "(.*)" and password "(.*)"')
def login_step(context: TestContext, user_name, password):
    pages.login.wait_for_login_page_visible()
    pages.login.set_username(user_name)
    pages.login.set_password(password)
    pages.login.click_login()


@step('products page .* displayed')
def products_page_should_be_displayed(context: TestContext):
    pages.products.wait_for_inventory_container_visible()


@step('I should see login page')
def should_see_login_page(context: TestContext):
    pages.login.wait_for_login_page_visible()
