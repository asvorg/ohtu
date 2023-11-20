*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  aapo
    Set Password  aapoo123
    Set Password Confirmation  aapoo123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  a
    Set Password  aapoo123
    Set Password Confirmation  aapoo123
    Submit Credentials
    Register Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  aapo
    Set Password  a
    Set Password Confirmation  a
    Submit Credentials
    Register Should Fail With Message  Password must be at least 8 characters long

Register With Nonmatching Password And Password Confirmation
    Set Username  aapo
    Set Password  aapo12345
    Set Password Confirmation  aapo123456
    Submit Credentials
    Register Should Fail With Message  Password and password confirmation do not match



Login After Successful Registration
    Set Username  aapo
    Set Password  aapo12345
    Set Password Confirmation  aapo12345
    Submit Credentials
    Register Should Succeed
    Go To Login Page
    Login Page Should Be Open



Login After Failed Registration
    Set Username  aapo
    Set Password  aapo12345
    Set Password Confirmation  aapo123456
    Submit Credentials
    Register Should Fail With Message  Password and password confirmation do not match


*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}