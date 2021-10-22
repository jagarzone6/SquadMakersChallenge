from behave import use_step_matcher, step
from support.test_context import TestContext
import support.pages as pages

use_step_matcher('re')


@step('I attempt to logout from the website')
def logout_step(context: TestContext):
    pages.menu.click_menu()
    pages.menu.click_logout()

