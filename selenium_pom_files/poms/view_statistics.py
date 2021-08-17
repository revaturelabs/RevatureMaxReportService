class AssociateInfo:
    associate_name_xpath = '/html/body/div/div[2]/div[2]/div/div/div[1]/table[2]/tbody/tr[2]/td[1]'

    def __init__(self, driver):
        self.driver = driver

    def associate_info(self):
        self.driver.find_element_by_xpath(self.associate_name_xpath).click()