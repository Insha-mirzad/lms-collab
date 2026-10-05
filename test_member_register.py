import pytest
from member_register import MemberRegistry

@pytest.fixture
def registry():
    """Provides a fresh instance of MemberRegistry for each test."""
    return MemberRegistry()

def test_register_valid_member(registry):
    """Ensures a valid member can be successfully registered."""
    assert registry.register("M01", "Anu", "anu@mbcet.ac.in") is True
    assert registry.count() == 1

def test_duplicate_id_rejected(registry):
    """Ensures registering an already existing Member ID raises a ValueError."""
    registry.register("M01", "Anu", "anu@mbcet.ac.in")
    with pytest.raises(ValueError, match="Member ID already exists"):
        registry.register("M01", "Rahul", "rahul@mbcet.ac.in")

def test_invalid_email_rejected(registry):
    """Ensures an invalid email format without '@' throws a ValueError."""
    with pytest.raises(ValueError, match="Invalid email"):
        registry.register("M02", "Rahul", "rahul.mbcet")
