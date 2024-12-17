*** Settings ***
Documentation     A test suite with a single test for New Tab
...               Created by hats' Robotcorder
Library           SeleniumLibrary    timeout=10

*** Variables ***
${BROWSER}    chrome
${SLEEP}      10

*** Test Cases ***
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver
    Call Method    ${options}    add_argument    --headless
    Call Method    ${options}    add_argument    --no-sandbox
    Call Method    ${options}    add_argument    --disable-dev-shm-usage
    Call Method    ${options}    add_argument    --disable-gpu
    Open Browser    https://www.google.com/search?q=al+projects&oq=al+projects&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQABiABDIMCAIQABgKGLEDGIAEMgwIAxAAGAoYsQMYgAQyCQgEEAAYChiABDIJCAUQABgKGIAEMgkIBhAAGAoYgAQyCQgHEAAYChiABDIJCAgQABgKGIAEMgkICRAAGAoYgATSAQk1NjIyajBqMTWoAgiwAgE&sourceid=chrome&ie=UTF-8    ${BROWSER}    options=${options}
    Wait Until Element Is Visible    xpath=(//h3[@class="LC20lb    timeout=5
    Click Element    xpath=(//h3[@class="LC20lb
    Wait Until Element Is Visible    xpath=(//img)[3]    timeout=5
    Click Element    xpath=(//img)[3]
    Close Browser
