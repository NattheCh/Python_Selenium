from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.w3schools.com")

tutorials_elements = driver.find_element_by_id("navbtn_tutorials")

webdriver.ActionChains(driver).move_to_element(tutorials_elements).perform()