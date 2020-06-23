from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://automationpractice.com")
driver.maximize_window()
driver.find_element_by_id("search_query_top").send_keys("skirt", Keys.ENTER)
driver.find_element_by_class_name("product_img_link").click()
