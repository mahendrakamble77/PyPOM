from configparser import ConfigParser

config = ConfigParser()

config.read("config.ini")

print(config.get("locators","username"))

print(config.get("testConfig","mySite"))


def readConfig(section,key):
    config = ConfigParser()
    config.read("config.ini")
    return config.get(section, key)

print(readConfig("locators-user","mainmenu1"))
