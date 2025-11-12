from pytest_playwright.pytest_playwright import page
from pageObjects.loginPage import LoginPage

class CreateUser:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://www.automationexercise.com/")
    def signup(self):

        try:
            if self.page.locator("button:has-text('Consent')").is_visible():
                self.page.locator("button:has-text('Consent')").click()
        except:
            # go further if no banner
            pass
        self.page.get_by_role("link", name=" Signup / Login").click()
        loginPage = LoginPage(self.page)
        return loginPage