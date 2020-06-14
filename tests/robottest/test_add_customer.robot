*** Settings ***
Library  SeleniumLibrary
Resource  test_login.robot
#Resource  test_delete_user.robot

*** Variables ***
${URL}          http://localhost/opencart/admin
${BROWSER}      Chrome
${CUSTOMER_URL}     http://localhost/opencart/

*** Keywords ***
User Login
    [Arguments]      ${USER_NAME}
    Open browser    ${URL}   ${BROWSER}
    Set Selenium Speed  0.1
    Input Text      id:input-username     ${USER_NAME}
    Input Text      id:input-password     ${USER_NAME}
    Click Button    css:button[type='submit']
    Title Should Be  Dashboard

Add Customer
    [Arguments]      ${CUSTOMER_NAME}   ${CUSTOMER_EMAIL}
    Click Link      //*[@id="menu-customer"]/a
    Click Link      //*[@id="collapse5"]/li[1]/a
    Click Link      //*[@id="content"]/div[1]/div/div/a
    Input Text      id:input-firstname  ${CUSTOMER_NAME}
    Input Text      id:input-lastname   ${CUSTOMER_NAME}
    Input Text      id:input-email      ${CUSTOMER_EMAIL}
    Input Text      id:input-telephone  ${CUSTOMER_NAME}
    Input Text      id:input-password   ${CUSTOMER_NAME}
    Input Text      id:input-confirm    ${CUSTOMER_NAME}
    Select From List by Value   id:input-status     1
    Click Button    css:button[type='submit']
    Element Should Be Visible       //*[@id="form-customer"]/table/tbody/tr/td[2]


Customer Login
    [Arguments]     ${CUSTOMER_EMAIL}  ${CUSTOMER_PASSWORD}
    Open browser    ${CUSTOMER_URL}
    Set Selenium Speed  0.1
    Click Link      //*[@id="top-links"]/ul/li[2]/a
    Click Link      //*[@id="top-links"]/ul/li[2]/ul/li[2]/a
    Input Text      id:input-email   ${CUSTOMER_EMAIL}
    Input Text      id:input-password   test
    Submit Form     //*[@id="content"]/div/div[2]/div/form
    Title Should Be     My Account


*** Test Cases ***
The user with admin role can add customer
        User Login  admin
        Add Customer   test   test@gmail.com
        Close Browser
New customer can login
        Customer Login  test@gmail.com    test
        Close Browser