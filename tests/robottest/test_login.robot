*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${URL}          http://localhost/opencart/admin
${BROWSER}      Chrome

*** Keywords ***
User Login
    [Arguments]      ${USER_NAME}
    Open browser    ${URL}   ${BROWSER}
    Input Text      id:input-username     ${USER_NAME}
    Input Text      id:input-password     ${USER_NAME}
    Click Button    css:button[type='submit']
    Title Should Be  Dashboard


*** Test Cases ***
The user can login under Admin user
        User Login  admin
        Close Browser
The user can login under Demo user
        User Login  demo
        Close Browser
