from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.remote.webelement import WebElement

class Driver():
    def __getattribute__(self, attr):
        """Prevent accessing inherited attributes"""
        for base in self.__bases__:
            if hasattr(base, attr):
                raise AttributeError

        return object.__getattribute__(self, attr)

def find_wait():
    try:
        driver = webdriver.Firefox()
    except Exception as e:
        # print(e)
        print(f"args={e.args[0]}")
        quit()

    driver.get('https://ytkimirti.github.io/')

    wait = WebDriverWait(driver, 2, 0.1)

    def myFunc(driver):
        print('Trying...')
        return expected_conditions.element_located_to_be_selected(driver.find_element(By.CSS_SELECTOR, '.undertext'))



    #gives TimeoutExeption
    wait.until(myFunc)

    time.sleep(2);

driver = webdriver.Firefox()

driver.get('http://demo.guru99.com/test/newtours/')

inputs = driver.find_elements(By.CSS_SELECTOR, 'input')


a = WebElement(None)

a.

print(inputs)
print([i.name for i in inputs])

driver.quit()