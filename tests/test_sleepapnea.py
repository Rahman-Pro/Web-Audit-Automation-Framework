import pytest

def test_check_title(driver):
    driver.get("https://sleepapneabd.com")
    assert "Sleep" in driver.title
    print("Test Passed!")
