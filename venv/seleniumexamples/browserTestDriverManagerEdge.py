from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager

#chromeDriverPath = "C:\\SeleniumProject\\seleniumproject\\venv\\drivers\\chromedriver.exe"
mySite = "http://bussiness.tmoksha.com/"


currentDriver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())

currentDriver.get(mySite)
currentDriver.maximize_window()
title = currentDriver.title

assert "Login" in title

print(title)

currentDriver.quit()
