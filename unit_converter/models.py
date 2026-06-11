from dataclasses import dataclass


@dataclass(frozen=True)
class ParsedInput:
    unit: str
    value: float


@dataclass(frozen=True)
class ConversionResult:
    source_unit: str
    source_value: float
    target_unit: str
    target_value: float
