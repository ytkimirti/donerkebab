from typing import List
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
from keys import Keys


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

    @property
    def action(self):
        """Returns a `webdriver.ActionChains(driver)` for you to chain up functions
        
        example:
        ```python
        # Performs CTRL + A to select whole text
        driver.action.key_down(Keys.CONTROL).send_keys("a").perform()

        # Enters text "qwerty" with keyDown SHIFT key and after keyUp SHIFT key (QWERTYqwerty)
        driver.action.key_down(Keys.SHIFT).send_keys_to_element(search, "qwerty").key_up(Keys.SHIFT).send_keys("qwerty").perform()
        ```
        """
        return webdriver.ActionChains(self.d)

    def execute(self, javascipt_code, *arguments):
        """Executes javascript inside browser

        Example:
        ```python
        # Can accept arguments ie. execute(script, arg1, arg2, arg3...)
        driver.execute("console.log('Hello ' + arguments[0])", "World")

        #Returns the value
        driver.execute("return 'Hello World'") # Hello World
        ```
        """
        with Spinner('Executing javascript'):
            return self.d.execute_script(javascipt_code, *arguments)

    def scroll_to_element(self, element):
        
        self.d.execute_script("arguments[0].scrollIntoView(true);", element)

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

    def get_element_by_xpath(self, xpath):
        """Searches for an element by its xpath 
        
        Waits until timeout runs out or element is found, returns `None` on timeout
        """

        ec = expected_conditions.presence_of_element_located([By.XPATH, xpath])

        return self._timeout_wrapper(f"Getting element '{xpath}'", f"Element '{xpath}' not found",self.timeout, ec)

    def get_element(self, css_selector):
        """Searches for an element by [it's css selector](https://www.w3schools.com/cssref/css_selectors.asp)
        
        Waits until timeout runs out or element is found, returns `None` on timeout
        """

        ec = expected_conditions.presence_of_element_located([By.CSS_SELECTOR, css_selector])

        return self._timeout_wrapper(f"Getting element '{css_selector}'", f"Element '{css_selector}' not found",self.timeout, ec)

    def get_element_multiple_attempts(self, *css_selectors:str):
        """Calls get_element function with multiple css selectors. If one fails, tries the seconds one

        Example:
        ```python
        driver.get_elements_multiple_attempts('div > center', 'div center')

        # is equal to

        for selector in ['div > center', 'div center']:
            return_value = driver.get_element(selector)

            if (return_value is not None):
                return return_value
        ```
        """
        for selector in css_selectors:
            return_value = self.get_element(selector)

            if (return_value is not None):
                return return_value
    
    def get_elements(self, css_selector):
        """Searches for elements by [their css selector](https://www.w3schools.com/cssref/css_selectors.asp)
        
        Waits until timeout runs out or elements are found, returns `None` on timeout
        """

        ec = expected_conditions.presence_of_all_elements_located([By.CSS_SELECTOR, css_selector])

        return self._timeout_wrapper(f"Getting elements with selector '{css_selector}'", f"No element found with '{css_selector}'",self.timeout, ec)

    def get_element_in_parent(self, parent_element, css_selector):
        """Searches for an element inside a parent_element by [it's css selector](https://www.w3schools.com/cssref/css_selectors.asp)
        
        Waits until timeout runs out or element is found, returns `None` on timeout
        """

        def callback_func(driver):
            return parent_element.find_element(By.CSS_SELECTOR, css_selector)

        ec = callback_func

        return self._timeout_wrapper(f"Getting element '{css_selector}' inside parent", f"Child element with '{css_selector}' not found",self.timeout, ec)

    def is_element_present(self, css_selector):
        """Instantly looks if an element is present ignoring timeouts [it's css selector](https://www.w3schools.com/cssref/css_selectors.asp)
    
        Returns the element or None if its not present
        """

        try: 
            return self.d.find_element(By.CSS_SELECTOR, css_selector)
        except:
            return None

    def get_elements_in_parent(self, parent_element, css_selector):
        """Searches for elements inside a parent_element by [it's css selector](https://www.w3schools.com/cssref/css_selectors.asp)
        
        Waits until timeout runs out or element is found, returns `None` on timeout
        """

        def callback_func(driver):
            return parent_element.find_elements(By.CSS_SELECTOR, css_selector)

        ec = callback_func

        return self._timeout_wrapper(f"Getting elements '{css_selector}' inside parent", "No matching child element found",self.timeout, ec)

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

driver = NewFirefoxDriver(headless=False)

def test_execute():
    driver.execute("console.log('Hello World!!')", 'arg1')

    print(driver.execute('return 23'))
    print(driver.execute("return {a: 20, b: 'mehmet'}"))

def test_driver():
    global driver
    # driver.forward()

    # driver.back()

    driver.open('https://www.npmjs.com/')

    driver.set_timeout(0)

    driver.get_alert()

    driver.set_timeout(3)

    e_center = driver.get_element('main')

    h1s = driver.get_elements_in_parent(e_center, 'h1')

    h2s = driver.get_elements_in_parent(e_center, 'h2')

    print("Printing H1's")
    [print(x.text) for x in h1s]
    print('\n\n')
    print("Printing H2's")
    [print(x.text) for x in h2s]
    # breakpoint()

    # e_h2 = driver.d.find_element(By.XPATH,'/html/body/div/div/div[2]/main/div/article/section[1]/div/h1')

    driver.quit()

def test_python():
    driver.open('https://www.python.org/')

    menu = driver.get_element('a[href="/downloads/"]')
    
    driver.action.move_to_element(menu).perform()

    submenu = driver.get_element('a[href="/downloads/source/"]')

    driver.action.move_to_element(submenu).click().perform()

    # driver.action.move_to_element(menu).move_to_element(submenu).click().perform()

    time.sleep(10)

def test_google():
    driver.open('https://google.com')

    driver.get_element('input').send_keys('Weather' + Keys.ESCAPE)

    time.sleep(2)

    driver.get_element('div center input').click()

    result_count = driver.get_element('div#result-stats').text

    print(f"Result count: {result_count}")

    driver.set_timeout(2)

    degrees_span = driver.get_element_multiple_attempts('non_working','non_working2', 'span#wob_tm.wob_t', 'div > div > div > span')

    print(f"Currently its {degrees_span.text} degrees")


def test_stackoverflow():

    driver.open('https://stackoverflow.com/questions/3401343/scroll-element-into-view-with-selenium')

    links = driver.get_elements('div.user-details > a[href^="/users"]')

    user = next(element for element in links if element.text == "DevDave")

    driver.scroll_to_element(user)

    time.sleep(10)

def test_form():
    driver.open('https://opentdb.com/api_config.php')

    inp = driver.get_element('input#trivia_amount')

    inp.clear()
    inp.send_keys('30')
    inp.submit()

    time.sleep(10)
    

try:
    test_form()
finally:
    driver.quit()

