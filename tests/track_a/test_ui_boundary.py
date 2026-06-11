"""Track A — UI / Boundary (Dual-Track RED skeleton)."""

import pytest

from unit_converter.validator import validate_lines


@pytest.mark.track_a
@pytest.mark.test_id("U-IN-01")
def test_u_in_01_empty_input_format_error():
    """Given: [''] → Then: status=fail (빈 입력 형식 오류)"""
    grid = [""]

    result = validate_lines(grid)

    assert result["status"] == "fail"
    assert len(result["failed_lines"]) >= 1


@pytest.mark.track_a
@pytest.mark.test_id("U-IN-02")
def test_u_in_02_missing_colon_format_error():
    """Given: ['meter'] → Then: status=fail (콜론 없음)"""
    grid = ["meter"]

    result = validate_lines(grid)

    assert result["status"] == "fail"
    assert result["failed_lines"][0]["line"] == "meter"


@pytest.mark.track_a
@pytest.mark.test_id("U-IN-03")
def test_u_in_03_negative_value_rejected():
    """Given: ['meter:-10'] → Then: status=fail, failed_lines 포함"""
    grid = ["meter:-10"]

    result = validate_lines(grid)

    assert result["status"] == "fail"
    assert len(result["failed_lines"]) >= 1
    assert result["failed_lines"][0]["line"] == "meter:-10"


@pytest.mark.track_a
@pytest.mark.test_id("U-OUT-01")
def test_u_out_01_meter_2_5_outputs_three_or_more_lines():
    """Given: 3줄 이상 변환 출력 → Then: status=pass"""
    grid = [
        "2.5 meter = 8.2 feet",
        "2.5 meter = 2.7 yard",
        "2.5 meter = 2.5 meter",
    ]

    result = validate_lines(grid)

    assert result["status"] == "pass"
    assert result["failed_lines"] == []
