import selenium
from selenium import webdriver

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.opera.options import Options as OperaOptions
from selenium.webdriver.safari.options import Options as SafariOptions

from ._spinner import Spinner
from .driver import Driver

def check_page_load_strategy(page_load_strategy):
    if page_load_strategy not in ['normal', 'eager', 'none']:
        raise ValueError("page_load_strategy can only be 'normal', 'eager' or 'none'\n"
                        "for reference: https://www.selenium.dev/documentation/webdriver/capabilities/shared/#pageloadstrategy")

def NewSafariDriver(log=True, headless=False, page_load_strategy='normal'):
    check_page_load_strategy(page_load_strategy)
    
    options = SafariOptions()

    options.page_load_strategy = page_load_strategy
    options.headless = headless

    with Spinner(log ,"Initing browser"):
        d = webdriver.Safari(options=options)
        driver = Driver(d, log)

    return driver
def NewOperaDriver(log=True, headless=False, page_load_strategy='normal'):
    check_page_load_strategy(page_load_strategy)
    
    options = OperaOptions()

    options.page_load_strategy = page_load_strategy
    options.headless = headless

    with Spinner(log ,"Initing browser"):
        d = webdriver.Opera(options=options)
        driver = Driver(d, log)

    return driver
def NewEdgeDriver(log=True, headless=False, page_load_strategy='normal'):
    check_page_load_strategy(page_load_strategy)
    
    options = EdgeOptions()

    options.page_load_strategy = page_load_strategy
    options.headless = headless

    with Spinner(log ,"Initing browser"):
        d = webdriver.Edge(options=options)
        driver = Driver(d, log)

    return driver
def NewFirefoxDriver(log=True, headless=False, page_load_strategy='normal'):
    check_page_load_strategy(page_load_strategy)
    
    options = FirefoxOptions()

    options.page_load_strategy = page_load_strategy
    options.headless = headless

    with Spinner(log ,"Initing browser"):
        d = webdriver.Firefox(options=options)
        driver = Driver(d, log)

    return driver
def NewChromeDriver(log=True, headless=False, page_load_strategy='normal'):
    check_page_load_strategy(page_load_strategy)
    
    options = ChromeOptions()

    options.page_load_strategy = page_load_strategy
    options.headless = headless

    with Spinner(log ,"Initing browser"):
        d = webdriver.Chrome(options=options)
        driver = Driver(d, log)

    return driver
