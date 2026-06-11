"""validate_lines — 경계 검증 RED."""

import pytest

from unit_converter.validator import validate_lines


@pytest.mark.test_id("U-IN-03")
def test_validate_lines_returns_fail_for_meter_minus_10():
    """Given: 'meter:-10' (음수 입력) → Then: status fail, failed_lines에 해당 줄 표현"""
    grid = ["meter:-10"]

    result = validate_lines(grid)

    assert result["status"] == "fail"
    assert len(result["failed_lines"]) >= 1
    failed = result["failed_lines"][0]
    assert failed["index"] == 0
    assert failed["line"] == "meter:-10"
