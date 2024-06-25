from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.locators import TestLocators
from tests.test_data import USER_EMAIL, USER_PASSWORD

#Переход из личного кабинета в конструктор через stellaburger
def test_steps_logo_burger(setup_driver):#Переход в личный кабинет
    driver = setup_driver
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.LOGIN_TO_ACCOUUNT))
    driver.find_element(*TestLocators.LOGIN_TO_ACCOUUNT).click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.LOGIN))
    driver.find_element(*TestLocators.AUTOR_EMAIL).send_keys(USER_EMAIL)
    driver.find_element(*TestLocators.AUTOR_PASSWORD).send_keys(USER_PASSWORD)
    driver.find_element(*TestLocators.LOGIN_TO_ACCOUUNT_REG).click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.BUTTON_CHECKOUT))
    driver.find_element(*TestLocators.PERSONAL_AREA).click()
    driver.find_element(*TestLocators.BURGER_LOGO).click()#клик по лого
    order_but = driver.find_element(*TestLocators.BUTTON_CHECKOUT)
    assert order_but.is_displayed()

#Переход из личного кабинета в конструктор
def test_steps_click_constructor(setup_driver):
    driver = setup_driver
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.LOGIN_TO_ACCOUUNT))
    driver.find_element(*TestLocators.LOGIN_TO_ACCOUUNT).click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.LOGIN))
    driver.find_element(*TestLocators.AUTOR_EMAIL).send_keys(USER_EMAIL)
    driver.find_element(*TestLocators.AUTOR_PASSWORD).send_keys(USER_PASSWORD)
    driver.find_element(*TestLocators.LOGIN_TO_ACCOUUNT_REG).click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.BUTTON_CHECKOUT))
    driver.find_element(*TestLocators.PERSONAL_AREA).click()
    driver.find_element(*TestLocators.LEGO).click()
    order_but = driver.find_element(*TestLocators.BUTTON_CHECKOUT)
    assert order_but.is_displayed()

# Проверка конструктора, переключение на вкладку Соусы
def test_slide_constructor_sauces(setup_driver):
    driver = setup_driver
    # Проверка конструктора
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.LOGIN_TO_ACCOUUNT))
    driver.find_element(*TestLocators.LOGIN_TO_ACCOUUNT).click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.LOGIN))
    driver.find_element(*TestLocators.AUTOR_EMAIL).send_keys(USER_EMAIL)
    driver.find_element(*TestLocators.AUTOR_PASSWORD).send_keys(USER_PASSWORD)
    driver.find_element(*TestLocators.LOGIN_TO_ACCOUUNT_REG).click()
    WebDriverWait(driver,3).until(
        EC.visibility_of_element_located(TestLocators.BUTTON_SAUCE)
    )
    driver.find_element(*TestLocators.BUTTON_SAUCE).click()
    sauces_tab = driver.find_element(*TestLocators.SAUCES_TAB)
    assert sauces_tab.is_displayed(), "Вкладка 'Соусы' является текущей активной вкладкой"
def test_slide_constructor_filling(setup_driver):
    driver = setup_driver
    # Проверка конструктора
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.LOGIN_TO_ACCOUUNT))
    driver.find_element(*TestLocators.LOGIN_TO_ACCOUUNT).click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.LOGIN))
    driver.find_element(*TestLocators.AUTOR_EMAIL).send_keys(USER_EMAIL)
    driver.find_element(*TestLocators.AUTOR_PASSWORD).send_keys(USER_PASSWORD)
    driver.find_element(*TestLocators.LOGIN_TO_ACCOUUNT_REG).click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.BUTTON_SAUCE)
    )
    driver.find_element(*TestLocators.BUTTON_FILLING).click()
    filling_tab = driver.find_element(*TestLocators.FILLING_TAB)
    assert filling_tab.is_displayed(), "Вкладка 'Начинки' является текущей активной вкладкой"

def test_slide_constructor_bread(setup_driver):
    driver = setup_driver
    # Проверка конструктора
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.LOGIN_TO_ACCOUUNT))
    driver.find_element(*TestLocators.LOGIN_TO_ACCOUUNT).click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.LOGIN))
    driver.find_element(*TestLocators.AUTOR_EMAIL).send_keys(USER_EMAIL)
    driver.find_element(*TestLocators.AUTOR_PASSWORD).send_keys(USER_PASSWORD)
    driver.find_element(*TestLocators.LOGIN_TO_ACCOUUNT_REG).click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(TestLocators.BUTTON_SAUCE)
    )
    driver.find_element(*TestLocators.BUTTON_FILLING).click()
    driver.find_element(*TestLocators.BUTTON_BREAD).click()
    bread_tab = driver.find_element(*TestLocators.BREAD_TAB)
    assert bread_tab.is_displayed(), "Вкладка 'Булки' является текущей активной вкладкой"
