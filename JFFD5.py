# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re, os
###################################################################################################
#--------------------------------------------------------------------------------------------------
#profile = webdriver.FirefoxProfile()
#profile.set_preference("browser.cache.disk.enable", False)
#profile.set_preference("browser.cache.memory.enable", False)
#profile.set_preference("browser.cache.offline.enable", False)
#profile.set_preference("network.http.use-cache", False)
#browser = webdriver.Firefox(profile)
#--------------------------------------------------------------------------------------------------
#FILE/APP INIT######################################################################################
path = os.getcwd()
print ("The current working directory is %s" % path)
print(path)
file_name = "SCREENSHOTS"
completeName = os. path. join(path, file_name)
print(completeName)
#os.mkdir($HOME/Desktop/SCREENSHOTS)
f = open('SeleniumJFFD.txt', 'w')
print ("OPEN FILE")
f.write('OPEN FILE \n')
browser = webdriver.Firefox()  
browser.get("https://www.justfoodfordogs.com/#") #JFFD WEBSITE
time.sleep(15)
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot1a.png')
browser.find_element_by_css_selector("button.affirm:nth-child(4)").click() #COOKIES ACCEPTED
print ("COOKIES ACCEPTED")
f.write('COOKIES ACCEPTED \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot1b.png')
#time.sleep(15)
#####################################################################################################
#Petco- Shorewood####################################################################################
#CSS SELECTOR  .navbar-header-location > a:nth-child(2)
#XPATH /html/body/div[2]/header/nav/div/div[1]/div/div/div/div/div[1]/a
#
#CSS SELECTOR  button.btn:nth-child(3)
#XPATH  /html/body/div[2]/header/nav/div/div[1]/div/div/div/div/div[1]/button
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot1b.png')
#print ("Petco- Shorewood")
#f.write('Petco- Shorewood \n')
#####################################################################################################
#SHIPPING UPDATES#####################################################################################
#CSS SELECTOR  .html-slot-container > div:nth-child(1) > label:nth-child(1) > a:nth-child(1) > span:nth-child(1)
#XPATH  /html/body/div[2]/header/nav/div/div[1]/div/div/div/div/div[2]/div/div/label/a/span
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot1c.png')
#print ("SHIPPING UPDATES")
#f.write('SHIPPING UPDATES \n')
#Vet Portal
#CSS SELECTOR  li.dropdown:nth-child(1) > a:nth-child(1)
#XPATH  //*[@id="customer-menu"]
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot1d.png')
#print ("Vet Portal")
#f.write('Vet Portal  \n')
######################################################################################################
#Contact Us###########################################################################################
#CSS SELECTOR  li.dropdown:nth-chalogild(2) > a:nth-child(1)
#XPATH  //*[@id="customer-menu"]
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot1e.png')
#print ("Contact Us")
#f.write('Contact Us  \n')
######################################################################################################
#MY ACCOUNT DROP DOWN ################################################################################
#CSS SELECTOR  #account-menu
#XPATH  //*[@id="account-menu"]
#—————————————————————Sign In————————————————————----———————————————
browser.find_element_by_id('account-menu').click() #OPENS My Account DROP DOWN
time.sleep(10)
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot1f.png')
#Sign In. https://www.justfoodfordogs.com/
#CSS SELECTOR  a.btn-primary
#XPATH  /html/body/div[2]/header/nav/div/div[1]/div/div/div/div/div[3]/li[3]/div/div/a
#browser.find_element_by_xpath("/html/body/div[2]/header/nav/div/div[1]/div/div/div/div/div[3]/li[3]/div/div/").click()
browser.find_element_by_css_selector("a.btn-primary").click() #Sign In
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot1g.png')
print ("My Account DROP DOWN")
f.write('My Account DROP DOWN \n')
browser.back() #BACK TO HOME PAGE
print ("BACK TO HOME PAGE")
f.write('BACK TO HOME PAGE \n')
#NEW CUSTOMER##########################################################################################
#———————————————————————New Customer—————————————————————————————————
browser.find_element_by_id('account-menu').click()
time.sleep(10)
#New Customer Start Here https://www.justfoodfordogs.com/login/?action=register
#CSS SELECTOR  .dropdown--menu--sign-up > a:nth-child(1)
#XPATH  /html/body/div[2]/header/nav/div/div[1]/div/div/div/div/div[3]/li[3]/div/div/span/a
browser.find_element_by_css_selector("a.btn-primary").click() #New Customer Start Here
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot1h.png')
print ("New Customer Start Here")
f.write('New Customer Start Here \n')
browser.back() #BACK TO HOME PAGE
print ("BACK TO HOME PAGE")
f.write('BACK TO HOME PAGE \n')
time.sleep(10)
#ACCOUNT################################################################################################
#————————————————————————Account————————————————————----————————————
browser.find_element_by_id('account-menu').click()
time.sleep(10)
#Account. https://www.justfoodfordogs.com/account
#CSS SELECTOR  div.content-asset:nth-child(3) > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)
#XPATH  /html/body/div[2]/header/nav/div/div[1]/div/div/div/div/div[3]/li[3]/div/div/div/ul/li[1]/a
browser.find_element_by_css_selector("div.content-asset:nth-child(3) > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)").click() #Account
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot1i.png')
print ("Account")
f.write('Account \n')
browser.back() #BACK TO HOME PAGE
print ("BACK TO HOME PAGE")
f.write('BACK TO HOME PAGE \n')
#ORDERS################################################################################################
#————————————————————————Orders—————————————————————————--------———————
browser.find_element_by_id('account-menu').click()
time.sleep(10)
#Orders  https://www.justfoodfordogs.com/orders
#CSS SELECTOR  div.content-asset:nth-child(3) > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1)
#XPATH  /html/body/div[2]/header/nav/div/div[1]/div/div/div/div/div[3]/li[3]/div/div/div/ul/li[2]/a
browser.find_element_by_css_selector("div.content-asset:nth-child(3) > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1").click() #Orders
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot1j.png')
print ("Orders")
f.write('Orders \n')
browser.back() #BACK TO HOME PAGE
print ("BACK TO HOME PAGE")
f.write('BACK TO HOME PAGE \n')
#MANAGE AUTOSHIP#########################################################################################
#—————————————————————————Manage Autoship———————————————————————————————
browser.find_element_by_id('account-menu').click()
time.sleep(10)
#Manage Autoship. https://www.justfoodfordogs.com/autoships
#CSS SELECTOR  div.content-asset:nth-child(3) > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1)
#XPATH  /html/body/div[2]/header/nav/div/div[1]/div/div/div/div/div[3]/li[3]/div/div/div/ul/li[3]/a
browser.find_element_by_css_selector("div.content-asset:nth-child(3) > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1)").click() #Manage Autoship
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot1k.png')
print ("Manage Autoship")
f.write('Manage Autoship \n')
browser.back() #BACK TO HOME PAGE
print ("BACK TO HOME PAGE")
f.write('BACK TO HOME PAGE \n')
#MY PETS##################################################################################################
#——————————————————————————My Pets————————————————————————----------——————
browser.find_element_by_id('account-menu').click()
time.sleep(10)
#My Pets. https://www.justfoodfordogs.com/mypets
#CSS SELECTOR  div.content-asset:nth-child(3) > ul:nth-child(1) > li:nth-child(4) > a:nth-child(1)
#XPATH  /html/body/div[2]/header/nav/div/div[1]/div/div/div/div/div[3]/li[3]/div/div/div/ul/li[4]/a
browser.find_element_by_css_selector("div.content-asset:nth-child(3) > ul:nth-child(1) > li:nth-child(4) > a:nth-child(1)").click() #My Pets
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot1l.png')
print ("My Pets")
f.write('My Pets \n')
browser.back() #BACK TO HOME PAGE
print ("BACK TO HOME PAGE")
f.write('BACK TO HOME PAGE \n')
#FILE/APP CLOSE############################################################################################
#——————————————————————————————————————————————-----------------——————————---------------------------------
print ("CLOSE FILE")
f.write('CLOSE FILE \n')
f.close()
#SHOP######################################################################################################
#FRESH FROZEN##############################################################################################
#//*[@id="daily-diets"] https://www.justfoodfordogs.com/daily-meals/
#DROP DOWN DISPLAYS 03/15/2021 1640
#elementDD = browser.find_element_by_id("shop")
#action = ActionChains(browser) #create action chain object
#action.click_and_hold(on_element = elementDD) #click and hold the item 
#action.perform() #SHOP DROP DOWN ELEMENT
#——————————————————————————————————————————————-----------------——————————---------------------------------
##DAILY DIETS###############################################################################################
#browser.find_element_by_id('daily-diets').click() #https://www.justfoodfordogs.com/daily-meals/ 
############################################################################################################
##PANTRY FRESH##############################################################################################
#browser.find_element_by_id('pantry-fresh').click()  #PANTRY FRESH
#VET DIETS##################################################################################################
#browser.find_element_by_id('vet-diets').click()
#DIY KITS###################################################################################################
#browser.find_element_by_id('diy-kits').click()
#CUSTOM DIETS###############################################################################################
#browser.find_element_by_id('custom-diets').click()
#DAILY DIETS################################################################################################
#browser.find_element_by_id('daily-diets-cats').click()
#TREATS#####################################################################################################
#browser.find_element_by_id('treats').click()
#SUPPLEMENTS################################################################################################
#browser.find_element_by_id('supplements').click()
#MERCHANDISE################################################################################################
#browser.find_element_by_id('').click(Merchandise)
############################################################################################################
#BROWSER####################################################################################################
#TRY CREATING/INSTANTIATE NEW BROWSER & CREATE elementDD/action/action.click_and_hold/action.perform 
#PANTRY FRESH //*[@id="pantry-fresh"] https://www.justfoodfordogs.com/pantry-fresh/
#browser.find_element_by_css_selector(".js--logoHome > img:nth-child(1)").click() #JFFD HOME PAGE LINK
#browser.find_element_by_id('pantry-fresh').click()  #PANTRY FRESH
#browser.back() #BACK TO HOME PAGE
#time.sleep(15)
#browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot2c.png')
#--------------------------------------------------------------------------------------------------
#VET SUPPORT MEALS##########################################################################################
#//*[@id="vet-diets"] https://www.justfoodfordogs.com/vet-support-meals/
#time.sleep(15)
#browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot2d.png')
#--------------------------------------------------------------------------------------------------
#DIY HOMEMADE KITS##########################################################################################
#//*[@id="diy-kits"] https://www.justfoodfordogs.com/diy/
#time.sleep(15)
#browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot2e.png')
#--------------------------------------------------------------------------------------------------
#CUSTOM DIETS###############################################################################################
#//*[@id="custom-diets"] https://www.justfoodfordogs.com/custom-prescriptive/
#time.sleep(15)
#browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot2f.png')
#--------------------------------------------------------------------------------------------------
#JUSTCATS###################################################################################################
#JUSTCATS  //*[@id="daily-diets-cats"] https://www.justfoodfordogs.com/just-cats/
#time.sleep(15)
#browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot2g.png')
#--------------------------------------------------------------------------------------------------
#TREATS#####################################################################################################
#//*[@id="treats"] https://www.justfoodfordogs.com/treats/
#time.sleep(15)
#browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot2h.png')
#--------------------------------------------------------------------------------------------------
#SUPPLEMENTS################################################################################################
#//*[@id="supplements"] https://www.justfoodfordogs.com/supplements/
#time.sleep(15)
#browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot2i.png')
#--------------------------------------------------------------------------------------------------
#BIG KIBBLE##################################################################################################
#//*[@id="Merchandise"] https://www.justfoodfordogs.com/product/big-kibble/700509903200.html
#time.sleep(15)
#browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot2j.png')
#--------------------------------------------------------------------------------------------------
#JFFD HOME PAGE LINK#########################################################################################
#browser.find_element_by_css_selector(".js--logoHome > img:nth-child(1)").click()
#browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot2k.png')
#CALCULATOR PAGE#############################################################################################
#https://www.justfoodfordogs.com/dog-food-calculator/
#browser.find_element_by_id("feeding-calculator").click() 
#browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot5.png')
#--------------------------------------------------------------------------------------------------
#ABOUT US ELEMENT############################################################################################
#elementAU = browser.find_element_by_id("about-us") 
#action = ActionChains(browser) #create action chain object
#action.click_and_hold(on_element = elementAU) #click and hold the item 
#action.perform() #perform the operation (show drop down) #WORKS 03/12/2021 1505
#browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot6.png') #SAME AS ScreenShot5.png
#BROWSER QUIT################################################################################################
browser.quit()
#--------------------------------------------------------------------------------------------------
