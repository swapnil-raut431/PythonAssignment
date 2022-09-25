from selenium.webdriver.common.by import By


class Loginpage:
    text_username_xpath="//input[@id='Email']"
    text_password_xpath="//input[@id='Password']"
    button_login_xpath="//button[normalize-space()='Log in']"
    button_logout_Linktext="Logout"

    def __init__(self,driver):
        self.driver=driver

    def setusername(self,username):
        self.driver.find_element(By.XPATH,self.text_username_xpath).clear()
        self.driver.find_element(By.XPATH,self.text_username_xpath).send_keys(username)

    def setpassword(self,password):
        self.driver.find_element(By.XPATH,self.text_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_password_xpath).send_keys(password)

    def clicklogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def clicklogout(self):
        self.driver.find_element(By.LINK_TEXT,self.button_logout_Linktext).click()