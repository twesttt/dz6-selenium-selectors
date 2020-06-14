*** Settings ***
Library  SeleniumLibrary
Resource  common.robot

*** Test Cases ***
Kind of setup
        User Login  admin
        Add User  test
        Close Browser
The user with admin role can add another user
        User Login  admin
        Delete User   test
        Close Browser
