from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("/Users/hasantarek/Documents/workspace_python/PythonTutorial/selenium/chromedriver")

# driver.get("http://google.com")
driver.get("https://www.td.com/us/en/personal-banking/")
# driver.find_element_by_css_selector("[maxlength]").send_keys("https://www.td.com/us/en/personal-banking/")
# driver.set_page_load_timeout("10")
# time.sleep(2)
# driver.find_element_by_css_selector(".FPdoLc [value='Google Search']").send_keys(Keys.ENTER)

# driver.set_page_load_timeout("10")
# time.sleep(2)
driver.find_element_by_class_name("label")
driver.find_element_by_css_selector(".td-desktop-search-show-btn").click()
driver.find_element_by_css_selector(".td-search-container .td-search-input").send_keys("What is Savings Overdraft Protection?")
driver.find_element_by_css_selector(".td-search-container [value]").send_keys(Keys.ENTER)
driver.maximize_window()


# driver.find_element_by_css_selector(".ng-touched").send_keys(Keys.RETURN)

driver.quit()

# driver.quit()
# driver.find_element_by_xpath("/html//div[@id='rso']/div[1]/div[@class='g']//a[@href='https://www.apple.com/']/h3[@class='LC20lb']").click()
# driver.set_page_load_timeout(10)
# time.sleep(2)

str = "spl"
str.split()
print(str)


