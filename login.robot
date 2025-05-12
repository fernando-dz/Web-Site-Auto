*** Settings ***
Library     Browser
Resource    Web-keys.robot
*** Variables ***
*** Test Cases ***
Login To Acme
    Launch Acme Login   chromium
    Launch Acme Login   webkit
    Launch Acme Login   firefox
Bad Logins
    Launch Acme     chromium
    AcmeBank Bad User
    Launch Acme     webkit
    Acmebank Bad User+Pass