import importlib
import inspect

import pytest


@pytest.mark.requirement("NFR-02")
def test_nfr02_components_exist_and_separated():
    """TEST-NFR-02: Parser / Registry / Converter / Printer 분리"""
    parser_mod = importlib.import_module("unit_converter.parser")
    registry_mod = importlib.import_module("unit_converter.registry")
    converter_mod = importlib.import_module("unit_converter.converter")
    printer_mod = importlib.import_module("unit_converter.printer")

    assert hasattr(parser_mod, "InputParser")
    assert hasattr(registry_mod, "UnitRegistry")
    assert hasattr(converter_mod, "UnitConverter")
    assert hasattr(printer_mod, "ResultPrinter")

    converter_source = inspect.getsource(converter_mod.UnitConverter)
    assert "print(" not in converter_source
    assert "input(" not in converter_source

    parser_source = inspect.getsource(parser_mod.InputParser)
    assert "print(" not in parser_source
