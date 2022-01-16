from test.BaseTest import BaseTest


class NewsPageTest(BaseTest):


    def test_CheckVisibilityEbayNews1(self):
        home_page = self.getHomePage()
        home_page.goNewsPage()
        news_page = self.getNewsPage()
        news_page.implicitly_wait(self.DEFAULT_TIMEOUT)
        news_page.isElementNewsVisible()
