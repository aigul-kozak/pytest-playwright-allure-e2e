import pytest
import os
import allure
import base64
from allure_commons.types import AttachmentType as BaseAttachmentType
from enum import Enum


def pytest_addoption(parser):
    parser.addoption(
        "--url_name",
        action="store",
        default="https://www.automationexercise.com/",
        help="Base URL for the tests",
    )
    parser.addoption(
        "--browser_name",
        action="store",
        default="chromium",
        help="Choose browser: chromium, firefox, webkit"
    )

@pytest.fixture()
def user_credentials(request):
    """Fixture to parametrize user data"""
    return request.param

@pytest.fixture()
def browserInstance(playwright, request):
    """
    Launch browser sequentially (one at a time) with Allure tracing.
    Browser can now be selected via CLI option.
    """
    # Get browser name from CLI option
    browser_name = request.config.getoption("browser_name")
    url_name = request.config.getoption("url_name")

    # Reflect browser in Allure report
    allure.dynamic.parameter("browser", browser_name)

    # Launch the browser
    browser = getattr(playwright, browser_name).launch(headless=False)

    # Create context and start tracing
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    # Open a new page
    page = context.new_page()
    # page.goto(url_name)  # Uncomment to navigate immediately

    yield page

    # --- After test teardown ---
    os.makedirs("test-results", exist_ok=True)
    trace_path = f"test-results/trace-{request.node.name}-{browser_name}.zip"

    # Stop tracing and save file
    context.tracing.stop(path=trace_path)

    # Attach tracing file to Allure report
    with open(trace_path, "rb") as trace_file:
        data = trace_file.read()
        allure.attach(
            data,
            name=f"trace-{browser_name}",
            attachment_type="application/zip"  # строкой вместо Enum
        )

    # Close context and browser
    context.close()
    browser.close()
