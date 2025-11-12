import pytest
#from pytest_playwright.pytest_playwright import page
import json


class HomePage:
    def __init__(self,page):
        self.page = page

    def logout(self):
        self.page.get_by_role("link", name=" Logout").click()
        from pageObjects.createUser import CreateUser
        createUserPage = CreateUser(self.page)
        return createUserPage

    def delete(self):
        self.page.get_by_role("link", name=" Delete Account").click()
        from pageObjects.accountDeletedPage import AccountDeletedPage
        accountDeletedPage = AccountDeletedPage(self.page)
        return accountDeletedPage