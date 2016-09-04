from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class Page(object):
    ''' Page that is loaded when user has come to shop '''

    def __init__(self, driver):
        self.driver = driver
        # Searching field
        self.title = self.driver.title

        self.search_field = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, ".search-block")))

        # Top left menu links
        self.top_left_menu_links = WebDriverWait(self.driver, 10).until(
            ec.presence_of_all_elements_located(
                (By.XPATH, ".//*[@id='top-links']/div[1]/ul[2]/li")))
        self.about_company_link = self.top_left_menu_links[0]
        self.delivery_link = self.top_left_menu_links[1]
        self.return_products_link = self.top_left_menu_links[2]
        self.sizechart_link = self.top_left_menu_links[3]
        self.contact_us_link = self.top_left_menu_links[4]

        # Top right menu links
        self.wishlist_link = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(
                (By.XPATH, ".//*[@id='top-links']//li[@class='wishlist']")))

        self.login_link = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(
                (By.XPATH, ".//*[@id='top-links']//a[@class='login-link']")))

    def follow(self, link):
        ''' Follow the link '''
        cursor = ActionChains(self.driver)
        cursor.move_to_element(link)
        cursor.click(link)
        cursor.perform()

    def search(self, goods):
        ''' Searching a goods '''

        self.goods_to_searching = goods

        self.search_field = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, ".search-block")))

        mouse_move = ActionChains(self.driver)
        mouse_move.move_to_element(self.search_field)
        mouse_move.click(self.search_field)
        mouse_move.send_keys(self.goods_to_searching, Keys.ENTER)
        mouse_move.perform()

        # return resultPage(self.driver)
