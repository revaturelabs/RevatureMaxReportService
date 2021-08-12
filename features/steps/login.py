import time

from behave import *

@given('a user is on the login page')
def user_login(context):
    context.driver.get('http://localhost:9001/login')

@when('the associate enters the correct username and password')
def associate_login(context):
    time.sleep(0.5)
    context.ul.enter_credentials_associate()


@when('the associate pushes the submit button')
def press_submit_login(context):
    context.ul.click_to_login()


@then('the associate is redirected to the associate dashboard')
def redirect_dashboard(context):
    assert 'associateHome' in context.driver.current_url


@when('the associate clicks the enter key')
def click_enter(context):
    context.ul.press_enter_to_login()

@when('the trainer enters the correct username and password')
def trainer_enters_credentials(context):
    time.sleep(0.5)
    context.ul.enter_credentials_trainer()


@when('the trainer pushes the submit button')
def press_submit_login_trainer(context):
    context.ul.click_to_login()


@then('the trainer is redirected to the trainer dashboard')
def redirect_dashboard_trainer(context):
    assert 'employeeHome' in context.driver.current_url


@when('the trainer clicks the enter key')
def trainer_enter_button(context):
    context.ul.press_enter_to_login()
