import pytest


def get_data():
    return [

        ("mahendra","Pass"),
        ("MAK", "PAss"),
        ("Test","Passss")
    ]

@pytest.mark.parametrize("username,password",get_data())
def test_doLogin (username, password ) :
    print (username + " -------- " + password )
