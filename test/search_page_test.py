from test.base_test import BaseTest


class SearchPageTest(BaseTest):


    def test_CheckResultListContainsKeyword2(self):
        home_page = self.getHomePage()
        home_page.input_field_search("cucumber")
        home_page.click_button_search()
        search_page = self.get_search_page()
        list_title = search_page.get_search_result_title()
        expected = False
        for element in list_title:
            if "Cucumber" in element.text:
                expected = True
        assert expected

    def test_incorrect_username_make_error_message6(self):
        home_page = self.getHomePage()
        home_page.input_field_search("asfdsf")
        home_page.click_button_search()
        search_page = self.get_search_page()
        search_page.is_no_exact_matches_message_visible()

    def test_incorrect_input_min_price_range_make_error_message9(self):
        home_page = self.getHomePage()
        home_page.input_field_search("cucumber")
        home_page.click_button_search()
        search_page = self.get_search_page()
        search_page.set_minimum_price("asd")
        search_page.error_input_price_value()

    def test_selected_keyword_in_results_search_list_visibility10(self):
        home_page = self.getHomePage()
        home_page.input_field_search("cucumber")
        home_page.click_button_search()
        search_page = self.get_search_page()
        search_page.set_related_search("Tomato")
        list_title = search_page.get_search_result_title()
        expected = False
        for element in list_title:
            if "Tomato" in element.text:
                expected = True
                break
        assert expected
