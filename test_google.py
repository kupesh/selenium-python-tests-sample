import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_google_search(browser):
    browser.get("https://www.google.com")
    search_box = browser.find_element(By.NAME, "q")
    search_box.send_keys("Selenium Python")
    search_box.submit()
    assert "Selenium" in browser.title
