from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.common.exceptions import InvalidArgumentException, TimeoutException
from logger import *
from halo import Halo

class Spinner(Halo):
    def __init__(self, text='', autofail=True):
        super().__init__(text=text ,enabled=True)
        self.autofail = autofail

    def __exit__(self, type, value, traceback):
        """Stops the spinner. For use in context managers."""

        if self.autofail: 
            if (traceback):
                self.fail()
            else:
                self.succeed()
        return super().__exit__(type, value, traceback)


class Driver:
    """Base wrapper class for selenium WebDriver"""

    d = None
    timeout = 20

    def set_timeout(self, timeout):
        """Default: 20 seconds. Gives a TimeoutException when element couldn't be found after this amount of time"""
        self.timeout = timeout

    @property
    def active_element(self):
        """It is used to track (or) find DOM element which has the focus in the current browsing context."""

        return self.d.switch_to.active_element

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

    def _timeout_wrapper(self, text, error_msg, timeout , condition):

        wait = WebDriverWait(self.d, timeout, 0.2)

        start_time = time.time()

        spinner = Spinner(text, autofail=False)
        spinner.start()

        def wrapper(driver):
            time_left = round(timeout - (time.time() - start_time), 2)
            time_left_str = f", timeout in {time_left}s"
            if (time_left < timeout / 2):
                spinner.text = text + time_left_str
            else:
                spinner.text = text;
            return condition(driver)
            # return expected_conditions.alert_is_present()
        
        try:
            return_val = wait.until(wrapper)
            spinner.succeed()
            return return_val
        except:
            spinner.text = error_msg
            spinner.fail()

    def get_alert(self):
        """Waits until an alert is present, returs alert. If no `alert` is found, returns `None` https://www.selenium.dev/documentation/webdriver/browser/alerts/#confirm"""

        # if (self.timeout == 0):
        #     try: 
        #         return self.d.switch_to.alert
        #     except:
        #         return None
        return self._timeout_wrapper("Waiting for alert", "No alert found",self.timeout, expected_conditions.alert_is_present())



    def get_element(self, css_selector):
        """Searches for an element by [it's css selector](https://www.w3schools.com/cssref/css_selectors.asp)
        
        Waits until timeout runs out or element is found, returns `None` on timeout
        """

        ec = expected_conditions.presence_of_element_located([By.CSS_SELECTOR, css_selector])

        return self._timeout_wrapper(f"Getting element '{css_selector}'", "Element not found",self.timeout, ec)
    
    def get_element_in_child(self, parent_element, css_selector):
        """Searches for an element inside a parent_element by [it's css selector](https://www.w3schools.com/cssref/css_selectors.asp)
        
        Waits until timeout runs out or element is found, returns `None` on timeout
        """

        def callback_func(driver):
            return parent_element.find_element(By.CSS_SELECTOR, css_selector)

        ec = callback_func

        return self._timeout_wrapper(f"Getting element '{css_selector}' inside parent", "Child element not found",self.timeout, ec)

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

def test_driver():
    global driver
    # driver.forward()

    # driver.back()

    driver.open('https://www.npmjs.com/')

    driver.set_timeout(0)

    driver.get_alert()

    driver.set_timeout(3)

    e_center = driver.get_element('section.f7728d4c')

    # e_h2 = driver.d.find_element(By.XPATH,'/html/body/div/div/div[2]/main/div/article/section[1]/div/h1')

    print(e_h2)
    print(e_h2.text)

    driver.quit()

try:
    test_driver()
finally:
    driver.quit()

