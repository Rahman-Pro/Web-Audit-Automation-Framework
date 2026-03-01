import pytest
from selenium.webdriver.common.by import By

def test_check_images_loading(driver, screenshot):
    driver.get("https://sleepapneabd.com")
    images = driver.find_elements(By.TAG_NAME, "img")
    print(f"Total images found: {len(images)}")

    for img in images:
        is_loaded = driver.execute_script(
            "return arguments[0].complete && typeof arguments[0].naturalWidth != \"undefined\" && arguments[0].naturalWidth > 0",
            img
        )
        assert is_loaded is True, f"Image not loaded: {img.get_attribute('src')}"

    print("? All images loaded successfully!")
    screenshot("images_load_check")
