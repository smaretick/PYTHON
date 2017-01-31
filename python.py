# -*- coding: utf-8 -*-
#/usr/local/bin/geckodriver (in PATH)
#I finally got back to this & am now able to use both FireFox & Chrome with Selenium 3 on #my MacBook Air running macOS Sierra (10.12.1). I used FF 50.1.0, Selenium 3, & Python #2.7.10 or Python 3.5.2

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

firefox_capabilities = DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True
firefox_capabilities['binary'] = '/Volumes/Untitled/Applications/Firefox.app/Contents/MacOS/firefox'
browser = webdriver.Firefox(capabilities=firefox_capabilities)
browser.get("https://www.google.com")
browser.quit()