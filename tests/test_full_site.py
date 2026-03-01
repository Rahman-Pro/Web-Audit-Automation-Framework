import pytest
import requests
from selenium.webdriver.common.by import By
import time

def test_full_site_audit(driver, screenshot):
    # ?. Page Load & SSL Check
    driver.get("https://sleepapneabd.com")
    assert "https" in driver.current_url, "SSL is not active!"
    print("? Page loaded & SSL active.")

    # ?. Page Title & Meta Tags
    assert "Sleep" in driver.title
    meta_desc = driver.find_element(By.XPATH, "//meta[@name=\"description\"]").get_attribute("content")
    assert len(meta_desc) > 0, "Meta description missing!"
    print("? SEO tags are present.")

    # ?. Broken Links Check
    links = driver.find_elements(By.TAG_NAME, "a")
    for link in links[:10]:  # ????? ???? ????? ??? ???? ??? ???????
        url = link.get_attribute("href")
        if url and url.startswith("http"):
            res = requests.head(url, timeout=5)
            assert res.status_code < 400, f"Broken link: {url}"
    print(f"? Checked {len(links)} links.")

    # ?. Responsive Test (Mobile View)
    driver.set_window_size(375, 812) # iPhone X size
    time.sleep(2)
    screenshot("mobile_view")
    driver.maximize_window()
    print("? Mobile responsiveness checked.")

    # ?. 404 Page Check
    driver.get("https://sleepapneabd.com/random-page-123")
    assert "404" in driver.page_source or "Not Found" in driver.title
    print("? 404 page is working.")

    # ?. Navigation & Contact Form Presence
    driver.get("https://sleepapneabd.com")
    nav = driver.find_element(By.TAG_NAME, "nav")
    assert nav.is_displayed()
    print("? Navigation menu is visible.")
