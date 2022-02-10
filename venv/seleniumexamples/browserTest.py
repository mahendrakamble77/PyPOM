from selenium import webdriver

chromeDriverPath = "C:\\SeleniumProject\\seleniumproject\\venv\\drivers\\chromedriver.exe"
mySite = "http://bussiness.tmoksha.com/"


currentDriver = webdriver.Chrome(executable_path=chromeDriverPath)
currentDriver.get(mySite)
currentDriver.maximize_window()
title = currentDriver.title

assert "Login" in title



currentDriver.quit()
