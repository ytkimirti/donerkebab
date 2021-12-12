from donerkebab import Keys
import time


# with Spinner("asdf"):
#     time.sleep()

print(Keys.F1)
# driver = NewFirefoxDriver(headless=True)

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

def test_chromedriver():
    options = ChromeOptions()

    options.headless = False

    driver = webdriver.Chrome(options=options)

    driver.get("https://google.com")

    time.sleep(5)
    driver.quit()

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
    
    inp = driver.get_element('select[name="trivia_category"]')

    driver.set_select_value(inp, '11')
    inp.submit()

    time.sleep(10)
    
# try:
#     test_google()
# finally:
#     driver.quit()