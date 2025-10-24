from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

GRID_URL = "http://localhost:4444/wd/hub"

def test_amazon(browser):
    print(f"\n🚀 Starting test on {browser} browser...")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
    else:
        print("❌ Unsupported browser")
        return

    driver = webdriver.Remote(command_executor=GRID_URL, options=options)
    driver.get("https://www.amazon.in/")
    driver.maximize_window()
    time.sleep(3)

    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys("headphones")
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)

    print(f"✅ {browser} test completed successfully on Amazon.")
    driver.quit()

for browser in ["chrome", "firefox"]:
    test_amazon(browser)
