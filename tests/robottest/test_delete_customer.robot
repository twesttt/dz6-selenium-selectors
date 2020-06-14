*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${URL}          http://localhost/opencart/admin
${BROWSER}      Chrome

*** Keywords ***
User Login
    [Arguments]      ${USER_NAME}
    Open browser    ${URL}   ${BROWSER}
    Set Selenium Speed  0.1
    Input Text      id:input-username     ${USER_NAME}
    Input Text      id:input-password     ${USER_NAME}
    Click Button    css:button[type='submit']
    Title Should Be  Dashboard


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
