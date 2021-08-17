from selenium.webdriver.common.keys import Keys

class UserLogin:
    username_box_id = 'username'
    password_box_id = 'password'
    login_button_id = 'submit'

    def __init__(self, driver):
        self.driver = driver

    def enter_credentials_trainer(self):
        self.driver.find_element_by_id(self.username_box_id).send_keys('mock1022.employee870e1a69-f385-4cdb-9c59-986de917eca4@mock.com')
        self.driver.find_element_by_id(self.password_box_id).send_keys('password')

    def enter_credentials_associate(self):
        self.driver.find_element_by_id(self.username_box_id).send_keys('mock10.associate85408cf3-910e-4b61-a70c-f3e5bb20f2fc@mock.com')
        self.driver.find_element_by_id(self.password_box_id).send_keys('password')

    def click_to_login(self):
        self.driver.find_element_by_id(self.login_button_id).click()

    def press_enter_to_login(self):
        self.driver.find_element_by_id(self.password_box_id).send_keys(Keys.ENTER)