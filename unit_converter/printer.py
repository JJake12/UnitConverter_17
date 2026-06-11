import csv
import io
import json
from typing import Literal

from unit_converter.models import ConversionResult

OutputFormat = Literal["table", "json", "csv"]


class ResultPrinter:
    """FR-02 출력, EXT-03: table / json / csv."""

    def print(self, results: list[ConversionResult], fmt: OutputFormat = "table") -> str:
        if fmt == "json":
            return self.print_json(results)
        if fmt == "csv":
            return self.print_csv(results)
        return self.print_table(results)

    def print_table(self, results: list[ConversionResult]) -> str:
        lines = [
            f"{r.source_value} {r.source_unit} = {r.target_value} {r.target_unit}"
            for r in results
        ]
        return "\n".join(lines)

    def print_json(self, results: list[ConversionResult]) -> str:
        payload = [
            {
                "source": {"unit": r.source_unit, "value": r.source_value},
                "target": {"unit": r.target_unit, "value": r.target_value},
            }
            for r in results
        ]
        return json.dumps(payload, indent=2)

    def print_csv(self, results: list[ConversionResult]) -> str:
        buffer = io.StringIO()
        writer = csv.writer(buffer)
        writer.writerow(["source_unit", "source_value", "target_unit", "target_value"])
        for r in results:
            writer.writerow([r.source_unit, r.source_value, r.target_unit, r.target_value])
        return buffer.getvalue().strip()
