<h1>🥙 donerkebab 🥙</h1>
> A super easy to use, beginner friendly [selenium](https://pypi.org/project/selenium/) wrapper


```shell
$ pip install donerkebab
```

## Usage

```py
# Also available for Firefox, Edge, Safari and Opera
from donerkebab import ChromeDriver

# Get an instance of the browser window
driver = ChromeDriver()

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

## Locating elements

### Css selectors

donerkebab always uses css selectors for locating elements. Some examples:

`input` element with type input
`div > input` element that is the direct child of input
`input.search` element with a class of 'search'
`input#main_button` element with an id of 'main_button'
`a[href='https://google.com']` link element with a href attribute

Definately check out more [advanced css selectors](https://saucelabs.com/resources/articles/selenium-tips-css-selectors). They come in really handy

### Locator methods
``

## API

### Driver init options

```py
driver = FirefoxDriver(log=True, executable_path=None,headless=False, page_load_strategy='normal'):
```
```
log -> Enable or disable logging
executable_path -> The full path to executable driver. If left null the it will look at the PATH variable to find the driver.
page_load_strategy -> Take a look at the [official docs](https://www.selenium.dev/documentation/webdriver/capabilities/shared/#pageloadstrategy)
```

### Driver methods

#### open(url)

Opens the url and waits until the page loads. Url must start with https:// or http://





