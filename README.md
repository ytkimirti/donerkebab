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