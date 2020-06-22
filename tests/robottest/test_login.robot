*** Settings ***
Library  SeleniumLibrary
Resource  common.robot


*** Test Cases ***
The user can login under Admin user
        User Login  admin
        Close Browser
The user can login under Demo user
        User Login  demo
        Close Browser
