from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.locators import TestLocators
from tests.test_data import USER_EMAIL, USER_PASSWORD

# Вход по кнопке «Войти в аккаунт» на главной
def test_login_via_main_button(setup_driver):
    driver = setup_driver
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.LOGIN_TO_ACCOUUNT)
    )
    driver.find_element(*TestLocators.LOGIN_TO_ACCOUUNT).click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.LOGIN)
    )
    driver.find_element(*TestLocators.AUTOR_EMAIL).send_keys(USER_EMAIL)
    driver.find_element(*TestLocators.AUTOR_PASSWORD).send_keys(USER_PASSWORD)
    driver.find_element(*TestLocators.LOGIN_TO_ACCOUUNT_REG).click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.BUTTON_CHECKOUT)
    )
    order_button = driver.find_element(*TestLocators.BUTTON_CHECKOUT)
    assert order_button.is_displayed()


# Авторизация через Личный кабинет
def test_login_via_personal_cabinet(setup_driver):
    driver = setup_driver
    WebDriverWait(driver, 4).until(
        EC.visibility_of_element_located(TestLocators.LOGIN_TO_ACCOUUNT)
    )
    driver.find_element(*TestLocators.PERSONAL_AREA).click()
    WebDriverWait(driver, 9).until(
        EC.visibility_of_element_located(TestLocators.LOGIN)
    )
    driver.find_element(*TestLocators.AUTOR_EMAIL).send_keys(USER_EMAIL)
    driver.find_element(*TestLocators.AUTOR_PASSWORD).send_keys(USER_PASSWORD)
    driver.find_element(*TestLocators.LOGIN_TO_ACCOUUNT_REG).click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.BUTTON_CHECKOUT)
    )
    order_button = driver.find_element(*TestLocators.BUTTON_CHECKOUT)
    assert order_button.is_displayed()

# Вход через кнопку в форме восстановления пароля
def test_login_via_forgot_password_form(setup_driver):
    driver = setup_driver
    WebDriverWait(driver, 4).until(
        EC.visibility_of_element_located(TestLocators.LOGIN_TO_ACCOUUNT)
    )
    driver.find_element(*TestLocators.LOGIN_TO_ACCOUUNT).click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.LOGIN)
    )
    driver.find_element(*TestLocators.BUTTON_RESTORE).click()
    driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()
    driver.find_element(*TestLocators.AUTOR_EMAIL).send_keys(USER_EMAIL)
    driver.find_element(*TestLocators.AUTOR_PASSWORD).send_keys(USER_PASSWORD)
    driver.find_element(*TestLocators.LOGIN_TO_ACCOUUNT_REG).click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.BUTTON_CHECKOUT)
    )
    order_button = driver.find_element(*TestLocators.BUTTON_CHECKOUT)
    assert order_button.is_displayed()

