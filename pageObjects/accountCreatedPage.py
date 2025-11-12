class AccountCreatedPage:
    def __init__(self,page):
        self.page = page

    def click_continue(self):
        self.page.get_by_role("link", name="Continue").click()
        from pageObjects.homePage import HomePage
        homePage = HomePage(self.page)
        return homePage