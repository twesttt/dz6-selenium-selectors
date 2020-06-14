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


Add User
    [Arguments]      ${USER_NAME}
    Click Link      //*[@id="menu-system"]/a
    Click Link      //*[@id="collapse7"]/li[2]/a
    Click Link      //*[@id="collapse7-1"]/li[1]/a
    Click Link      //*[@id="content"]/div[1]/div/div/a
    Input Text      id:input-username   ${USER_NAME}
    Select From List by Value   id:input-user-group     10
    Input Text      id:input-firstname  ${USER_NAME}
    Input Text      id:input-lastname   ${USER_NAME}
    Input Text      id:input-email      test@gmail.com
    Input Text      id:input-password   ${USER_NAME}
    Input Text      id:input-confirm    ${USER_NAME}
    Select From List by Value   id:input-status     1
    Click Button    css:button[type='submit']
    Element Should Be Visible       //*[@id="form-user"]/div/table/tbody/tr[3]/td[2]


Delete User
    [Arguments]      ${USER_NAME}
    Click Link      //*[@id="menu-system"]/a
    Click Link      //*[@id="collapse7"]/li[2]/a
    Click Link      //*[@id="collapse7-1"]/li[1]/a
    Select Checkbox     //*[@id="form-user"]/div/table/tbody/tr[3]/td[1]/input
    Click Button    css:button[data-original-title='Delete']
    Alert Should Be Present     action=ACCEPT
    Element Should Not Be Visible       //*[@id="form-user"]/div/table/tbody/tr[3]/td[2]