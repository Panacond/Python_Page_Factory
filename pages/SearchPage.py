from selenium.webdriver.common.keys import Keys

from pages.BasePage import BasePage


class SearchPage(BasePage):
    locators = {
        "resultTitleSearch": ('XPATH', "//h3[@class='s-item__title']"),
        "noExactMatchesMessage": ('XPATH', "//h3[text()='No exact matches found']"),
        "fieldMinPrice": ('XPATH', "//input[@aria-label='Minimum Value in $']"),
        "resultErrorPriceFind": ('XPATH', "//div[@class='x-price__error']"),
        "relatedSearch": ('XPATH', "//span[@class='cbx x-refine__multi-select-cbx']"),
    }

    def getSearchResultTitle(self):
        return self.driver.find_elements_by_xpath("//h3[@class='s-item__title']")

    def isNoExactMatchesMessageVisible(self):
        self.noExactMatchesMessage.isDisplayed()

    def setMinimumPrice(self, price):
        self.fieldMinPrice.sendKeys(price + Keys.ENTER)

    def ErrorInputPriceValue(self):
        expected = True
        if self.resultErrorPriceFind.size() == 1:
            expected = False
        return expected

    def setRelatedSearch(self, text):
        for element in self.relatedSearch:
            try:
                elementText = element.getText()
            except Exception:
                elementText = ""
            if text in elementText:
                element.clik()
                continue
