import pytest

from unit_converter.exceptions import ValidationError
from unit_converter.models import ParsedInput
from unit_converter.validator import InputValidator


@pytest.mark.requirement("FR-04")
def test_fr04_negative_value_rejected(registry):
    """TEST-FR-04: meter:-1 → rejected"""
    validator = InputValidator(registry)
    with pytest.raises(ValidationError, match="Negative"):
        validator.validate(ParsedInput(unit="meter", value=-1.0))
