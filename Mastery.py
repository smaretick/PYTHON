# -*- coding: utf-8 -*-
#start BrowserStackLocal ./BrowserStackLocal --key MDKicy4nya2192zewKpz
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import unittest, time, re

desired_cap = {'browser': 'Chrome','browser_version': '80.0','os': 'OS X','os_version': 'High Sierra','project': 'MASTERY','browserstack.debug': 'true', 'resolution': '1600x1200'}

#desired_cap = {'browser': 'Firefox','browser_version': '62.0 beta','os': 'OS X','os_version': 'High #Sierra','project': #'MASTERY','browserstack.debug': 'true'}

browser = webdriver.Remote(
    command_executor='http://scottmaretick2:MDKicy4nya2192zewKpz@hub.browserstack.com:80/wd/hub', desired_capabilities= desired_cap)


#runs with either Firefox or Chrome
#CHROME
#options = webdriver.ChromeOptions()
#options.add_argument('headless')
#options.add_argument('window-size= 1360 x 1400')
#browser = webdriver.Chrome("/Users/scottmaretick/Desktop/chromedriver"),chrome_options=options;)
#browser = webdriver.Chrome("/Users/scottmaretick/Desktop/chromedriver")
#print(browser.get_window_size())
#browser.set_window_size(1360, 800) #fits my second monitor
#print(browser.get_window_size())
#browser = webdriver.Firefox()  
#browser.maximize_window()
browser.get("https://www.mastery.net/")
time.sleep(30)
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot1.png');
#PAGING DOWN MAIN PAGE START
#browser.execute_script("window.scrollTo(0,600);")
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot2.png');
browser.execute_script("window.scrollTo(600,900);")
time.sleep(10)
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot3.png');
browser.execute_script("window.scrollTo(900,1500);") #MASTERY TEAM
time.sleep(10)
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot4.png');
browser.execute_script("window.scrollTo(1500,2400);") #WE'RE HIRING
time.sleep(10)

#BACKEND ENGINEER
browser.find_element_by_css_selector("div.careers-item:nth-child(1) > a:nth-child(1)").click()
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot5.png');
time.sleep(10)
browser.execute_script("window.scrollTo(200,600);")
time.sleep(10)
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot6.png');
browser.execute_script("window.scrollTo(600,900);")
time.sleep(10) 
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot7.png');
browser.back() #BACK TO WE'RE HIRING
time.sleep(10)

#FRONTEND ENGINEER
browser.find_element_by_css_selector("div.careers-item:nth-child(2) > a:nth-child(1)").click()
time.sleep(10)
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot6.png'); 
browser.execute_script("window.scrollTo(200,600);")
time.sleep(10)
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot6.png');
browser.execute_script("window.scrollTo(600,900);") 
time.sleep(10)
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot7.png');
browser.back() #BACK TO WE'RE HIRING
time.sleep(10)

#MOBILE ENGINEER
browser.find_element_by_css_selector("div.careers-item:nth-child(3) > a:nth-child(1)").click() 
time.sleep(10)
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot8.png');
browser.execute_script("window.scrollTo(200,600);")
time.sleep(10)
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot9.png');
browser.execute_script("window.scrollTo(600,900);") 
time.sleep(10)
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot10.png');
browser.back() #BACK TO WE'RE HIRING
time.sleep(10)

#CLIENT SERVICES
browser.find_element_by_css_selector("div.careers-item:nth-child(4) > a:nth-child(1)").click()
time.sleep(10)
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot11.png'); 
browser.execute_script("window.scrollTo(200,600);")
time.sleep(10)
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot12.png');
browser.back()
time.sleep(10)

#QA
browser.find_element_by_css_selector("div.careers-item:nth-child(5) > a:nth-child(1)").click() 
time.sleep(10)
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot13.png');
browser.execute_script("window.scrollTo(200,600);")
time.sleep(10)
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot14.png');
browser.execute_script("window.scrollTo(600,900);") 
time.sleep(10)
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot15.png');
browser.execute_script("window.scrollTo(900,1200);")
time.sleep(10)
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot16.png');
browser.execute_script("window.scrollTo(1200,1800);")
time.sleep(10)
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot17.png');
browser.back()
time.sleep(10)

#DATA SCIENCES
browser.find_element_by_css_selector("div.careers-item:nth-child(6) > a:nth-child(1)").click() 
time.sleep(10)
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot16.png');
browser.execute_script("window.scrollTo(200,600);")
time.sleep(10)
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot17.png');
browser.back()
time.sleep(10)

#PEOPLE TEAM
browser.find_element_by_css_selector("div.careers-item:nth-child(7) > a:nth-child(1)").click()
time.sleep(10)
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot18.png'); 
browser.execute_script("window.scrollTo(200,600);")
time.sleep(10)
browser.back()
time.sleep(10)

#GENERAL INTEREST
browser.find_element_by_css_selector("div.careers-item:nth-child(8) > a:nth-child(1)").click() 
time.sleep(10)
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot19.png');
browser.execute_script("window.scrollTo(200,600);")
time.sleep(10)
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot20.png');
browser.back()
time.sleep(10)

browser.execute_script("window.scrollTo(2400,2600);") #BOTTOM OF PAGE
time.sleep(10)
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot14.png');	
#PAGING DOWN MAIN PAGE END
print browser.title

#SEE ALL OPENINGS
browser.find_element_by_css_selector("html body section#careers.careers.bg-full-black.paragraph div.container-1200 div.careers-inner div.button a").click()
time.sleep(10)
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot15.png');
browser.execute_script("window.scrollTo(200,600);")
time.sleep(10)
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot16.png');
browser.execute_script("window.scrollTo(600,900);")
time.sleep(10)
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot17.png');
browser.execute_script("window.scrollTo(900,1200);")
time.sleep(10)
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot18.png');
browser.back()
time.sleep(10)

browser.execute_script("window.scrollTo(0,600);") #BACK TO TOP OF PAGE
time.sleep(10)

browser.find_element_by_css_selector(".menu > a:nth-child(1)").click() #PRODUCT 
time.sleep(10)
print browser.title
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot19.png');
browser.find_element_by_css_selector(".menu > a:nth-child(2)").click() #THE TEAM
time.sleep(10)
print browser.title
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot20.png');
browser.find_element_by_css_selector(".menu > a:nth-child(3)").click() #CAREERS
time.sleep(10)
browser.execute_script("window.scrollTo(2400,2600);") #BOTTOM OF CAREERS PAGE
time.sleep(10)
print browser.title
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot17.png');
browser.find_element_by_css_selector(".menu > a:nth-child(3)").click() #GET IN TOUCH
time.sleep(10)
print browser.title
#browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot18.png');
browser.quit()
