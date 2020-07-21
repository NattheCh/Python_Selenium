from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///E:/Selenium%20Python/FileUpload.html")

upload_input = driver.find_element_by_id("myFile")

path = os.path.abspath("pipi.txt")

driver.save_screenshot("screenshots/beforeupload.png")
upload_input.send_keys(path)
driver.save_screenshot("screenshots/afterupload.png")