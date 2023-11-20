*** Settings ***
Resource    resource.robot
Library    AppLibrary
Test Setup    Create User And Input Login Command

*** Test Cases ***
Login With Incorrect Password
    Input Credentials    kalle    wrongpassword
    Output Should Contain    Invalid username or password

Login With Nonexistent Username
    Input Credentials    nonexistent_user    password123
    Output Should Contain    User not found

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
