import pytest

def test_validate_title():
    expected_title = " M Great"
    actual_title = "I M Great"

    # if actual_title == expected_title:
    #     print("Test Case Passed")
    # else:
    #     print("Test Case Failed")

    assert expected_title == actual_title, " The Titles are not Matching"

    assert "Mahendra" in actual_title, "Mahendra is not there in title"
    assert False, "Forceful Failure"