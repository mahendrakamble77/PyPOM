import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException




#chromeDriverPath = "C:\\SeleniumProject\\seleniumproject\\venv\\drivers\\chromedriver.exe"
mySite = "http://bussiness.tmoksha.com/"


currentDriver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
currentDriver.implicitly_wait(20)
currentDriver.get(mySite)
currentDriver.maximize_window()
title = currentDriver.title
cd = currentDriver
assert "Login" in title

#Simple input to Text Field
user = currentDriver.find_element_by_id("username")
user.send_keys("purva")

#Simple input to Password text field
password = currentDriver.find_element_by_id("password")
password.send_keys("purva")

#for Clicking the Button
currentDriver.find_element_by_class_name("button").click()

title = currentDriver.title

if "Home" in title:
    print(" We are on home page - Test Passed")
else:
    print("Test is Failed")

#Getting the Text Value
currentUser = currentDriver.find_element_by_xpath("//*[@id='topmenu-login-dropdown']/a/span[1]").text

print(currentUser)

#Clicking the Menu using Xpath
currentDriver.find_element_by_xpath("//*[@id='mainmenutd_project']/div").click()


#Clicking Left Menu using xpath
currentDriver.find_element_by_xpath("//*[@id='id-left']/div/div[3]/div[3]/a").click()


element = cd.find_element_by_xpath("//*[@id='id-right']/div/form/div[2]/table/tbody/tr[12]/td[2]/input")
time.sleep(10)
if not element.is_selected():
    element.click()
    print("Executed this code")

time.sleep(15)
cd.quit()