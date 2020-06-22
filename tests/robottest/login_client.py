from selenium import webdriver
from selenium.webdriver.common.by import By
from robot.api.deco import keyword

# class LoginAsClient:
MY_ACCOUNT = "//*[@id='top-links']/ul/li[2]/a"
LOGIN = "//*[@id='top-links']/ul/li[2]/ul/li[2]/a"
EMAIL = "#input-email"
PASSWORD = "#input-password"
LOGIN_SUBMIT = "//*[@id='content']/div/div[2]/div/form/input"

@keyword("Open Opencart Client Login Page")
def driver():
    browser = webdriver.Chrome()
    browser.get("http://localhost/opencart/")
    browser.find_element(By.XPATH, MY_ACCOUNT).click()
    browser.find_element(By.XPATH, LOGIN).click()
    return browser

@keyword('Login As Client')
def admin_login(driver, email, password):
    input_email = driver.find_element(By.CSS_SELECTOR, EMAIL)
    input_email.send_keys(email)
    password_field = driver.find_element(By.CSS_SELECTOR, PASSWORD)
    password_field.clear()
    password_field.send_keys(password)
    driver.find_element(By.XPATH, LOGIN_SUBMIT).click()
    assert driver.title == 'My Account'
