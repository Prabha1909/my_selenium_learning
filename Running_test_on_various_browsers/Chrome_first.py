from selenium import webdriver
import os


class ChromeTestWindows():
    def test(self):
        driverLocation = "C:\\Users\\pselvam\\Desktop\\Python_Tutorial\\Selenium\\Drivers\\chromedriver.exe"
        os.environ["Webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.get("http://www.letskodeit.com")

chrome = ChromeTestWindows()
chrome.test()