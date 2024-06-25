from selenium.webdriver.common.by import By

class TestLocators:
    LOGIN_TO_ACCOUUNT = By.XPATH, ".//button[text()='Войти в аккаунт']"
    LOGIN = By.XPATH, ".//h2[text()='Вход']"
    LOGIN_TO_ACCOUUNT_REG = By.XPATH, ".//button[text()='Войти']"
    BUTTON_REGISTRATION = By.XPATH, ".//a[@class='Auth_link__1fOlj']"
    INPUT_NAME = By.XPATH, "//label[text()='Имя']/following-sibling::input[@type='text']"
    INPUT_EMAIL = By.XPATH, "//label[text()='Email']/following-sibling::input[@type='text']"
    INPUT_PASSWORD = By.XPATH, ".//input[@type='password']"
    BUTTON_REGISTRATION_1 = By.XPATH, ".//button[text()='Зарегистрироваться']"
    PERSONAL_AREA = By.XPATH, ".//p[text()='Личный Кабинет']"
    AUTOR_EMAIL = By.XPATH, ".//input[@type='text']"
    AUTOR_PASSWORD = By.XPATH, ".//input[@type='password']"
    BUTTON_CHECKOUT = By.XPATH, ".//button[text()='Оформить заказ']"
    BUTTON_RESTORE = By.XPATH, ".//a[text()='Восстановить пароль']"
    LOGOUT = By.XPATH, ".//button[text()='Выход']"
    BURGER_LOGO = By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']"
    LEGO = By.XPATH, ".//p[text()='Конструктор']"
    BUTTON_SAUCE = By.XPATH, ".//span[text()='Соусы']"
    BUTTON_FILLING = By.XPATH, ".//span[text()='Начинки']"
    BUTTON_BREAD = By.XPATH, ".//span[text()='Булки']"
    BREAD_TAB = By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc') and .//span[text()='Булки']]"
    FILLING_TAB = By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc') and .//span[text()='Начинки']]"
    SAUCES_TAB = By.XPATH,"//div[contains(@class, 'tab_tab_type_current__2BEPc') and .//span[text()='Соусы']]"
    PERSONAL_AREA_IN = By.XPATH, ".//p[text()='В этом разделе вы можете изменить свои персональные данные']"
    INPUT_PERSONAL_AREA = By.XPATH, ".//div[@class='input__container']"
    TEXT_INVALID_PAS = By.XPATH, ".//p[text()='Некорректный пароль']"




