from donerkebab import Keys, NewFirefoxDriver, NewChromeDriver

driver = NewChromeDriver(log=True, headless=False)

driver.open('https://github.com')

driver.get_element('div')

driver.sleep(5)

driver.quit()

