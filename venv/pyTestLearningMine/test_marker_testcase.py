import pytest

@pytest.mark.functional
def test_doLogin ( ) :
    print ( "Executing Login Test Case" )

@pytest.mark.regression
def test_doRegister ( ) :
    print ( "Executing Registeration Test Case" )

@pytest.mark.functional
def test_doLogout ( ) :
    print ( "Executing Logout Test Case" )

@pytest.mark.skip
def test_skipping():
    print("Skipping Test")
