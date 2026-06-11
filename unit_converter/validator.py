from unit_converter.exceptions import UnknownUnitError, ValidationError
from unit_converter.models import ParsedInput
from unit_converter.registry import UnitRegistry


class InputValidator:
    """FR-03, FR-04: 파싱 결과 검증."""

    def __init__(self, registry: UnitRegistry) -> None:
        self._registry = registry

    def validate(self, parsed: ParsedInput) -> None:
        if parsed.value < 0:
            raise ValidationError(f"Negative value not allowed: {parsed.value}")

        if not self._registry.has_unit(parsed.unit):
            raise UnknownUnitError(f"Unknown unit: {parsed.unit}")


def validate_lines(grid: list[str]) -> dict:
    failed_lines: list[dict] = []

    for index, line in enumerate(grid):
        if line == "":
            failed_lines.append({"index": index, "line": line})
            continue

        if " = " not in line and ":" not in line:
            failed_lines.append({"index": index, "line": line})
            continue

        if " = " not in line:
            _, value_str = line.split(":", 1)
            try:
                value = float(value_str.strip())
            except ValueError:
                failed_lines.append({"index": index, "line": line})
                continue

            if value < 0:
                failed_lines.append({"index": index, "line": line})

    if failed_lines:
        return {"status": "fail", "failed_lines": failed_lines}

    return {"status": "incomplete", "failed_lines": []}
