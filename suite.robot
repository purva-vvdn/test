*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Tc_01
    Open Browser   https://the-internet.herokuapp.com/checkboxes   Chrome
    Sleep    5s
    Maximize Browser Window
    Sleep    5s
    Select Checkbox    //input[@type="checkbox"][1]
    Sleep    5s
    Unselect Checkbox    //input[@type="checkbox" and @checked][1]
    Sleep    5s
    Close Browser
    Sleep    5s