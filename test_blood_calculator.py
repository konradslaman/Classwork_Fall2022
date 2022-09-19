import pytest

@pytest.mark.parametrize("HDL, level" ,
    [(85, "Normal"),
    (50, "Borderline Low"),
    (30, "Low")])

def test_check_HDL(HDL, level):
    from blood_calculator import check_HDL
    answer = check_HDL(HDL)
    expected = level
    assert answer == expected

@pytest.mark.parametrize("LDL, level" ,
    [(120, "Normal"),
    (150, "Borderline High"),
    (180, "High"),
    (190, "Very High")])

def test_check_LDL(LDL, level):
    from blood_calculator import check_LDL
    answer = check_LDL(LDL)
    expected = level
    assert answer == expected

@pytest.mark.parametrize("TC, level" ,
    [(150, "Normal"),
    (210, "Borderline High"),
    (240, "High")])

def test_check_TC(TC, level):
    from blood_calculator import check_TC
    answer = check_TC(TC)
    expected = level
    assert answer == expected

"""
def test_check_HDL_BL():
    from blood_calculator import check_HDL
    answer = check_HDL(50)
    expected = "Borderline Low"
    assert answer == expected

def test_check_HDL_Low():
    from blood_calculator import check_HDL
    answer = check_HDL(30)
    expected = "Low"
    assert answer == 
"""