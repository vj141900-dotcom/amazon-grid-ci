from selenium.webdriver.common.by import By
import time

def test_amazon_search(driver):
    driver.get("https://www.amazon.in/")
    driver.find_element(By.ID, "twotabsearchtextbox").send_keys("wireless mouse")
    driver.find_element(By.ID, "nav-search-submit-button").click()
    time.sleep(3)
    assert "wireless mouse" in driver.title.lower()
