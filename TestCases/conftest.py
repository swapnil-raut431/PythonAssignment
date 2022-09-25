import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

@pytest.fixture()
def setup():
    s=Service("C:\\Users\\Swapnil PC\\AppData\\Local\\Programs\\Python\\Python310\\chromedriver.exe")
    driver=webdriver.Chrome(service=s)
    return driver


