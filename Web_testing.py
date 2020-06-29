from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://automationpractice.com")
driver.maximize_window()
driver.find_element_by_id("search_query_top").send_keys("skirt", Keys.ENTER)
driver.find_element_by_class_name("product_img_link").click()

driver.execute_script("window.scrollTo(0, 400)")

quantity_input = driver.find_element_by_id("quantity_wanted")
quantity_input.clear()
quantity_input.send_keys("3")

size_select = Select(driver.find_element_by_tag_name("select"))
size_select.select_by_visible_text("M")

driver.find_elements_by_class_name("icon-minus")[0].click()