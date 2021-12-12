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

def InitDriver(OptionsFunc, InitFunc, log=True, executable_path=None,headless=False, page_load_strategy='normal'):
    # print(f"driver in {executable_path}")
    check_page_load_strategy(page_load_strategy)
    
    options = OptionsFunc()

    options.page_load_strategy = page_load_strategy
    options.headless = headless

    with Spinner(log , "Opening browser"):
        args = {'options':options}
        if (executable_path):
            args['executable_path'] = executable_path

        d = InitFunc(**args)

        driver = Driver(d, log)

    return driver
    
def EdgeDriver(log=True, executable_path=None,headless=False, page_load_strategy='normal'):
    return InitDriver(EdgeOptions, webdriver.Edge, log, executable_path, headless, page_load_strategy)

def OperaDriver(log=True, executable_path=None,headless=False, page_load_strategy='normal'):
    return InitDriver(OperaOptions, webdriver.Opera, log, executable_path, headless, page_load_strategy)

def SafariDriver(log=True, executable_path=None,headless=False, page_load_strategy='normal'):
    return InitDriver(SafariOptions, webdriver.Safari, log, executable_path, headless, page_load_strategy)

def FirefoxDriver(log=True, executable_path=None,headless=False, page_load_strategy='normal'):
    return InitDriver(FirefoxOptions, webdriver.Firefox, log, executable_path, headless, page_load_strategy)

def ChromeDriver(log=True, executable_path=None,headless=False, page_load_strategy='normal'):
    return InitDriver(ChromeOptions, webdriver.Chrome, log, executable_path, headless, page_load_strategy)
