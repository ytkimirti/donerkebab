import sys

print(sys.path)

sys.path.insert(0, '/Users/ytkimirti/Projects/python/donerkebab')

from donerkebab import Keys, NewFirefoxDriver, NewChromeDriver

driver = NewChromeDriver(log=True, headless=False)

driver.open('https://github.com')

driver.get_element('div')

driver.sleep(5)

driver.quit()

