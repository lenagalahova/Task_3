import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from config import URL



def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Выбор браузера: chrome или firefox")

@pytest.fixture(params=["chrome", "firefox"], scope="function")
def driver(request):
    browser = request.param
    
    if browser == "chrome":
        options = ChromeOptions()
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
       raise ValueError(f"Неподдерживаемый браузер: {browser}")
    
    driver.maximize_window()
    driver.get(URL)
    yield driver
    driver.quit()
