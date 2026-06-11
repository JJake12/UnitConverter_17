from unit_converter.exceptions import ParseError
from unit_converter.models import ParsedInput


class InputParser:
    """FR-01, FR-05: unit:value 문자열 파싱."""

    def parse(self, raw: str) -> ParsedInput:
        if ":" not in raw:
            raise ParseError("Invalid format. Use unit:value (ex: meter:2.5)")

        unit, value_str = raw.split(":", 1)
        unit = unit.strip()
        value_str = value_str.strip()

        if not unit:
            raise ParseError("Invalid format. Use unit:value (ex: meter:2.5)")

        try:
            value = float(value_str)
        except ValueError as exc:
            raise ParseError(f"Invalid number: {value_str}") from exc

        return ParsedInput(unit=unit, value=value)
