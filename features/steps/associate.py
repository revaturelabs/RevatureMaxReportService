import time

from behave import *

@when('an associate is on the login page')
def user_login(context):
    context.driver.get('http://localhost:9001/login')

@when('the associate enters the correct username and password1')
def associate_login(context):
    time.sleep(0.5)
    context.ul.enter_credentials_associate()


@when('the associate pushes the submit button1')
def press_submit_login(context):
    context.ul.click_to_login()


@then('the associate is redirected to the associate dashboard1')
def redirect_dashboard(context):
    assert 'associateHome' in context.driver.current_url

@given('the user enters text into the search bar')
def enter_text_search_bar(context):
    context.sb.enter_text_for_associate()
    time.sleep(0.5)
    assert 'associateHome' in context.driver.current_url

@when('the associate clicks on the profile icon')
def profile_icon(context):
    context.ep.click_on_icon()
    time.sleep(0.5)


@when('the associate clicks on the edit profile button')
def edit_profile(context):
    context.ep.go_to_edit_profile()
    time.sleep(1)


@then('the associate is redirected to the edit profile page')
def redirect_edit_profile(context):
    assert 'associateprofile' in context.driver.current_url

@when('the associate clicks on the change password button')
def change_password(context):
    context.ep.go_to_change_password()
    time.sleep(1)


@then('the associate is redirected to the change password page')
def redirect_change_password(context):
    assert 'passwordchange' in context.driver.current_url


