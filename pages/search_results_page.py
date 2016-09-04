import home
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Page(home.Page):
    ''' Web page with searching result '''
    def __init__(self, driver):
        super(Page, self).__init__(driver)
        self.driver = driver

    def found(self):
        ''' Searching result '''
        try:
            WebDriverWait(self.driver, 4).until(
                ec.presence_of_all_elements_located(
                    (By.CSS_SELECTOR, ".mini-title>a")))
            result = self.driver.page_source
        except:
            result = ''
        return (result)
