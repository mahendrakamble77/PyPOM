from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

#chromeDriverPath = "C:\\SeleniumProject\\seleniumproject\\venv\\drivers\\chromedriver.exe"
mySite = "http://bussiness.tmoksha.com/"


currentDriver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
currentDriver.get(mySite)
currentDriver.maximize_window()
title = currentDriver.title

assert "Login" in title

currentDriver.quit()
