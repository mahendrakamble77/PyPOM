import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import allure
from allure_commons.types import AttachmentType



def get_data():
    return [

        ("purva","purva"),
        ("shubdha", "shubdha"),
        ("purva","purva")
    ]

def setup_function():
    global currentDriver
    mySite = "http://bussiness.tmoksha.com/"

    currentDriver = webdriver.Chrome ( executable_path = ChromeDriverManager ().install () )
    currentDriver.implicitly_wait ( 20 )
    currentDriver.get ( mySite )
    currentDriver.maximize_window ()
    allure.attach(currentDriver.get_screenshot_as_png(),name="loginPage",attachment_type = AttachmentType.PNG)

def teardown_function():
    currentDriver.quit()


@pytest.mark.parametrize("username,password",get_data())
def test_doLogin (username, password ) :
    print (username + " -------- " + password )
    user = currentDriver.find_element_by_id ( "username" )
    user.send_keys ( username )

    # Simple input to Password text field
    passw = currentDriver.find_element_by_id ( "password" )
    passw.send_keys ( password )

    # for Clicking the Button
    currentDriver.find_element_by_class_name ( "button" ).click ()
    title = currentDriver.title

    if "Home" in title :
        print ( " We are on home page - Test Passed" )
    else :
        print ( "Test is Failed" )
    allure.attach ( currentDriver.get_screenshot_as_png (), name = "homepage", attachment_type = AttachmentType.PNG )
    # Getting the Text Value
    currentUser = currentDriver.find_element_by_xpath ( "//*[@id='topmenu-login-dropdown']/a/span[1]" ).text

    print ( currentUser )
