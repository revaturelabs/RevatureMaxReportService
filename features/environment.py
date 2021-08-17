from selenium import webdriver
from selenium_pom_files.poms.user_login import UserLogin
from selenium_pom_files.poms.enter_text_into_search_box import SearchBox
from selenium_pom_files.poms.logout import LogOut
from selenium_pom_files.poms.view_statistics import AssociateInfo
from selenium_pom_files.poms.edit_profile_page import EditProfile

def before_all(context):
    context.driver = webdriver.Chrome(executable_path='/Users/amrab/Downloads/chromedriver_win32/chromedriver')
    context.ul = UserLogin(context.driver)
    context.sb = SearchBox(context.driver)
    context.lo = LogOut(context.driver)
    context.ai = AssociateInfo(context.driver)
    context.ep = EditProfile(context.driver)

def after_all(context):
    context.driver.quit()