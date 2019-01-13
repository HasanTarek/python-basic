from selenium import webdriver

import time

from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome("/Users/hasantarek/Documents/workspace_python/PythonTutorial/selenium/chromedriver")
driver.get("https://www.cpg.org/")

# driver.set_page_load_timeout(2)
# time.sleep(2)
driver.find_element_by_css_selector("[class='span-24'] [class] [class='tiny-span-30']:nth-of-type(1) [target]").send_keys(Keys.ENTER)


