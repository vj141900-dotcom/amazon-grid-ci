import pytest
from selenium import webdriver

GRID_URL = "http://localhost:4444/wd/hub"

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = request.param
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        driver = webdriver.Remote(command_executor=GRID_URL, options=options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Remote(command_executor=GRID_URL, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
