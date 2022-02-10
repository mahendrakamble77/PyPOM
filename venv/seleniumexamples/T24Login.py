import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException




#chromeDriverPath = "C:\\SeleniumProject\\seleniumproject\\venv\\drivers\\chromedriver.exe"
mySite = "http://13.91.17.160:8080/BrowserWeb/servlet/BrowserServlet"


currentDriver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
currentDriver.implicitly_wait(20)
currentDriver.get(mySite)
currentDriver.maximize_window()
title = currentDriver.title
cd = currentDriver


#Simple input to Text Field
user = currentDriver.find_element_by_xpath("//*[@id='signOnName']")
user.send_keys("ATAR.2")

#Simple input to Password text field
password = currentDriver.find_element_by_xpath("//*[@id='password']")
password.send_keys("87654321")

#for Clicking the Button
currentDriver.find_element_by_xpath("//*[@id='sign-in']").click()


cd.quit()