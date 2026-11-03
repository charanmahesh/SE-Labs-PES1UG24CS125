import pytest

from attendance_eligibility import (
    attendance_percent,
    attendance_warning,
    exam_eligibility,
)


def test_attendance_percent_validates_inputs():
    with pytest.raises(ValueError, match="invalid total"):
        attendance_percent(0, 0, 0)
    with pytest.raises(ValueError, match="invalid attended count"):
        attendance_percent(-1, 10, 0)
    with pytest.raises(ValueError, match="invalid attended count"):
        attendance_percent(11, 10, 0)


def test_attendance_percent_caps_medical_leave_and_credited_classes():
    assert attendance_percent(10, 20, 0) == 50
    assert attendance_percent(10, 20, 7) == 75
    assert attendance_percent(19, 20, 3) == 100


def test_exam_eligibility_covers_each_decision_branch():
    assert exam_eligibility(80, False, False) == "fees pending"
    assert exam_eligibility(75, False, True) == "eligible"
    assert exam_eligibility(65, True, True) == "eligible"
    assert exam_eligibility(65, False, True) == "condonation required"
    assert exam_eligibility(64, False, True) == "detained"


def test_attendance_warning_covers_each_decision_branch():
    assert attendance_warning(85, 0) is None
    assert attendance_warning(74, 5) == "critical"
    assert attendance_warning(74, 4) == "final notice"
    assert attendance_warning(75, 0) == "reminder"
