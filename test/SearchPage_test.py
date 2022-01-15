from test.BaseTest import BaseTest


class SearchPageTest(BaseTest):


    def test_CheckResultListContainsKeyword(self):
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
