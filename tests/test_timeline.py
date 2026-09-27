from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_timeline import load_events, render  # noqa: E402

def test_events_are_loaded_in_timestamp_order():
    events = load_events()
    timestamps = [event["timestamp"] for event in events]
    assert timestamps == sorted(timestamps)

def test_render_contains_expected_evidence():
    output = render(load_events())
    assert "powershell.exe" in output
    assert "203.0.113.77:443" in output
    assert "Failed sign-in" in output
