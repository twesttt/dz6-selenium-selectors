from selenium import webdriver
from selenium.webdriver.common.by import By
from robot.api.deco import keyword


# class LoginAsAdmin:
USERNAME = "#input-username"
PASSWORD = "#input-password"
FORGOTTEN_PASSWORD = "span.help-block a"
LOGIN = "button[type='submit']"

@keyword("Open Opencart Admin Login Page")
def driver():
    browser = webdriver.Chrome()
    browser.get("http://localhost/opencart/admin")
    return browser

@keyword('Login As Admin')
def admin_login(driver, name, password):
    input_username = driver.find_element(By.CSS_SELECTOR, USERNAME)
    input_username.send_keys(name)
    password_field = driver.find_element(By.CSS_SELECTOR, PASSWORD)
    password_field.clear()
    password_field.send_keys(password)
    driver.find_element(By.CSS_SELECTOR, LOGIN).click()
    assert driver.title == 'Dashboard'
