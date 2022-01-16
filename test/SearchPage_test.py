from test.BaseTest import BaseTest


class SearchPageTest(BaseTest):


    def test_CheckResultListContainsKeyword2(self):
        home_page = self.getHomePage()
        home_page.inputFieldSearch("cucumber")
        home_page.clickButtonSearch()
        search_page = self.getSearchPage()
        listTitle = search_page.getSearchResultTitle()
        expected = False
        for element in listTitle:
            if "Cucumber" in element.text:
                expected = True
        assert expected

    def test_incorrect_username_make_error_message6(self):
        home_page = self.getHomePage()
        home_page.inputFieldSearch("asfdsf")
        home_page.clickButtonSearch()
        search_page = self.getSearchPage()
        search_page.isNoExactMatchesMessageVisible()

    def test_incorrect_input_min_price_range_make_error_message9(self):
        home_page = self.getHomePage()
        home_page.inputFieldSearch("cucumber")
        home_page.clickButtonSearch()
        search_page = self.getSearchPage()
        search_page.setMinimumPrice("asd")
        search_page.errorInputPriceValue()

    def test_selected_keyword_in_results_search_list_visibility10(self):
        home_page = self.getHomePage()
        home_page.inputFieldSearch("cucumber")
        home_page.clickButtonSearch()
        search_page = self.getSearchPage()
        search_page.setRelatedSearch("Tomato")
        list_title = search_page.getSearchResultTitle()
        expected = False
        for element in list_title:
            if "Tomato" in element.text:
                expected = True
                break
        assert expected
