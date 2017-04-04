from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#desired_cap = {'os': 'Windows', 'os_version': 'xp', 'browser': 'Chrome', 'browser_version': '48.0' }
#desired_cap = {'os': 'Windows', 'os_version': 'xp', 'browser': 'IE', 'browser_version': '7.0' }
desired_cap = {'os': 'Mac', 'os_version': 'Sierra', 'browser': 'Firefox', 'browser_version': '52.0' }


driver = webdriver.Remote(
                          command_executor='http://scottmarrtick1:V4rusztksgxGNLXszMGG@hub.browserstack.com:80/wd/hub',
                          desired_capabilities=DesiredCapabilities.FIREFOX)


driver.get("http://www.google.com")
if not "Google" in driver.title:
    raise Exception("Unable to load google page!")
elem = driver.find_element_by_name("q")
elem.send_keys("BrowserStack")
elem.submit()
print driver.title
driver.quit()
