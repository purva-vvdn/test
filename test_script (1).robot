*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${URL}            https://example.com/login
${BROWSER}        chrome
${USERNAME}       testuser
${PASSWORD}       password123

*** Test Cases ***
Verify Login Functionality
    Open Browser    ${URL}    ${BROWSER}
    Input Text      id=username    ${USERNAME}
    Input Text      id=password    ${PASSWORD}
    Click Button    id=loginButton
    Wait Until Page Contains Element    xpath=//div[@id="welcomeMessage"]
    Capture Page Screenshot
    Close Browser

