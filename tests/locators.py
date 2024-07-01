from selenium.webdriver.common.by import By


class Locators:

    # Страница входа в аккаунт
    LOGIN_EMAIL = (By.XPATH, "//input[@type='text']")
    LOGIN_PASSWORD = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//form//button")
    LOGIN_LINK = (By.XPATH, "//a[@href='/login']")

    # Страница восстановления пароля
    PASS_RECOVERY_LINK = (By.XPATH, "//a[@href='/forgot-password']")
    PASS_RECOVERY_EMAIL = (By.XPATH, "//input[@type='text']")
    PASS_RECOVERY_BUTTON = (By.XPATH, "//form//button")
    PASS_RECOVERY_PAGE_LABEL = (By.XPATH, "//h2")

    # Кнопки входа на главной странице и кнопка зарегистрироваться
    SIGN_IN_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")
    AUTH_BUTTON = (By.XPATH, "//form//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")

    # Страница регистрации
    REGISTER_LINK = (By.XPATH, "//a[@href='/register']")
    REGISTER_LOGIN = (By.XPATH, "//label[contains(text(), 'Имя')]/..//input")
    REGISTER_EMAIL = (By.XPATH, "//label[contains(text(), 'Email')]/..//input")
    REGISTER_PASSWORD = (By.XPATH, "//label[contains(text(), 'Пароль')]/..//input")
    REGISTER_PASSWORD_ERROR_MESSAGE = (By.XPATH, "//p[@class='input__error text_type_main-default']")

    # Страница личного кабинета
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//nav//a[@href='/account']")
    PERSONAL_ACCOUNT_EMAIL = (By.XPATH, "//input[@value='marialawson@example.net']")
    LOG_OUT_BUTTON = (By.XPATH, "//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']")
    LOG_OUT_LABEL = (By.XPATH, "//h2")
    LOGO_LINK = (By.XPATH, "//nav//div/a[@href='/']")

    # Страница конструктора
    CONSTRUCTOR_LINK = (By.XPATH, "//nav//a[@class='AppHeader_header__link__3D_hX']")
    CONSTRUCTOR_LABEL = (By.XPATH, "//h1")
    SAUCES_LINK_ACTIVE = (By.XPATH, "//div[span[contains(text(), 'Соусы')]]")
    FILLINGS_LINK_ACTIVE = (By.XPATH, "//div[span[contains(text(), 'Начинки')]]")
    BREADS_LINK_ACTIVE = (By.XPATH, "//div[span[contains(text(), 'Булки')]]")
