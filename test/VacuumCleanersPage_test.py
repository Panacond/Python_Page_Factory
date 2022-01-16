from test.BaseTest import BaseTest


class SearchPageTest(BaseTest):


    def test_CheckVisibilityEbayNews3(self):
        home_page = self.getHomePage()
        home_page.clickButtonXiaomi()
        xiaomi_page = self.getXiaomiPage()
        xiaomi_page.clickButtonVacuumCleaners()
        xiaomi_vacuum_cleaners_page = self.getXiaomiVacuumCleanersPage()
        xiaomi_vacuum_cleaners_page.clickButtonPrice()
        xiaomi_vacuum_cleaners_page.clickSelectPriceRange150_350()
        list_price = xiaomi_vacuum_cleaners_page.getCheckPrise()
        expected = True
        for element in list_price:
            correctText = element.text.replace("$", "")
            correctText = correctText.split(" to ")[0]
            priceValue = float(correctText)
            if priceValue < 150:
                expected = False
            elif priceValue > 350:
                expected = False
        assert expected

    def test_change_view_of_cleaners_list4(self):
        home_page = self.getHomePage()
        home_page.clickButtonXiaomi()
        xiaomi_page = self.getXiaomiPage()
        xiaomi_page.clickButtonVacuumCleaners()
        xiaomi_vacuum_cleaners_page = self.getXiaomiVacuumCleanersPage()
        xiaomi_vacuum_cleaners_page.implicitly_wait(self.DEFAULT_TIMEOUT)
        xiaomi_vacuum_cleaners_page.clickButtonView()
        xiaomi_vacuum_cleaners_page.clickButtonViewList()
        xiaomi_vacuum_cleaners_page.isElementViewListVisible()

    def test_keyword_in_result_search_on_vacuum_cleaners_page8(self):
        home_page = self.getHomePage()
        home_page.clickButtonXiaomi()
        xiaomi_page = self.getXiaomiPage()
        xiaomi_page.clickButtonVacuumCleaners()
        xiaomi_vacuum_cleaners_page = self.getXiaomiVacuumCleanersPage()
        xiaomi_vacuum_cleaners_page.inputSearchField("vacuum")
        list_title = xiaomi_vacuum_cleaners_page.getListResultTitle()
        expected = False
        for element in list_title:
            if "Vacuum" in element.text:
                expected = True
        assert expected
