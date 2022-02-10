import pytest

pytest.fixture ( scope = "module" )


def setupModule ( ) :
    print ( "Opening DB Connection" )

    yield
    print ( "Closing DB Connection" )


pytest.fixture ( scope = "function" )


def setupFunction ( ) :
    print ( "Launching Browser" )

    yield
    print ( "Closing the Browser" )


def test_doLogin ( ) :
    print ( "Executing Login Test Case" )


def test_doRegister ( ) :
    print ( "Executing Registeration Test Case" )
