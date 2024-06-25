from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.locators import TestLocators
from tests.test_data import USER_EMAIL, USER_PASSWORD

def test_steps_personal_link(setup_driver):#Переход в личный кабинет
    driver = setup_driver
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.LOGIN_TO_ACCOUUNT))
    driver.find_element(*TestLocators.LOGIN_TO_ACCOUUNT).click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.LOGIN))
    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(USER_EMAIL)
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(USER_PASSWORD)
    driver.find_element(*TestLocators.LOGIN_TO_ACCOUUNT_REG).click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.BUTTON_CHECKOUT))
    driver.find_element(*TestLocators.PERSONAL_AREA).click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.INPUT_PERSONAL_AREA))
    personal_area = driver.find_element(*TestLocators.PERSONAL_AREA_IN)
    assert personal_area.is_displayed()

#Выход из аккаунта
def test_logout(setup_driver):
    driver = setup_driver
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.LOGIN_TO_ACCOUUNT)
    )
    driver.find_element(*TestLocators.LOGIN_TO_ACCOUUNT).click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.LOGIN))
    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(USER_EMAIL)
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(USER_PASSWORD)
    driver.find_element(*TestLocators.LOGIN_TO_ACCOUUNT_REG).click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.BUTTON_CHECKOUT))
    driver.find_element(*TestLocators.PERSONAL_AREA).click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.LOGOUT))
    driver.find_element(*TestLocators.LOGOUT).click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.LOGIN))
    button_registration = driver.find_element(*TestLocators.LOGIN)
    assert button_registration.is_displayed()
