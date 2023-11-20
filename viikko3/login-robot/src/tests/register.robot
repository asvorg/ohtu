*** Settings ***
Resource    resource.robot
Library    AppLibrary
Test Setup    Create User And Input Login Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials   aapo    timo1234
    Output Should Contain   New user registered

Register With Already Taken Username And Valid Password
    Input Credentials   aapo    timo1234
    Output Should Contain   User with username aapo already exists

Register With Too Short Username And Valid Password
    Input Credentials   a    a
    Output Should Contain   Invalid username format

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials   !!!!!!!!!!!!!!!    timo1234
    Output Should Contain   Invalid username format

Register With Valid Username And Too Short Password
    Input Credentials   aapo    a
    Output Should Contain   Invalid password

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials   aapo    asdfghjklqwe
    Output Should Contain   New user registered

*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kalle123
    AppLibrary.Input New Command  login  kalle  kalle123

Input Credentials
    [Arguments]  ${username}  ${password}
    AppLibrary.Input New Command  login  ${username}  ${password}

Output Should Contain
    [Arguments]    ${expected_output}
    # Implement the logic to check if the expected output is present
    # This might involve calling a method in your AppLibrary or other relevant code
    Log    Verifying output: ${expected_output}