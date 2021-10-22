from behave.runner import Context
from support.driver import Driver
from support.test_context import TestContext, ScenarioData
from selenium.webdriver.remote.webdriver import WebDriver
from support.driver import Driver
from support.pages import with_driver


def before_all(context: Context):
    context = TestContext(context)
    with_driver(Driver.get_driver())


def after_all(context: TestContext):
    Driver.quit_driver()


def before_scenario(context: TestContext, scenario):
    context.scenario_data = ScenarioData()
