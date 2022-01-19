from test.base_test import BaseTest


class SearchPageTest(BaseTest):

    def test_incorrect_quantity_makes_error_message7(self):
        home_page = self.getHomePage()
        home_page.click_button_xiaomi()
        xiaomi_page = self.get_xiaomi_page()
        xiaomi_page.click_button_vacuum_cleaners()
        xiaomi_vacuum_cleaners_page = self.get_xiaomi_vacuum_cleaners_page()
        xiaomi_vacuum_cleaners_page.implicitly_wait(self.DEFAULT_TIMEOUT)
        xiaomi_vacuum_cleaners_page.click_first_element_list()
        product_page = self.get_product_page()
        product_page.click_field_number_product()
        product_page.input_field_number_product(0)
        product_page.is_error_number_message()

    def test_incorrect_username_makes_error_message5(self):
        home_page = self.getHomePage()
        home_page.click_button_xiaomi()
        xiaomi_page = self.get_xiaomi_page()
        xiaomi_page.click_button_vacuum_cleaners()
        xiaomi_vacuum_cleaners_page = self.get_xiaomi_vacuum_cleaners_page()
        xiaomi_vacuum_cleaners_page.implicitly_wait(self.DEFAULT_TIMEOUT)
        xiaomi_vacuum_cleaners_page.click_first_element_list()
        product_page = self.get_product_page()
        product_page.click_button_add_to_watchlist()
        login_page = self.get_login_page()
        login_page.input_field_user_name('Alex')
        login_page.click_button_continue()
        login_page.is_error_message_visible()