"""Track A — UI / Boundary (Dual-Track RED skeleton)."""

import pytest


@pytest.mark.track_a
@pytest.mark.test_id("U-IN-01")
def test_u_in_01_empty_input_format_error():
    """Given: '' (빈 입력) → Then: 형식 오류 메시지"""
    pytest.fail("RED: U-IN-01 — empty input must produce format error message")


@pytest.mark.track_a
@pytest.mark.test_id("U-IN-02")
def test_u_in_02_missing_colon_format_error():
    """Given: 'meter' (콜론 없음) → Then: 형식 오류"""
    pytest.fail("RED: U-IN-02 — input without colon must produce format error")


@pytest.mark.track_a
@pytest.mark.test_id("U-IN-03")
def test_u_in_03_negative_value_rejected():
    """Given: 'meter:-1' → Then: 음수 거부"""
    pytest.fail("RED: U-IN-03 — negative value must be rejected")


@pytest.mark.track_a
@pytest.mark.test_id("U-OUT-01")
def test_u_out_01_meter_2_5_outputs_three_or_more_lines():
    """Given: 'meter:2.5' → Then: 3줄 이상 출력 (스켈레톤)"""
    pytest.fail("RED: U-OUT-01 — meter:2.5 must output 3 or more conversion lines")
