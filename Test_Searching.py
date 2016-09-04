import unittest
import pages.home as home
import pages.search_results_page as search_results_page
from selenium import webdriver
from hidden_info import WEB_APPLICATION_URL


# TEST DATA:
existent_goods = "Gabriella"
non_existent_goods = "iuioi jhjh"


class Search(unittest.TestCase):
    ''' User searches a goods from Home Page '''
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/opt/chromedriver")
        self.driver.get(WEB_APPLICATION_URL)

    def tearDown(self):
        self.driver.close()

    # @unittest.skip('User searches a goods in searching field')
    def test_search_goods(self):
        ''' User searches an existent goods in searching field '''
        page = home.Page(self.driver)
        page.search(existent_goods)
        result = search_results_page.Page(self.driver)
        self.assertIn(existent_goods, result.found())

    # @unittest.skip('User searches a goods in searching field')
    def test_search_inv_goods(self):
        ''' User searches a non-existent goods in searching field '''
        page = home.Page(self.driver)
        page.search(non_existent_goods)
        result = search_results_page.Page(self.driver)
        self.assertNotIn(non_existent_goods, result.found())


if __name__ == '__main__':
    unittest.main()
