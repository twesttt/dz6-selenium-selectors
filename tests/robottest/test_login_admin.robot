*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${URL}          http://localhost/opencart/admin
${BROWSER}      Chrome

*** Keywords ***
The user can login
    [Arguments]      ${USER_NAME}
    Open browser    ${URL}   ${BROWSER}
    Input Text      id:input-username     ${USER_NAME}
    Input Text      id:input-password     ${USER_NAME}
    Click Button    css:button[type='submit']
    Title Should Be  Dashboard
    Close Browser


*** Test Cases ***
The user can login under Admin user
        The user can login  admin
The user can login under Demo user
        The user can login  demo
