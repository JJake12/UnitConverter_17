import json
from pathlib import Path

from unit_converter.registry import UnitRegistry


class ConfigLoader:
    """EXT-01: JSON/YAML 설정 파일에서 비율 로드."""

    @staticmethod
    def load_into_registry(path: str | Path, registry: UnitRegistry) -> None:
        file_path = Path(path)
        suffix = file_path.suffix.lower()

        if suffix == ".json":
            data = json.loads(file_path.read_text(encoding="utf-8"))
        elif suffix in (".yaml", ".yml"):
            try:
                import yaml
            except ImportError as exc:
                raise ImportError("PyYAML is required for YAML config files") from exc
            data = yaml.safe_load(file_path.read_text(encoding="utf-8"))
        else:
            raise ValueError(f"Unsupported config format: {suffix}")

        units = data.get("units", data)
        for name, meters_per_unit in units.items():
            registry.register(name, meters_per_unit=float(meters_per_unit))
