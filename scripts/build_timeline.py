#!/usr/bin/env python3
"""Render the synthetic incident CSV as a simple ordered investigation timeline."""

from __future__ import annotations
import csv
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "synthetic_timeline.csv"

def parse_timestamp(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)

def load_events(path: Path = DATA) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    return sorted(rows, key=lambda row: parse_timestamp(row["timestamp"]))

def render(events: list[dict[str, str]]) -> str:
    lines = []
    for event in events:
        lines.append(
            f'{event["timestamp"]} | {event["device"]} | {event["event_type"]} | '
            f'{event["process_or_action"]} | {event["detail"]}'
        )
    return "\n".join(lines)

if __name__ == "__main__":
    print(render(load_events()))
