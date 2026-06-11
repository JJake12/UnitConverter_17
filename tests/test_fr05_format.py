import pytest

from unit_converter.exceptions import ParseError
from unit_converter.parser import InputParser


@pytest.mark.requirement("FR-05")
@pytest.mark.parametrize("raw", ["meter/abc", "meter2.5"])
def test_fr05_invalid_format_error(raw):
    """TEST-FR-05: invalid format → ParseError"""
    with pytest.raises(ParseError):
        InputParser().parse(raw)
