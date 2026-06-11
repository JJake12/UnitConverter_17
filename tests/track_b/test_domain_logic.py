"""Track B — Domain / Logic (Dual-Track RED skeleton)."""

import pytest

from unit_converter.converter import UnitConverter
from unit_converter.models import ParsedInput


@pytest.mark.track_b
@pytest.mark.test_id("D-CNV-01")
def test_d_cnv_01_to_meter_one_feet(registry):
    """Given: 1 feet → Then: 0.3048 m (±ε)"""
    converter = UnitConverter(registry)

    assert converter.to_meter(1, "feet") == pytest.approx(0.3048, rel=1e-3)


@pytest.mark.track_b
@pytest.mark.test_id("D-CNV-02")
def test_d_cnv_02_convert_all_2_5_meter_to_feet(registry):
    """Given: 2.5 m → Then: 8.20210 ft (5자리)"""
    converter = UnitConverter(registry)
    results = converter.convert_all(ParsedInput(unit="meter", value=2.5))

    by_unit = {r.target_unit: r.target_value for r in results}
    assert round(by_unit["feet"], 5) == 8.20210


@pytest.mark.track_b
@pytest.mark.test_id("D-CNV-03")
def test_d_cnv_03_feet_to_yard_via_meter_consistency(registry):
    """Given: feet → yard → Then: meter 경유 일치"""
    converter = UnitConverter(registry)
    results = converter.convert_all(ParsedInput(unit="feet", value=1.0))

    by_unit = {r.target_unit: r.target_value for r in results}
    meters = converter.to_meter(1.0, "feet")
    yard_via_meter = meters / registry.get_meters_per_unit("yard")
    assert by_unit["yard"] == pytest.approx(yard_via_meter)


@pytest.mark.track_b
@pytest.mark.test_id("D-REG-01")
def test_d_reg_01_register_cubit_convertible(registry):
    """Given: cubit 0.4572 m 등록 → Then: 변환 가능"""
    registry.register("cubit", meters_per_unit=0.4572)
    converter = UnitConverter(registry)
    results = converter.convert_all(ParsedInput(unit="cubit", value=1.0))

    by_unit = {r.target_unit: r.target_value for r in results}
    assert "cubit" in by_unit
    assert by_unit["meter"] == pytest.approx(0.4572)


@pytest.mark.track_b
@pytest.mark.test_id("D-CFG-01")
def test_d_cfg_01_load_json_corrupted_file_config_error(registry, tmp_path):
    """Given: 깨진 JSON 파일 → Then: ConfigError"""
    from unit_converter.exceptions import ConfigError

    bad_config = tmp_path / "bad.json"
    bad_config.write_text("{invalid", encoding="utf-8")

    with pytest.raises(ConfigError):
        registry.load_from_file(str(bad_config))
