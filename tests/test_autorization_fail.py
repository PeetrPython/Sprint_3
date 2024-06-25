from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.locators import TestLocators
from tests.test_data import USER_NAME, USER_EMAIL, USER_PASSWORD, INVALID_PASSWORD

# Регистрация с некорректным паролем
def test_register_user_invalid_pas(setup_driver):
    driver = setup_driver
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.LOGIN_TO_ACCOUUNT)
    )
    driver.find_element(*TestLocators.LOGIN_TO_ACCOUUNT).click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.LOGIN)
    )
    driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()
    driver.find_element(*TestLocators.INPUT_NAME).send_keys(USER_NAME)
    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(USER_EMAIL)
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(INVALID_PASSWORD)
    driver.find_element(*TestLocators.BUTTON_REGISTRATION_1).click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.TEXT_INVALID_PAS))
    err_pas = driver.find_element(*TestLocators.TEXT_INVALID_PAS)
    assert err_pas.is_displayed()

#Регистрация с незаполненым именем
def test_register_invalid_name(setup_driver):
    driver = setup_driver
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.LOGIN_TO_ACCOUUNT)
    )
    driver.find_element(*TestLocators.LOGIN_TO_ACCOUUNT).click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.LOGIN)
    )
    driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()
    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(USER_EMAIL)
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(USER_PASSWORD)
    driver.find_element(*TestLocators.BUTTON_REGISTRATION_1).click()

    assert WebDriverWait(driver, 3).until_not(
        EC.visibility_of_element_located(TestLocators.LOGIN))


def test_register_invalid_email(setup_driver):
    driver = setup_driver
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.LOGIN_TO_ACCOUUNT)
    )
    driver.find_element(*TestLocators.LOGIN_TO_ACCOUUNT).click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.LOGIN)
    )
    driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()
    driver.find_element(*TestLocators.INPUT_NAME).send_keys(USER_NAME)
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(USER_PASSWORD)
    driver.find_element(*TestLocators.BUTTON_REGISTRATION_1).click()

    assert WebDriverWait(driver, 3).until_not(
        EC.visibility_of_element_located(TestLocators.LOGIN))

