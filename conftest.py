import pytest
from selenium import webdriver
import os

@pytest.fixture
def driver():
    # Create Chrome driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def screenshot(driver):
    # Create screenshots directory if it doesn't exist
    os.makedirs("screenshots", exist_ok=True)
    
    def _screenshot(name):
        driver.save_screenshot(f"screenshots/{name}.png")
    
    return _screenshot
