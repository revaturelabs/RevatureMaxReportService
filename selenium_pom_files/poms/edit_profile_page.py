
class EditProfile:
    profile_icon_xpath = '/html/body/header/div[2]/div[2]/div/div[1]/img'
    edit_profile_xpath = '/html/body/header/div[2]/div[2]/div/div[2]/ul/li[1]/a'
    change_password_xpath = '/html/body/header/div[2]/div[2]/div/div[2]/ul/li[2]/a'
    def __init__(self, driver):
        self.driver = driver

    def click_on_icon(self):
        self.driver.find_element_by_xpath(self.profile_icon_xpath).click()
    def go_to_edit_profile(self):
        self.driver.find_element_by_xpath(self.edit_profile_xpath).click()
    def go_to_change_password(self):
        self.driver.find_element_by_xpath(self.change_password_xpath).click()