import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://automationpractice.com")
    driver.maximize_window()
    yield
    driver.quit()


def test_method(test_setup):
    assert driver.title == "My Store"


