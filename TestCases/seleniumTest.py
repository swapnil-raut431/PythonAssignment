import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

print("****************exceution started**********************")
driver = webdriver.Chrome()
driver.get("http://seiyria.com/bootstrap-slider/")
slider = driver.find_element(By.CSS_SELECTOR,"div#example-1 div.slider-handle.min-slider-handle.round")
move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(40, 0).release().perform()
time.sleep(5)
print(slider.location)
driver.close()
