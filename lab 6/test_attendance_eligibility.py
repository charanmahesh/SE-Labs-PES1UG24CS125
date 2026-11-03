import pytest
from attendance_eligibility import attendance_percent, exam_eligibility, attendance_warning

#Example test cases:
def test_plain_percent():
    assert attendance_percent(30, 40, 0) == 75

def test_eligible():
    assert exam_eligibility(80, False, True) == "eligible"


def test_attendance_percent_validation_and_credits():
    with pytest.raises(ValueError, match="invalid total"):
        attendance_percent(0, 0, 0)
    with pytest.raises(ValueError, match="invalid attended count"):
        attendance_percent(-1, 10, 0)
    assert attendance_percent(10, 20, 7) == 75
    assert attendance_percent(19, 20, 3) == 100


def test_exam_eligibility_other_outcomes():
    assert exam_eligibility(80, False, False) == "fees pending"
    assert exam_eligibility(65, False, True) == "condonation required"
    assert exam_eligibility(64, False, True) == "detained"


def test_attendance_warning_noncritical_outcomes():
    assert attendance_warning(85, 0) is None
    assert attendance_warning(74, 4) == "final notice"
    assert attendance_warning(75, 0) == "reminder"


def test_attendance_percent_rejects_attendance_above_total():
    with pytest.raises(ValueError, match="invalid attended count"):
        attendance_percent(11, 10, 0)


def test_exam_eligibility_with_condonation():
    assert exam_eligibility(65, True, True) == "eligible"


def test_attendance_warning_critical_with_more_than_four_weeks_left():
    assert attendance_warning(74, 5) == "critical"
