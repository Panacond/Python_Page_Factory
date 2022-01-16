from test.BaseTest import BaseTest


class SearchPageTest(BaseTest):

    def test_incorrect_quantity_makes_error_message7(self):
        home_page = self.getHomePage()
        home_page.clickButtonXiaomi()
        xiaomi_page = self.getXiaomiPage()
        xiaomi_page.clickButtonVacuumCleaners()
        xiaomi_vacuum_cleaners_page = self.getXiaomiVacuumCleanersPage()
        xiaomi_vacuum_cleaners_page.implicitly_wait(self.DEFAULT_TIMEOUT)
        xiaomi_vacuum_cleaners_page.clickFirstElementList()
        product_page = self.getProductPage()
        product_page.clickFieldNumberProduct()
        product_page.inputFieldNumberProduct(0)
        product_page.isErrorNumberMessage()

    def test_incorrect_username_makes_error_message(self):
        home_page = self.getHomePage()
        home_page.clickButtonXiaomi()
        xiaomi_page = self.getXiaomiPage()
        xiaomi_page.clickButtonVacuumCleaners()
        xiaomi_vacuum_cleaners_page = self.getXiaomiVacuumCleanersPage()
        xiaomi_vacuum_cleaners_page.implicitly_wait(self.DEFAULT_TIMEOUT)
        xiaomi_vacuum_cleaners_page.clickFirstElementList()
        product_page = self.getProductPage()
        product_page.clickButtonAddToWatchlist()
        login_page = self.getLoginPage()
        login_page.inputFieldUserName('Alex')
        login_page.clickButtonContinue()
        login_page.isErrorMessageVisible()