# -*- coding: utf-8 -*-
#start BrowserStackLocal ./BrowserStackLocal MDKicy4nya2192zewKpz
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

desired_cap = {'os': 'Mac', 'os_version': 'Sierra', 'browser': 'Chrome', 'browser_version': '57.0' }

desired_cap['browserstack.local'] = True
desired_cap['browserstack.localIdentifier'] = 'TestSun'

browser = webdriver.Remote(
                          command_executor='http://scottmarrtick1:V4rusztksgxGNLXszMGG@hub.browserstack.com:80/wd/hub',
                          desired_capabilities=DesiredCapabilities.FIREFOX)

#runs with either Firefox or Chrome
#browser = webdriver.Chrome("/Users/nickmaschinski/Desktop/chromedriver")  #V49.0.2623.112
#browser = webdriver.Firefox()  #V30.0
#browser.maximize_window()
browser.get("http://www.bloonaway.co.uk/")
#browser.find_element_by_xpath(".//*[@id='top']/body/div[3]/div/div[1]/div[1]/div/div[2]/a[2]/span").click() #BLOG
browser.get("http://www.bloonaway.co.uk/blog/")
browser.get("http://www.bloonaway.co.uk/prize-draw/")
browser.get("http://www.bloonaway.co.uk/shipping/")
browser.get("http://www.bloonaway.co.uk/privacy-policy/")
browser.get("http://www.bloonaway.co.uk/about-us/")
browser.get("http://www.bloonaway.co.uk/contacts/")
browser.get("http://www.bloonaway.co.uk/testimonials/")
browser.get("http://www.bloonaway.co.uk/guarantee/")
browser.get("http://www.bloonaway.co.uk/cashback/")
browser.quit()
