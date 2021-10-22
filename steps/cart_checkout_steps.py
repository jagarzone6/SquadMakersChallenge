from behave import use_step_matcher, step
from support.test_context import TestContext
import support.pages as pages

use_step_matcher('re')


@step('I add following products to the shopping cart')
def add_products_step(context: TestContext):
    for row in context.table:
        pages.products.add_product(row["PRODUCT NAME"])
        

@step('I go to the shopping cart')
def go_to_shopping_cart(context: TestContext):
    pages.menu.click_shopping_cart()


@step('I complete chekout process with following details')
def go_to_shopping_cart(context: TestContext):
    pages.car_check_out.click_checkout()
    checkout_info = context.table[0]
    pages.car_check_out.send_first_name(checkout_info["First Name"])
    pages.car_check_out.send_last_name(checkout_info["Last Name"])
    pages.car_check_out.send_zip_code(checkout_info["Zip/Postal Code"])
    pages.car_check_out.click_continue()
    pages.car_check_out.click_finish()



@step('the order should be completed successfully')
def go_to_shopping_cart(context: TestContext):
    pages.car_check_out.wait_for_successfull_order()
