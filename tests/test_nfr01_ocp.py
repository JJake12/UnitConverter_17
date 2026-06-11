import inspect

import pytest

from unit_converter.converter import UnitConverter
from unit_converter.models import ParsedInput
from unit_converter.registry import UnitRegistry


@pytest.mark.requirement("NFR-01")
def test_nfr01_add_unit_without_modifying_converter(registry):
    """TEST-NFR-01: add inch without changing Converter source"""
    converter_source_before = inspect.getsource(UnitConverter.convert_all)

    registry.register("inch", meters_per_unit=0.0254)
    converter = UnitConverter(registry)
    results = converter.convert_all(ParsedInput(unit="inch", value=12.0))

    by_unit = {r.target_unit: r.target_value for r in results}
    assert "inch" in by_unit
    assert by_unit["meter"] == pytest.approx(12.0 * 0.0254)

    converter_source_after = inspect.getsource(UnitConverter.convert_all)
    assert converter_source_before == converter_source_after
