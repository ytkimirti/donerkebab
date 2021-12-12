from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chromium.options import Options as ChromiumOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def check_page_load_strategy(page_load_strategy):
    if page_load_strategy not in ['normal', 'eager', 'none']:
        raise ValueError("page_load_strategy can only be 'normal', 'eager' or 'none'\n"
                        "for reference: https://www.selenium.dev/documentation/webdriver/capabilities/shared/#pageloadstrategy")

def NewFirefoxDriver(headless:bool=False, page_load_strategy='normal'):
    check_page_load_strategy(page_load_strategy)
    
    options = FirefoxOptions()

    options.page_load_strategy = page_load_strategy
    options.headless = headless

    with Spinner("Initing browser"):
        d = webdriver.Firefox(options=options)
        driver = Driver(d)

    return driver
