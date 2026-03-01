import pytest
from selenium.webdriver.common.by import By
import requests

def test_broken_links(driver):
    driver.get("https://sleepapneabd.com")
    links = driver.find_elements(By.TAG_NAME, "a")
    print(f"Total links found: {len(links)}")

    for link in links:
        url = link.get_attribute("href")
        if url and url.startswith("http"):
            try:
                response = requests.head(url, allow_redirects=True, timeout=5)
                assert response.status_code < 400, f"Broken link: {url} (Status: {response.status_code})"
            except requests.exceptions.RequestException:
                pytest.fail(f"Could not reach URL: {url}")
    
    print("? All links are working!")
