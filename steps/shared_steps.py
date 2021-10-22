from behave import use_step_matcher, step
from support.test_context import TestContext
from support.driver import go_to
import support.pages as pages

use_step_matcher('re')


@step('I have access to saucedemo app')
def open_app(context: TestContext):
    go_to("https://www.saucedemo.com/")


@step('error message "(.*)" should be displayed')
def error_diplayed(context: TestContext, error_str):
    pages.login.wait_for_error_visible(error_str)


@step('I should see "(.*)" message')
def login_step(context: TestContext, message):
    pages.car_check_out.wait_for_message_visible(message)