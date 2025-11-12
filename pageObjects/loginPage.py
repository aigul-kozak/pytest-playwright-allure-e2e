from pytest_playwright.pytest_playwright import page

from pageObjects.signUpPage import SignUpPage
from pageObjects.homePage import HomePage
import pytest
from pytest_playwright.pytest_playwright import page
import json

class LoginPage:
    def __init__(self,page):
        self.page = page

    def name(self, user_credentials):
        self.page.locator("form:has-text('Signup')").get_by_placeholder("Name").fill(user_credentials["userName"])
        self.page.locator("form:has-text('Signup')").get_by_placeholder("Email Address").fill(user_credentials["userEmail"])
        self.page.get_by_role("button", name="Signup").click()
        signUpPage = SignUpPage(self.page)
        return signUpPage
    def login(self, user_credentials):
        self.page.locator("form:has-text('Login')").get_by_placeholder("Email Address").fill(user_credentials["userEmail"])
        self.page.locator("form:has-text('Login')").get_by_placeholder("Password").fill(user_credentials["userPassword"])
        self.page.get_by_role("button", name="Login").click()
        homePage = HomePage(self.page)
        return homePage
    def invalid_login(self, invalid_credentials):
        self.page.locator("form:has-text('Login')").get_by_placeholder("Email Address").fill(invalid_credentials["userEmail"])
        self.page.locator("form:has-text('Login')").get_by_placeholder("Password").fill(invalid_credentials["userPassword"])
        self.page.get_by_role("button", name="Login").click()
    def invalid_signup(self,user_credentials):
        self.page.locator("form:has-text('Signup')").get_by_placeholder("Name").fill(user_credentials["userName"])
        self.page.locator("form:has-text('Signup')").get_by_placeholder("Email Address").fill(user_credentials["userEmail"])
        self.page.get_by_role("button", name="Signup").click()
    def valid_login(self,user_credentials):
        self.page.locator("form:has-text('Login')").get_by_placeholder("Email Address").fill(user_credentials["userEmail"])
        self.page.locator("form:has-text('Login')").get_by_placeholder("Password").fill(user_credentials["userPassword"])
        self.page.get_by_role("button", name="Login").click()
        home_page = HomePage(self.page)
        return home_page





