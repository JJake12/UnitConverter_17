from unit_converter.converter import UnitConverter
from unit_converter.exceptions import ParseError, ValidationError
from unit_converter.parser import InputParser
from unit_converter.printer import ResultPrinter
from unit_converter.registry import UnitRegistry
from unit_converter.validator import InputValidator


class Application:
    """Parser → Validator → Converter → Printer 오케스트레이션."""

    def __init__(self, registry: UnitRegistry) -> None:
        self._parser = InputParser()
        self._validator = InputValidator(registry)
        self._converter = UnitConverter(registry)
        self._printer = ResultPrinter()

    def process(self, raw: str, output_format: str = "table") -> str:
        parsed = self._parser.parse(raw)
        self._validator.validate(parsed)
        results = self._converter.convert_all(parsed)
        return self._printer.print(results, fmt=output_format)  # type: ignore[arg-type]

    def run(self) -> None:
        raw = input("Insert value for converting (ex: meter:2.5): ")
        try:
            print(self.process(raw))
        except (ParseError, ValidationError) as exc:
            print(str(exc))
