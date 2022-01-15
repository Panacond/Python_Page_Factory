import unittest
from selenium import webdriver
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from pages.NewsPage import NewsPage
from pages.ProductPage import ProductPage
from pages.SearchPage import SearchPage
from pages.XiaomiPage import XiaomiPage
from pages.XiaomiVacuumCleanersPage import XiaomiVacuumCleanersPage


class BaseTest(unittest.TestCase):

    DEFAULT_TIMEOUT = 100

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.ebay.com/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()

    def getHomePage(self):
        return HomePage(self.driver)

    def getLoginPage(self):
        return LoginPage(self.driver)

    def getNewsPage(self):
        return NewsPage(self.driver)

    def getProductPage(self):
        return ProductPage(self.driver)

    def getSearchPage(self):
        return SearchPage(self.driver)

    def getXiaomiPage(self):
        return XiaomiPage(self.driver)

    def getXiaomiVacuumCleanersPage(self):
        return XiaomiVacuumCleanersPage(self.driver)
