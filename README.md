# Test md file

## Element methods
```python



driver = NewFirefoxDriver()

driver.open('https://www.google.com')

input_element = driver.get_element('input')

# None of the element methods are modified
# You can look at the official selenium documentation
# https://www.selenium.dev/documentation/webdriver/actions_api/keyboard/#sendkeys

# Writes hello world inside input_element
input_element.send_keys('Hello world')

# clears out the text inside input_element
input_element.clear() 


```