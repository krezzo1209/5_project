from selenium.webdriver.common.by import By

class MainPageLocators:
    """Главная страница"""
    main_form = (By.CSS_SELECTOR, "main[class*='App_componentContainer']")
    logo_btn = (By.CSS_SELECTOR, "div[class*='AppHeader_header__logo']")
    personal_account_btn = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")
    login_account_btn = (By.XPATH, "//button[.='Войти в аккаунт']")
    constructor_btn = (By.XPATH, "//p[.='Конструктор']")
    order_feed_btn = (By.XPATH, "//p[.='Лента Заказов']")
    bun_btn = (By.XPATH, "//span[contains(text(),'Булки')]")
    sauces_btn = (By.XPATH, "//span[.='Соусы']")
    toppings_btn = (By.XPATH, "//span[.='Начинки']")
    place_order_button = (By.XPATH, "//button[.='Оформить заказ']")
    sauce_section = (By.XPATH, "//h2[.='Соусы']/following-sibling::ul")
    bun_section = (By.XPATH, "//h2[.='Булки']/following-sibling::ul")
    topping_section = (By.XPATH, "//h2[.='Начинки']/following-sibling::ul")

class AuthPageLocators:
    """Авторизация"""
    auth_form = (By.CSS_SELECTOR, "div[class*='Auth_login']")
    email_input = (By.CSS_SELECTOR, "input[type='email']")
    password_input = (By.CSS_SELECTOR, "input[type='password']")
    login_btn = (By.XPATH, "//button[.='Войти']")
    registration_btn = (By.XPATH, "//a[.='Зарегистрироваться']")
    recover_btn = (By.XPATH, "//a[.='Восстановить пароль']")
    constructor_btn = MainPageLocators.constructor_btn
    order_feed_btn = MainPageLocators.order_feed_btn
    logo_btn = MainPageLocators.logo_btn
    personal_account_btn = MainPageLocators.personal_account_btn

class RegistrationPageLocators:
    """Регистрация"""
    name_input = (By.CSS_SELECTOR, "input[name='name']")
    email_input = (By.CSS_SELECTOR, "input[type='email']")
    password_input = (By.CSS_SELECTOR, "input[type='password']")
    registration_btn = (By.XPATH, "//button[.='Зарегистрироваться']")
    login_btn = (By.XPATH, "//a[.='Войти']")
    constructor_btn = MainPageLocators.constructor_btn
    order_feed_btn = MainPageLocators.order_feed_btn
    logo_btn = MainPageLocators.logo_btn
    personal_account_btn = MainPageLocators.personal_account_btn
    error_double_user = (By.XPATH, "//p[.='Такой пользователь уже существует']")
    error_incorrect_password = (By.XPATH, "//p[.='Некорректный пароль']")

class RecoverPageLocators:
    """Восстановление пароля"""
    email_input = (By.CSS_SELECTOR, "input[type='email']")
    recover_btn = (By.XPATH, "//button[.='Восстановить']")
    login_btn = (By.XPATH, "//a[.='Войти']")
    constructor_btn = MainPageLocators.constructor_btn
    order_feed_btn = MainPageLocators.order_feed_btn
    logo_btn = MainPageLocators.logo_btn
    personal_account_btn = MainPageLocators.personal_account_btn

class PersonalAreaLocators:
    """Личный кабинет"""
    profile_form = (By.CSS_SELECTOR, "div[class*='Account_account']")
    profile_btn = (By.XPATH, "//a[.='Профиль']")
    order_history_btn = (By.XPATH, "//a[.='История заказов']")
    exit_btn = (By.XPATH, "//button[contains(.,'Выход')]")
    save_btn = (By.XPATH, "//button[.='Сохранить']")
    cancel_btn = (By.XPATH, "//button[.='Отмена']")
    constructor_btn = MainPageLocators.constructor_btn
    order_feed_btn = MainPageLocators.order_feed_btn
    logo_btn = MainPageLocators.logo_btn
    personal_account_btn = MainPageLocators.personal_account_btn
