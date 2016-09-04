import unittest
import pages.home as home
from selenium import webdriver
from hidden_info import WEB_APPLICATION_URL


class TestingLinks(unittest.TestCase):
    ''' User searches a goods from Home Page '''
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/opt/chromedriver")
        self.driver.get(WEB_APPLICATION_URL)

    def tearDown(self):
        self.driver.close()

    # @unittest.skip('User searches a goods in searching field')
    def test_top_links(self):
        ''' Serfing through all top links '''
        page = home.Page(self.driver)
        links = len(page.top_left_menu_links)
        i = 0
        while i < links:
            page.follow(page.top_left_menu_links[i])
            page = home.Page(self.driver)
            print (page.title)
            i = i + 1


if __name__ == '__main__':
    unittest.main()
