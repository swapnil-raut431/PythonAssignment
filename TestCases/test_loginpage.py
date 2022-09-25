import time

import pytest
import softest

from Utility.XLutils import xlutils
from POM.LoginPage import *
from selenium.webdriver.chrome.service import Service


class Testddt1:
    baseurl="https://admin-demo.nopcommerce.com/"
    path="C:\\Users\\Swapnil PC\\PycharmProjects\\pythonProject11\\Test_Data\\data1.xlsx"

    def test_0001(self,setup):
        self.driver=setup
        self.driver.get(self.baseurl)
        self.lp=Loginpage(self.driver)
        self.row=xlutils.getrowcount(self.path,'Sheet2')
        lst_status=[]

        for r in range(2,self.row+1):
            username=xlutils.readdata(self.path,'Sheet2',r,1)
            password=xlutils.readdata(self.path,'Sheet2',r,2)
            exp=xlutils.readdata(self.path,'Sheet2',r,3)

            self.lp.setusername(username)
            self.lp.setpassword(password)
            self.lp.clicklogin()
            time.sleep(3)

            value="Dashboard / nopCommerce administration"
            if self.driver.title==value:
                self.driver.close()
                assert True
                print("test passed")
            else:
                assert False
                self.driver.close()
                print("test failed")

