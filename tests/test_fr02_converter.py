import pytest

from unit_converter.converter import UnitConverter
from unit_converter.models import ParsedInput
from unit_converter.registry import METER_TO_FEET, METER_TO_YARD


@pytest.mark.requirement("FR-02")
def test_fr02_convert_to_all_units(registry):
    """TEST-FR-02: meter 2.5 → feet≈8.2021, yard≈2.7340"""
    converter = UnitConverter(registry)
    results = converter.convert_all(ParsedInput(unit="meter", value=2.5))

    by_unit = {r.target_unit: r.target_value for r in results}
    assert by_unit["feet"] == pytest.approx(2.5 * METER_TO_FEET)
    assert by_unit["yard"] == pytest.approx(2.5 * METER_TO_YARD)
