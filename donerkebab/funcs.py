from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.common.exceptions import InvalidArgumentException
from logger import *
from halo import Halo

class Spinner(Halo):
    def __init__(self, text):
        super().__init__(text=text ,enabled=True)
    def __exit__(self, type, value, traceback):
        """Stops the spinner. For use in context managers."""
        if (traceback):
            self.fail()
        else:
            self.succeed()

# class Timeout(Spinner):
#     time_passed = 0
#     timeout = 0

#     def __init__(self, text, timeout):
#         super().__init__(text=text)
#         self.timeout = timeout
#         self.time_passed = 0
#     def render(self):
#         self.time_passed += 0.001 * self._interval;

#         print(str(self.timeout - self.time_passed))
#         super().render()

# def webdriver_wait_spinner(driver, text, spinner, timeout, start_time):
#     timestr = str(time.time() - start_time) + 's'
    
#     spinner.text = f"{text} {timestr}"


class Driver:
    """Base wrapper class for selenium WebDriver"""

    d = None

    @property
    def title(self):
        """The page title that writes on top of the tab"""
        return self.d.title

    @property
    def current_url(self):
        """Gets currently open url"""
        return self.d.current_url

    def back(self):
        """Pressing the browser's back button:"""
        log('Pressed browser back button')
        self.d.back()

    def forward(self):
        """Pressing the browser's forward button:"""
        log('Pressed browser forward button')
        self.d.forward()

    def refresh(self):
        """Pressing the browser's refresh button:"""
        log('Pressed browser refresh button')
        self.d.refresh()

    def __init__(self, driver):
        self.d = driver
    
    def open(self, url:str):
        """Opens a url, url must start with 'https://' or 'http://'"""
        with Spinner(f"Opening {url}") as spinner:
            if not url.startswith('https://') and not url.startswith('http://'):
                raise ValueError("Url must start with https:// or http://")

            self.d.get(url)

    def quit(self):
        """Closes the browser"""
        with Spinner("Quitting"):
            self.d.quit()

    def _timeout_wrapper(self, text, timeout, spinner, condition):
        wait = WebDriverWait(self.d, timeout, 0.2)

        start_time = time.time()

        def wrapper(driver):
            time_left = round(timeout - (time.time() - start_time), 2)
            spinner.text = f"{text}, timeout in {time_left}s"
            return condition()
            # return expected_conditions.alert_is_present()

        return wait.until(wrapper, 'Waiting for alert timed out!')
    

    def wait_for_alert(self, timeout) -> str:
        """Waits until an alert is present, returs text inside the alert"""
        with Spinner() as spinner:
            alert = self._timeout_wrapper(timeout, "Waiting for alert", spinner, expected_conditions.alert_is_present())

            return alert
       
    def set_window_size(self, width, height):
        """Sets browser window size in pixels"""
        try:
            self.d.set_window_size(width, height)
        except InvalidArgumentException as e:
            raise ValueError('width and height must be positive integers')

    """Sets browser position in pixels"""
    def set_window_position(self, x_pos, y_pos):
        try:
            self.d.set_window_position(x_pos, y_pos)
        except InvalidArgumentException as e:
            raise ValueError('x_pos and y_pos must be integers')
        


def NewFirefoxDriver(headless:bool=False,
                    page_load_strategy='normal',
                    width:int=None,
                    height:int=None,
                    x_pos:int=None,
                    y_pos:int=None
                    ):
    if page_load_strategy not in ['normal', 'eager', 'none']:
        raise ValueError("page_load_strategy can only be 'normal', 'eager' or 'none'\n"
                        "for reference: https://www.selenium.dev/documentation/webdriver/capabilities/shared/#pageloadstrategy")
    
    options = FirefoxOptions()

    options.page_load_strategy = page_load_strategy
    options.headless = headless

    d = webdriver.Firefox(options=options)

    driver = Driver(d)

    if width and height:
        driver.set_window_size(width, height)

    if x_pos and y_pos:
        driver.set_window_position(x_pos, y_pos)


    return driver


driver = NewFirefoxDriver(headless=False, height=20, width=20, x_pos=1000, y_pos=10)

driver.wait_for_alert(10)

# driver.forward()

# driver.back()

# driver.open('https://www.google.com')


driver.quit()

