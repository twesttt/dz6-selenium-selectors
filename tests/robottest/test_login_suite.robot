*** Settings ***
Library  SeleniumLibrary
#Library  MyLib
Library  login_client.py
Library  login_admin.py
Suite Teardown  Close Browser

*** Test Cases ***
The user can login as Admin
        ${driver}   Open Opencart Admin Login Page
        Login As Admin     ${driver}   admin   admin
The user can login as Client
        ${driver}   Open Opencart Client Login Page
        Login As Client     ${driver}   test@gmail.com  test

