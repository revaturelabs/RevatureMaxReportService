
class SearchBox:
    search_box = 'searchBox'
    dashboard_xpath = '/html/body/div/div[1]/ul/li[1]/span'
    def __init__(self, driver):
        self.driver = driver

    def enter_text_for_associate(self):
        self.driver.find_element_by_id(self.search_box).send_keys('QC')
    def enter_text_for_trainer(self):
        self.driver.find_element_by_xpath(self.dashboard_xpath).click()
        self.driver.find_element_by_id(self.search_box).send_keys('name2')