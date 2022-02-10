import pytest

def setup_module(module):
    print("Opening DB Connection")

def teardown_module(Module):
    print("Closing DB Connection")

def setup_function(function):
    print("Launching Browser")

def teardown_function(function):
    print("Closing the Browser")

def test_doLogin():
    print("Executing Login Test Case")

def test_doRegister():
    print("Executing Registeration Test Case")