*** Settings ***
Library  SeleniumLibrary
Resource  common.robot


*** Test Cases ***
The user with admin role can add another user
        User Login  admin
        Add User   test
        Close Browser
New user can login
        User Login  test
        Close Browser
Kind of teardown
        User Login  admin
        Delete User  test
        Closer Browser