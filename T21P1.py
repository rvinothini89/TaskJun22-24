from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep


class sausedemo:

    # locators
    username = "// input[ @ name = 'user-name']"
    password = "// input[ @ name = 'password']"
    login = "//input[@name='login-button']"
    options = "//button[@id='react-burger-menu-btn']"
    logout = "//a[text()='Logout']"

    # constructor to intialize url and driver
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    # method to access web page
    def webpageAccess(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            sleep(2)
            # getting cookies before login using get_cookies() method
            cookies = self.driver.get_cookies()
            print("Cookies before login: ",cookies)
        except:
            print("Error accessing web page")

    # method to login to webpage
    def webLogin(self):
        try:
            userName = self.driver.find_element(by=By.XPATH,value=self.username)
            userName.send_keys("problem_user")
            sleep(2)
            passWord = self.driver.find_element(by=By.XPATH,value=self.password)
            passWord.send_keys("secret_sauce")
            sleep(2)
            login_button = self.driver.find_element(by=By.XPATH,value=self.login)
            login_button.click()
            sleep(2)
            # getting cookies after login using get_cookies() method.
            # before login cookies were empty and populated post login
            cookies = self.driver.get_cookies()
            for cookie in cookies:
                    print("cookies after login: ", cookie)
        except:
            print("Error logging into web page")

    # method to logout from web page
    def webLogout(self):
        try:
            o_button = self.driver.find_element(by=By.XPATH,value=self.options)
            o_button.click()
            sleep(2)
            logout_button = self.driver.find_element(by=By.XPATH,value=self.logout)
            logout_button.click()
            sleep(2)
        except:
            print("Error logging out from webpage")

    # method to quit the driver
    def shutdown(self):
        try:
            self.driver.quit()
        except:
            print("Error terminating driver")


url = "https://www.saucedemo.com/"
sd = sausedemo(url)
sd.webpageAccess()
sd.webLogin()
sd.webLogout()
sd.shutdown()
