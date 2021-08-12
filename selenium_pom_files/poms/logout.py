
class LogOut:
    log_out_xpath = '/html/body/header/div[2]/div[1]/div/a[5]'
    log_out_trainer_xpath = '/html/body/div/div[1]/div[2]/a/img'
    def __init__(self, driver):
        self.driver = driver

    def log_out(self):
        self.driver.find_element_by_xpath(self.log_out_xpath).click()
    def log_out_trainer(self):
        self.driver.find_element_by_xpath(self.log_out_trainer_xpath).click()