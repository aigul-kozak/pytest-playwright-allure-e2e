from pageObjects.createUser import CreateUser
from pageObjects.homePage import HomePage


class AccountDeletedPage:
    def __init__(self, page):
        self.page = page
    def continue_after_del(self):
        self.page.get_by_role("link", name="Continue").click()
        home_page = HomePage(self.page)
        return home_page