import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException

def isElementPresentID(id):
    try:
        res = cd.find_element_by_id(id).is_displayed()
        return res
    except NoSuchElementException as msg:
        return False



#chromeDriverPath = "C:\\SeleniumProject\\seleniumproject\\venv\\drivers\\chromedriver.exe"
mySite = "http://bussiness.tmoksha.com/"


currentDriver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
currentDriver.implicitly_wait(20)
currentDriver.get(mySite)
currentDriver.maximize_window()
title = currentDriver.title

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
currentDriver.find_element_by_xpath("//*[@id=\"mainmenua_hrm\"]/span").click()

#Clicking Left Menu using xpath
currentDriver.find_element_by_xpath("//*[@id=\"id-left\"]/div/div[3]/div[3]/a").click()
# This is for Drop Down
#first identify the Dropdown on Screen using xpath
dd = currentDriver.find_element_by_xpath("//*[@id=\"type\"]")
#Then use Select imported from Webdriver.support
#Select(dd).select_by_visible_text("Sick leave")
cd = currentDriver
selectDD = Select(dd)
selectDD.select_by_value("2")

element = cd.find_element_by_xpath("//*[@id='date_debut_']")

print(element.is_displayed())

result = isElementPresentID("date_debut")
print("Recieved from function : ",result)

result = isElementPresentID("date_debut_")
print("Recieved from function : ",result)

print("Code after Exception")

cd.quit()