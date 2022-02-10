import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

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

selectDD = Select(dd)
selectDD.select_by_value("2")

print("Length of DropDown is : ",len(selectDD.options))
for m in selectDD.options:
    print(m.text)



#Simple Sending keys
currentDriver.find_element_by_xpath("//*[@id=\"date_debut_\"]").send_keys("01/19/2022")

cd = currentDriver

elements = cd.find_elements_by_tag_name("a")
print(len(elements))

'''
for links in elements:
    print("The text is  ", links.text, "and URL link is ",links.get_attribute("href"))

'''

# Finding links from particular area

block = cd.find_element_by_xpath("//*[@id='id-left']")
elements = block.find_elements_by_tag_name("a")

print(len(elements))


for links in elements:
    print("The text is  ", links.text, "and URL link is ",links.get_attribute("href"))


print("Directly Printing", elements.__getitem__(3).text)




