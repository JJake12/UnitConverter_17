from unit_converter.exceptions import UnknownUnitError

METER_TO_FEET = 3.28084
METER_TO_YARD = 1.09361


class UnitRegistry:
    """NFR-01 OCP 확장점: 단위·비율 등록 및 조회."""

    def __init__(self) -> None:
        self._meters_per_unit: dict[str, float] = {}

    @classmethod
    def default(cls) -> "UnitRegistry":
        registry = cls()
        registry.register("meter", meters_per_unit=1.0)
        registry.register("feet", meters_per_unit=1.0 / METER_TO_FEET)
        registry.register("yard", meters_per_unit=1.0 / METER_TO_YARD)
        return registry

    def register(self, name: str, *, meters_per_unit: float) -> None:
        if meters_per_unit <= 0:
            raise ValueError("meters_per_unit must be positive")
        self._meters_per_unit[name] = meters_per_unit

    def has_unit(self, name: str) -> bool:
        return name in self._meters_per_unit

    def get_meters_per_unit(self, name: str) -> float:
        if name not in self._meters_per_unit:
            raise UnknownUnitError(f"Unknown unit: {name}")
        return self._meters_per_unit[name]

    def all_units(self) -> dict[str, float]:
        return dict(self._meters_per_unit)

    def load_from_file(self, path: str) -> None:
        from unit_converter.config_loader import ConfigLoader

        ConfigLoader.load_into_registry(path, self)
