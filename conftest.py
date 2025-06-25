import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # ✅ добавлен импорт
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # раскомментируйте, если хотите запускать без UI
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def get_login_driver(driver):
    driver.get(URLS.MAIN_PAGE_URL)
    driver.find_element(*MainPageLocators.personal_account_btn).click()
    driver.find_element(*AuthPageLocators.email_input).send_keys(Person.email)
    driver.find_element(*AuthPageLocators.password_input).send_keys(Person.password)
    driver.find_element(*AuthPageLocators.login_account_btn).click()

    return driver