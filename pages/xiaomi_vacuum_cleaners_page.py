from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class XiaomiVacuumCleanersPage(BasePage):

    locators = {
        "button_price": ('XPATH', "//span[text()='Price']"),
        "select_price_range_150_350": ('XPATH', "//span[text()='$150.00 to $350.00']"),
        "check_price": ('XPATH', "//span[@class='s-item__price']"),
        "button_view": ('XPATH', "//button[@aria-label='Gallery View']"),
        "button_view_list": ('XPATH', "//span[text()='List View']"),
        "element_view_list": ('XPATH', "//ul[@class='b-list__items_nofooter']"),
        "first_element_list": ('XPATH', "//div[@class='s-item__wrapper clearfix']"),
        "search_Field": ('XPATH', "//input[@placeholder='Search for anything']"),
        "list_result_title": ('XPATH', "//h3[@class='s-item__title']"),
    }

    def click_button_price(self):
        self.button_price.click()

    def click_select_price_range150_350(self):
        self.select_price_range_150_350.click()

    def get_check_prise(self):
        # return self.check_price.get_all_list_item()
        return self.driver.find_elements_by_xpath(self.locators.get("check_price")[1])

    def click_button_view(self):
        self.button_view.click_button()

    def click_button_view_list(self):
        self.button_view_list.click_button()

    def is_element_view_list_visible(self):
        self.element_view_list.is_displayed()

    def click_first_element_list(self):
        self.first_element_list.click()

    def input_search_field(self, text):
        self.search_Field.set_text(text + Keys.ENTER)

    def get_list_result_title(self):
        # return self.list_result_title.get_all_list_item()
        return self.driver.find_elements_by_xpath(self.locators.get("list_result_title")[1])
