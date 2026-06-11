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
