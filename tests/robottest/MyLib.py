from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from robot.api.deco import keyword
from ..login_methods import LoginAsAdmin, LoginAsClient


class MyLib:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    @keyword("Open Opencart Admin Login Page")
    def get_admin_login_page(self):
        LoginAsAdmin.driver()

    @keyword('Login As Admin')
    def login_as_admin(self, driver, name, password):
        LoginAsAdmin.admin_login(driver, name, password)

    @keyword("Open Opencart Client Login Page")
    def get_client_login_page(self):
        LoginAsClient.driver()

    @keyword('Login As Client')
    def login_as_client(self, driver, email, password):
        LoginAsAdmin.admin_login(driver, email, password)
