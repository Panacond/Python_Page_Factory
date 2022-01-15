from test.BaseTest import BaseTest


class SearchPageTest(BaseTest):


    def test_CheckVisibilityEbayNews(self):
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
