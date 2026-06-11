from unit_converter.models import ConversionResult, ParsedInput
from unit_converter.registry import UnitRegistry


class UnitConverter:
    """FR-02: meter 기준 전 단위 변환 (단위별 분기 없음 — NFR-01)."""

    def __init__(self, registry: UnitRegistry) -> None:
        self._registry = registry

    def to_meter(self, value: float, unit: str) -> float:
        return value * self._registry.get_meters_per_unit(unit)

    def convert_all(self, parsed: ParsedInput) -> list[ConversionResult]:
        meters = parsed.value * self._registry.get_meters_per_unit(parsed.unit)
        results: list[ConversionResult] = []

        for unit_name, meters_per_unit in self._registry.all_units().items():
            target_value = meters / meters_per_unit
            results.append(
                ConversionResult(
                    source_unit=parsed.unit,
                    source_value=parsed.value,
                    target_unit=unit_name,
                    target_value=target_value,
                )
            )

        return results
