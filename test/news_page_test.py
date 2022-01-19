from test.base_test import BaseTest


class NewsPageTest(BaseTest):

    def test_check_visibility_ebay_news1(self):
        home_page = self.getHomePage()
        home_page.go_news_page()
        news_page = self.get_news_page()
        news_page.implicitly_wait(self.DEFAULT_TIMEOUT)
        news_page.is_element_news_visible()
