*** Settings ***
Library    AppLibrary
Resource    resource.robot
Test Setup    Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials   aapo    timo1234
    Output Should Contain   asdsad
Register With Already Taken Username And Valid Password
# ...

Register With Too Short Username And Valid Password
# ...

Register With Enough Long But Invalid Username And Valid Password
# ...

Register With Valid Username And Too Short Password
# ...

Register With Valid Username And Long Enough Password Containing Only Letters
# ...