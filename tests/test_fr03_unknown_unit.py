import pytest

from unit_converter.exceptions import UnknownUnitError
from unit_converter.models import ParsedInput
from unit_converter.validator import InputValidator


@pytest.mark.requirement("FR-03")
def test_fr03_unknown_unit_error(registry):
    """TEST-FR-03: cubit:1 → clear error"""
    validator = InputValidator(registry)
    with pytest.raises(UnknownUnitError, match="cubit"):
        validator.validate(ParsedInput(unit="cubit", value=1.0))
