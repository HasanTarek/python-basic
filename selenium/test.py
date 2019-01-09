from selenium import webdriver

import time

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("/Users/hasantarek/Documents/workspace_python/PythonTutorial/selenium/chromedriver")
# driver = webdriver.Firefox("/Users/hasantarek/Documents/workspace_python/PythonTutorial/selenium/geckodriver")
# driver = webdriver.ie("/Users/hasantarek/Documents/workspace_python/PythonTutorial/selenium/IEDriverServer.exe")
driver.set_page_load_timeout("10")
driver.get("https://www.google.com/")
driver.find_element_by_name("q").send_keys("http://venturepulse.org/")

time.sleep(4)
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)

driver.get("http://venturepulse.org/")
time.sleep(4)
driver.find_element_by_css_selector('#nav_list_items li:nth-of-type(2) [target]').click()

time.sleep(6)
driver.set_page_load_timeout("50")
driver.maximize_window()
driver.refresh()
driver.quit()
