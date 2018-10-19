from selenium import webdriver

class FFtest():
    def fftest_method(self):

        #creating the instance of webdriver
        driver = webdriver.Firefox(executable_path="C:\\Users\\pselvam\\Desktop\\Python_Tutorial\\Selenium\\Drivers\\geckodriver.exe")

        driver.get("http://www.facebook.com")

ff = FFtest
ff.fftest_method(self="a")

#added comment
