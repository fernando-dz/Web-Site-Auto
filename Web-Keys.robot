*** Settings ***
Library     Browser
Library     OperatingSystem
*** Variables ***

#USERS -
${domainuser}   testbot
${domainemail}  @example.com
${username}     ${domainuser}${domainemail}
${password}    gibberish


*** Keywords ***
### Login ###
AcmeBank Login
    [ARGUMENTS]     ${username}
    Fill Text       //*[@id="username"]       $username
    Click           //*[@id="log-in"]
    wait for elements state     //html/body/div/div[3]/div[1]/div/div/div[2]/div[2]    visible

AcmeBank Bad User+Pass
    ${secret}    Get Environment Variable    SECRET
    Fill Text       //*[@id="username"]    Wild - no domain, and some punctuation too.
    Fill Secret     //*[@id="password"]    $secret
    Click           //*[@id="log-in"]
    ${errorResult}    wait for elements state     //html/body/div/div/h4    visible     timeout=1
    pass execution if  ${errorResult}==Pass

AcmeBank Bad User
    ${secret}    Get Environment Variable    SECRET
    Fill Text       //*[@id="username"]    Wild - no domain, and some punctuation too.
    Fill Secret     //*[@id="password"]    $secret
    Click           //*[@id="log-in"]
    ${errorResult}    wait for elements state     //html/body/div/div/h4    visible     timeout=1
    pass execution if  ${errorResult}==Pass

Launch Acme
    [ARGUMENTS]     ${browser}
    New Browser     ${browser}    headless=false
    New Page        https://demo.applitools.com

Launch Acme Login
    [ARGUMENTS]     ${browser}
    New Browser     ${browser}    headless=false
    New Page        https://demo.applitools.com
    AcmeBank Login    ${username}

### Dashboard ###
