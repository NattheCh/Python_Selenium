from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://automationpractice.com")
driver.maximize_window()
driver.find_element_by_id("search_query_top")
driver.find_element(By.ID, "search_query_top")
driver.find_element_by_css_selector("a")
driver.find_element_by_css_selector("img.logo")
driver.get("http://automationpractice.com/index.php?id_product=6&controller=product")
print(driver.find_element_by_css_selector("td:nth-child(2)").text)
print(driver.find_element_by_xpath("//tbody//tr[2]//td[2]").text)
lista = len(driver.find_elements_by_xpath("//tbody//tr"))
print(lista)

driver.quit()