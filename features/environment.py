from selenium import webdriver


def before_all(context):
    context.driver = webdriver.Chrome(executable_path='/Users/amrab/Downloads/chromedriver_win32/chromedriver')


def after_all(context):
    context.driver.quit()