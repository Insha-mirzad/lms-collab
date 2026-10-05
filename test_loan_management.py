from datetime import date
import pytest
from loan_management import due_date, calculate_fine

def test_due_date_is_14_days():
    """Ensures the loan period is exactly 14 days."""
    assert due_date(date(2026, 10, 1)) == date(2026, 10, 15)

def test_no_fine_when_on_time():
    """Ensures no fine is charged if returned exactly on the due date."""
    assert calculate_fine(date(2026, 10, 1), date(2026, 10, 15)) == 0

def test_fine_for_3_days_late():
    """Ensures late fine calculates correctly ($2 per day * 3 days = $6)."""
    assert calculate_fine(date(2026, 10, 1), date(2026, 10, 18)) == 6

def test_return_before_issue_raises():
    """Ensures a ValueError is raised if chronological dates are impossible."""
    with pytest.raises(ValueError):
        calculate_fine(date(2026, 10, 5), date(2026, 10, 1))
