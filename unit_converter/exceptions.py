class ParseError(Exception):
    """FR-05: 잘못된 입력 형식."""


class ValidationError(Exception):
    """FR-04: 유효하지 않은 값 (음수 등)."""


class UnknownUnitError(ValidationError):
    """FR-03: 등록되지 않은 단위."""


class ConfigError(Exception):
    """D-CFG-01: 깨진 JSON 설정 파일."""
