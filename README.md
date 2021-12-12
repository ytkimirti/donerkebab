<h1 align='center'>🥙 donerkebab 🥙</h1>
> A super easy to use, beginner friendly [selenium](https://pypi.org/project/selenium/) wrapper


```shell
$ pip install donerkebab
```

## Usage

### 1. Download the driver for your browser
[Chrome](https://chromedriver.chromium.org/downloads)
[Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
[Firefox](https://github.com/mozilla/geckodriver/releases)
[Safari](https://webkit.org/blog/6900/webdriver-support-in-safari-10/)

### 2. Place it in a PATH directory
This might be /usr/bin or the directory as your python script

```py
# Also available for Firefox, Edge, Safari and Opera
from donerkebab import ChromeDriver

# Get an instance of the browser window
# You can easily start it in headless mode too
driver = ChromeDriver(headless=False)

driver.open('https://duckduckgo.com/')

# Browser will wait at max 10 seconds until element is found
driver.set_timeout(10)

# You can find elements by their CSS selectors
input_box = driver.get_element('input#search_form_input_homepage')

# Uses classic selenium element functions
input_box.send_keys('Do pigs fly?')

driver.sleep(2)

submit_button = driver.get_element('input#search_button_homepage')

# Perform the search
submit_button.click()

# Get the container of all the result links
results_container = driver.get_element('div.results--main')

# Get all the links inside the container with a class of 'results__a'
results = driver.get_elements_in_parent(results_container, 'a.result__a')

# Print all the links
print("🔎 Results for 'Do pigs fly?' 🔎")
for result in results:
    # get title and href attribute (the link adress) for every result
    print(result.text + ' -> ' + result.get_attribute('href'))

driver.quit()
```

# API

## Driver init options

```py
driver = FirefoxDriver(log=True, executable_path=None,headless=False, page_load_strategy='normal'):
```
```
headless -> Hides the window and runs the browser in the background. Really usefull
log -> Enable or disable logging
executable_path -> The full path to executable driver. If left null the it will look at the PATH variable to find the driver.
page_load_strategy -> Take a look at the [official docs](https://www.selenium.dev/documentation/webdriver/capabilities/shared/#pageloadstrategy)
```

## Locating elements

### Css selectors

donerkebab always uses css selectors for locating elements. Some examples:

- `input` element with type input
- `div > input` element that is the direct child of input
- `input.search` element with a class of 'search'
- `input#main_button` element with an id of 'main_button'
- `a[href='https://google.com']` link element with a href attribute

Definately check out more [advanced css selectors](https://saucelabs.com/resources/articles/selenium-tips-css-selectors). They come in really handy

### Locator methods

```py
driver.get_element(css_selector)
driver.get_elements(css_selector)
driver.get_element_in_parent(parent_element, css_selector)
driver.get_elements_in_parent(parent_element, css_selector)
driver.get_element_by_xpath(xpath)

driver.is_element_present(css_selector) # Searches for element without any timeout

# Tries the first selector, if none element is found, tries the alternate selector
# Great for having backup selectors for elements that might change
driver.get_element_multiple_attempts(selector1, selector2, selector3...)

# Returns the active element
driver.active_element

# Scrolls that element into view
driver.scroll_to_element(element)

# Waits until an alert is present, and returns that alert
driver.get_alert()
```

### Driver methods

#### open(url)

Opens the url and waits until the page loads. Url must start with https:// or http://
