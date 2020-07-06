from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


def sign_in(driver_sign_in):
    driver_sign_in.find_element_by_id("email").send_keys("vesihi3633@wonwwf.com")
    driver_sign_in.find_element_by_id("passwd").send_keys("PonPon", Keys.ENTER)


if __name__ == '__main__':
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://automationpractice.com")
    driver.maximize_window()
    driver.find_element_by_link_text("Sign in").click()
    signIn(driver)
    driver.find_element_by_css_selector("a.logout").click()

