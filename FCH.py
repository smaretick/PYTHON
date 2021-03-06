# -*- coding: utf-8 -*-
#download gechodriver https://github.com/mozilla/geckodriver/releases
#/usr/local/bin/geckodriver (in PATH)

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
#FIREFOX
#firefox_capabilities = DesiredCapabilities.FIREFOX
#firefox_capabilities['marionette'] = True
#firefox_capabilities['binary'] = '/Volumes/Untitled/Applications/Firefox.app/Contents/MacOS/firefox'
#browser = webdriver.Firefox(capabilities=firefox_capabilities)

#CHROME
browser = webdriver.Chrome("/Users/scottmaretick/Desktop/chromedriver")

browser.get("https://accounts.google.com")
print (browser.title)
browser.save_screenshot('//Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot1.png');
browser.find_element_by_id("Email").clear()
browser.find_element_by_id("Email").send_keys("scottmaretick51@gmail.com")
browser.find_element_by_id("next").click()
browser.save_screenshot('//Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot2.png');
#time.sleep(10);
browser.find_element_by_id("Passwd").clear()
#time.sleep(10);
browser.find_element_by_id("Passwd").send_keys("sm110751")
#time.sleep(10);
browser.find_element_by_id("signIn").click()
browser.save_screenshot('//Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot3.png');
#time.sleep(10);
browser.find_element_by_xpath(".//*[@id='gbwa']/div[1]/a").click()  #Google Apps
browser.save_screenshot('//Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot4.png');
browser.find_element_by_xpath(".//*[@id='gb1']/span[1]").click()    #Search
browser.save_screenshot('//Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot5.png');
print (browser.title)  #Google
#time.sleep(10);
browser.get("https://www.google.com/webhp?ei=kY20WIGxIsLr-AHcyLK4DA&ved=0EKkuCAUoAQ#q=google+analytics&*")
#time.sleep(10);
browser.save_screenshot('//Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot6.png');
print (browser.title) #google analytics - Google Search
browser.get("https://www.google.com/analytics/?gclid=CjwKEAiAuc_FBRD7_JCM3NSY92wSJABbVoxBWL-hCEVIFJ0QbUGvdx4vmJqrR--PdTAOMbwoRL0o6xoCji3w_wcB#?modal_active=none")
#time.sleep(10);
browser.save_screenshot('//Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot7.png');
print (browser.title) #Google Analytics Solutions - Marketing Analytics & Measurement – Google
browser.get("https://analytics.google.com/analytics/web/#report/defaultid/a39099721w75626535p78130152/")
time.sleep(10);
browser.save_screenshot('//Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot8.png');
browser.quit()
