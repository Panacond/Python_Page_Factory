from test.base_test import BaseTest


class SearchPageTest(BaseTest):

    def test_check_visibility_ebay_news3(self):
        home_page = self.getHomePage()
        home_page.click_button_xiaomi()
        xiaomi_page = self.get_xiaomi_page()
        xiaomi_page.click_button_vacuum_cleaners()
        xiaomi_vacuum_cleaners_page = self.get_xiaomi_vacuum_cleaners_page()
        xiaomi_vacuum_cleaners_page.click_button_price()
        xiaomi_vacuum_cleaners_page.click_select_price_range150_350()
        list_price = xiaomi_vacuum_cleaners_page.get_check_prise()
        expected = True
        for element in list_price:
            correct_text = element.text.replace("$", "")
            correct_text = correct_text.split(" to ")[0]
            price_value = float(correct_text)
            if price_value < 150:
                expected = False
            elif price_value > 350:
                expected = False
        assert expected

    def test_change_view_of_cleaners_list4(self):
        home_page = self.getHomePage()
        home_page.click_button_xiaomi()
        xiaomi_page = self.get_xiaomi_page()
        xiaomi_page.click_button_vacuum_cleaners()
        xiaomi_vacuum_cleaners_page = self.get_xiaomi_vacuum_cleaners_page()
        xiaomi_vacuum_cleaners_page.implicitly_wait(self.DEFAULT_TIMEOUT)
        xiaomi_vacuum_cleaners_page.click_button_view()
        xiaomi_vacuum_cleaners_page.click_button_view_list()
        xiaomi_vacuum_cleaners_page.is_element_view_list_visible()

    def test_keyword_in_result_search_on_vacuum_cleaners_page8(self):
        home_page = self.getHomePage()
        home_page.click_button_xiaomi()
        xiaomi_page = self.get_xiaomi_page()
        xiaomi_page.click_button_vacuum_cleaners()
        xiaomi_vacuum_cleaners_page = self.get_xiaomi_vacuum_cleaners_page()
        xiaomi_vacuum_cleaners_page.input_search_field("vacuum")
        list_title = xiaomi_vacuum_cleaners_page.get_list_result_title()
        expected = False
        for element in list_title:
            if "Vacuum" in element.text:
                expected = True
        assert expected
