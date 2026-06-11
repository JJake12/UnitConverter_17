import pytest

from unit_converter.exceptions import ParseError
from unit_converter.parser import InputParser


@pytest.mark.requirement("FR-01")
def test_fr01_parse_valid_input():
    """TEST-FR-01: meter:2.5 → value=2.5, unit=meter"""
    parsed = InputParser().parse("meter:2.5")
    assert parsed.value == 2.5
    assert parsed.unit == "meter"
