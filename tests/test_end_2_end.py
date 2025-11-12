import allure
from pathlib import Path
import json
import pytest
from playwright.sync_api import Page, expect, Playwright

from pageObjects.accountDeletedPage import AccountDeletedPage
from pageObjects.createUser import CreateUser
from pageObjects.loginPage import LoginPage
from pageObjects.signUpPage import SignUpPage
from pageObjects.homePage import HomePage
from pageObjects.accountCreatedPage import AccountCreatedPage
import os



BASE_DIR = Path(__file__).resolve().parent.parent  # 2 levels up : tests -> route
DATA_DIR = BASE_DIR / "data"

with open(DATA_DIR /'credentials.json') as f:
    user_credentials = json.load(f)['user_credentials']

with open(DATA_DIR /'invalid_credentials.json') as f:
    invalid_user_credentials = json.load(f)['invalid_user_credentials']

@pytest.mark.parametrize("credentials",user_credentials,ids=lambda x: f"user_{x['userEmail']}")
@pytest.mark.parametrize("invalid_credentials",invalid_user_credentials,ids=lambda x: f"invalid_{x['userEmail']}")
def test_user_flow(playwright:Playwright, browser_name, credentials, invalid_credentials):
    headless_mode = os.getenv("HEADLESS", "true").lower() == "true"
    browser = getattr(playwright, browser_name).launch(headless=headless_mode)
    page = browser.new_page()
    # Navigate to Create User page
    with allure.step("Navigate to Create User page"):
        createUserPage = CreateUser(page)
        createUserPage.navigate()
    # Sign up user
    with allure.step(f"Sign up user: {credentials}"):
        loginPage = createUserPage.signup()
        loginPage.name(credentials)
        signUpPage = SignUpPage(page)
        click_continue = signUpPage.fill_signup_form(credentials)
        homePage = click_continue.click_continue()
    # Logout user
    with allure.step("Logout user"):
        homePage.logout()
    # Login with invalid credentials
    with allure.step(f"Login with invalid credentials: {invalid_credentials}"):
        loginPage = createUserPage.signup()
        loginPage.invalid_login(invalid_credentials)
        allure.attach(loginPage.page.screenshot(), name="invalid_login", attachment_type=allure.attachment_type.PNG)
        expect(loginPage.page.locator("text=Your email or password is incorrect!")).to_be_visible()
    # Attempt to sign up with existing credentials
    with allure.step(f"Attempt to sign up with existing credentials: {credentials}"):
        loginPage.invalid_signup(credentials)
        allure.attach(loginPage.page.screenshot(), name="signup_exists", attachment_type=allure.attachment_type.PNG)
        expect(loginPage.page.locator("text=Email Address already exist!")).to_be_visible()
    # Login valid user
    with allure.step(f"Login valid user: {credentials}"):
        homePage = loginPage.valid_login(credentials)
    # Delete account
    with allure.step("Delete account"):
        deletedPage = homePage.delete()
        allure.attach(deletedPage.page.screenshot(), name="account_deleted", attachment_type=allure.attachment_type.PNG)
        expect(deletedPage.page.locator("text=Account Deleted!")).to_be_visible()
        deletedPage.continue_after_del()

        browser.close()




