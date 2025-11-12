import pytest
from pytest_playwright.pytest_playwright import page
import json

class SignUpPage:
    def __init__(self,page):
        self.page = page

    def fill_signup_form(self, user_credentials):
        self.page.evaluate("""
            () => {
                const ad = document.querySelector('div.grippy-host');
                if (ad) { ad.style.display = 'none'; }
            }
            """)
        self.page.get_by_role('radio', name="Mrs").check()
        #self.page.locator("#name").fill(user_credentials["userName"])
        #self.page.locator("#email").fill(user_credentials["userEmail"])
        self.page.locator("#password").fill(user_credentials["userPassword"])

        if self.page.locator('path[d="M10,26 L10,6 A6,6 0 0,1 16,1 L60,1 A6,6 0 0,1 66,6 L66,20 66,26 Z"]').is_visible():
            self.page.locator('path[d="M10,26 L10,6 A6,6 0 0,1 16,1 L60,1 A6,6 0 0,1 66,6 L66,20 66,26 Z"]').click()

        self.page.locator("#days").select_option("1")
        self.page.locator("#months").select_option("1")
        self.page.locator("#years").select_option("2000")
        self.page.get_by_role("checkbox", name="Receive special offers from our partners!").check()
        self.page.locator("#first_name").fill(user_credentials["userFirstName"])
        self.page.locator("#last_name").fill(user_credentials["userLastName"])
        self.page.locator("#address1").fill(user_credentials["userAddress"])
        self.page.get_by_role("combobox", name="country").select_option("Canada")
        self.page.locator("#state").fill(user_credentials["userState"])
        self.page.locator("#city").fill(user_credentials["userCity"])
        self.page.locator("#zipcode").fill(user_credentials["userZipCode"])
        self.page.locator("#mobile_number").fill(user_credentials["userMobile"])
        self.page.get_by_role("button", name="Create Account").click()
        from pageObjects.accountCreatedPage import AccountCreatedPage
        accountCreatedPage = AccountCreatedPage(self.page)
        return accountCreatedPage






