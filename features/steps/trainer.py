import time

from behave import *

@when('a trainer is on the login page1')
def trainer_on_page(context):
    context.driver.get('http://localhost:9001/login')


@when('the trainer enters the correct username and password1')
def trainer_enters_credentials(context):
    time.sleep(0.5)
    context.ul.enter_credentials_trainer()


@when('the trainer pushes the submit button1')
def press_submit_login_trainer(context):
    context.ul.click_to_login()


@then('the trainer is redirected to the trainer dashboard1')
def redirect_dashboard_trainer(context):
    assert 'employeeHome' in context.driver.current_url

@when('a trainer presses the particular associate')
def trainer_associate_view(context):
    context.ai.associate_info()
    time.sleep(1)
    assert 'employeeHome' in context.driver.current_url

@given('the trainer enters text into the search bar')
def trainer_search_box(context):
    time.sleep(0.5)
    context.sb.enter_text_for_trainer()
    time.sleep(1)
    assert 'employeeHome' in context.driver.current_url

@when('the trainer presses the logout button')
def log_out(context):
    context.lo.log_out_trainer()

@then('the trainer is redirected to the login page')
def redirect_login(context):
    time.sleep(1)
    assert 'login' in context.driver.current_url


