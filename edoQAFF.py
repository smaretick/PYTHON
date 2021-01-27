from selenium import webdriver 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time 

#runs with either Firefox or Chrome
browser = webdriver.Firefox()
browser.maximize_window()
#Firefox loads all pages without wait calls

#ChromeDriver
#DesiredCapabilities capabilities = DesiredCapabilities.chrome();
#capabilities.setCapability("chrome.verbose", false);
#browser = webdriver.Chrome()

#QA Marketplace link
browser.get("http://abcdefghijk.qa.edo:8080/marketplace-ui/")
browser.save_screenshot('//Users/nickmaschinski/Desktop/EDOscreengrabs/edo1QAMrktPl.png')  #screenshot
print "Selenium call to QA"

#PROD
#browser.get("http://abcdefghijk.edo.local/marketplace-ui/login.do;jsessionid=46DDC9EE0179F21B0720123B4822A2B5.c10v212")
#browser.save_screenshot('//Users/nickmaschinski/Desktop/EDOscreengrabsP/edo1Prod.png')  #screenshot
#print "Selenium call to prod"

#UAT
#echo "Selenium call to UAT"
#UAT Marketplace link
#browser.get("http://abcdefghijk.uat.edo:8080/marketplace-ui/")

#calling implicitly_wait method only works with Firefox for screengrabs if you call it once
print "Call to wait 90 secs"
browser.implicitly_wait(90)

#print "Logon to QA (smaretick@edointeractive.com)"
#Username
print "Call to input username"
browser.find_element_by_name("j_username").clear()
browser.find_element_by_name("j_username").send_keys("scott.maretick@edointeractive.com")
#password
print "Call to input password"
browser.find_element_by_name("j_password").clear()
browser.find_element_by_name("j_password").send_keys("sm110751")
browser.save_screenshot('//Users/nickmaschinski/Desktop/EDOscreengrabs/edo2QAMrktPl.png')  #screenshot
browser.find_element_by_css_selector("input.btn.btn-success").click()

#Dashboard
print "Call to get Dashboard"
browser.get("http://abcdefghijk.qa.edo:8080/marketplace-ui/Accounts/EnrolledAccountsDashboard")
browser.save_screenshot('//Users/nickmaschinski/Desktop/EDOscreengrabs/edo3QADashboard.png')  #screenshot

#Network Research
print "Call to get Network Research"
#Network Analyzer
browser.get("http://abcdefghijk.qa.edo:8080/marketplace-ui/presale/networkAnalyzer")
print "Call to get Network Analyzer"
print "sleeping for 60 secs to allow page to load"
time.sleep(60) # Let the page load
browser.save_screenshot('//Users/nickmaschinski/Desktop/EDOscreengrabs/edo4QANetworkAnalyzer.png')  #screenshot

#Location Explorer
print "Call to get Location Explorer"
browser.get("http://abcdefghijk.qa.edo:8080/marketplace-ui/presale/locationExplorer")
print "sleeping for 20 secs to allow page to load"
time.sleep(20) # Let the page load
browser.save_screenshot('//Users/nickmaschinski/Desktop/EDOscreengrabs/edo5QALocationExplorer.png')  #screenshot

#Budget Bulider
print "Call to Budget Builder"
browser.get("http://abcdefghijk.qa.edo:8080/marketplace-ui/presale/budgetBuilder")
browser.save_screenshot('//Users/nickmaschinski/Desktop/EDOscreengrabs/edo6QABudgetBuilder.png')  #screenshot

#Enroll Accounts
print "Call to get Enroll Accounts" 
browser.get("http://abcdefghijk.qa.edo:8080/marketplace-ui/Accounts/EnrollmentList")
browser.save_screenshot('//Users/nickmaschinski/Desktop/EDOscreengrabs/edo7QAEnrollAccts.png')  #screenshot

#Active Accounts
browser.get("http://abcdefghijk.qa.edo:8080/marketplace-ui/Accounts/Active")
print "Call to get Active Accounts"
browser.save_screenshot('//Users/nickmaschinski/Desktop/EDOscreengrabs/edo8QAActiveAccts.png')  #screenshot

print "Call to quit browser"
browser.quit()
#browser.close()
