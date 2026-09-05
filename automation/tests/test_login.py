import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.login_page import LoginPage


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()


def test_login_page_loads(driver):
    base_url = os.getenv("BASE_URL", "http://localhost:3000")
    page = LoginPage(driver)
    page.open(base_url)
    assert "/login" in driver.current_url


@pytest.mark.skip(reason="Requires valid test credentials and a running target application")
def test_valid_login(driver):
    base_url = os.getenv("BASE_URL", "http://localhost:3000")
    page = LoginPage(driver)
    page.open(base_url)
    page.login(os.environ["TEST_EMAIL"], os.environ["TEST_PASSWORD"])
    assert "/login" not in driver.current_url
