from locators import MainPageLocators, PersonalAreaLocators, AuthPageLocators
from urls import URLS
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver, get_login_driver
from data import Person


class TestProfileArea:


    def test_transition_from_personal_area_to_constructor_by_click_constructor_btn_success(self, get_login_driver):
        """Проверка перехода из личного кабинета в конструктор по кнопке 'Конструктор'"""
        driver = get_login_driver
        driver.maximize_window()

        # Переход в ЛК
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.personal_account_btn)
        )
        driver.find_element(*MainPageLocators.personal_account_btn).click()

        # Кликаем на "Конструктор"
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(PersonalAreaLocators.constructor_btn)
        )
        driver.find_element(*PersonalAreaLocators.constructor_btn).click()

        # Ожидаем перехода на главную страницу конструктора
        WebDriverWait(driver, 10).until(
            EC.url_to_be(URLS.MAIN_PAGE_URL)
        )
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.bun)
        )

        bun_displayed = driver.find_element(*MainPageLocators.bun).is_displayed()

        assert driver.current_url == URLS.MAIN_PAGE_URL and bun_displayed


    def test_transition_from_personal_area_to_constructor_by_click_logo_success(self, get_login_driver):
        """Проверка перехода из личного кабинета в конструктор по клику на логотип"""
        driver = get_login_driver
        driver.maximize_window()

        # Переход в ЛК
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.personal_account_btn)
        )
        driver.find_element(*MainPageLocators.personal_account_btn).click()

        # Кликаем на логотип
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(PersonalAreaLocators.logo_btn)
        )
        driver.find_element(*PersonalAreaLocators.logo_btn).click()


        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.bun)
        )

        bun_displayed = driver.find_element(*MainPageLocators.bun).is_displayed()

        assert driver.current_url == URLS.MAIN_PAGE_URL and bun_displayed
