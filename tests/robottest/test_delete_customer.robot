*** Settings ***
Library  SeleniumLibrary
Resource  common.robot

*** Keywords ***

Delete Customer
    Click Link      //*[@id="menu-customer"]/a
    Click Link      //*[@id="collapse5"]/li[1]/a
    Select Checkbox     //*[@id="form-customer"]/table/tbody/tr/td[1]/input
    Click Button    css:button[data-original-title='Delete']
    Alert Should Be Present     action=ACCEPT
    Element Should Not Be Visible       //*[@id="form-customer"]/table/tbody/tr/td[2]


*** Test Cases ***
The user with admin role can add another user
        User Login  admin
        Delete Customer
        Close Browser
