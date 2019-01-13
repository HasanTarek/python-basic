from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("/Users/hasantarek/Documents/workspace_python/PythonTutorial/selenium/chromedriver")

driver.implicitly_wait("30")
driver.get("https://www.facebook.com/")
driver.implicitly_wait("30")
# driver.maximize_window()
# driver.implicitly_wait("30")
# driver.find_element_by_xpath().send_keys(Keys.ENTER)
# driver.implicitly_wait("30")
driver.find_element_by_id("email").send_keys("tarek_101@hotmail.com")
# driver.implicitly_wait("30")
driver.find_element_by_id("pass").send_keys("123abcxyz")
driver.find_element_by_id("u_0_2").send_keys(Keys.ENTER)


driver.quit()
for x in range(0,5):
    print("********** PASS **********")
# time.sleep(10)
# driver.implicitly_wait("30")
# driver.set_page_load_timeout(10)