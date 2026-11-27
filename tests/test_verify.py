"""Run: python -m pytest tests -q"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "checker"))

from verify import check, primes_upto  # noqa: E402


def test_primes():
    assert primes_upto(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def test_known_optimal_small_tuples():
    for t, w in (([0, 2], 2), ([0, 4, 6], 6), ([0, 2, 6, 8], 8), ([0, 4, 6, 10, 12], 12)):
        assert check({"k": len(t), "tuple": t}) == {"verdict": "VALID", "k": len(t), "width": w}


def test_inadmissible():
    assert check({"k": 2, "tuple": [0, 1]})["verdict"] == "INVALID"          # both classes mod 2
    assert check({"k": 3, "tuple": [0, 2, 4]})["verdict"] == "INVALID"       # every class mod 3
    assert check({"k": 3, "tuple": [0, 2, 2]})["verdict"] == "INVALID"       # repeats


def test_seed_and_baseline_are_valid():
    seed = json.loads((ROOT / "tuples" / "k10-w32-primes.json").read_text())
    assert check(seed)["width"] == 32
    out = subprocess.run([sys.executable, "baselines/sieve.py", "200"], cwd=ROOT,
                         capture_output=True, text=True, check=True)
    assert check(json.loads(out.stdout))["verdict"] == "VALID"


def test_records_table():
    recs = json.loads((ROOT / "RECORDS.json").read_text())["records"]
    assert [r["k"] for r in recs] == list(range(2, 5001))
    by = {r["k"]: r for r in recs}
    assert by[50]["width"] == 246 and by[50]["proved_optimal"]
    assert by[1000]["width"] == 7802 and not by[1000]["proved_optimal"]


def test_malformed():
    for bad in ({"k": 1, "tuple": [0]}, {"k": 3, "tuple": [0, 2]}, {"k": 2, "tuple": [0, 2.0]},
                {"k": 2, "tuple": [0, 2], "x": 1}, {"k": 2, "tuple": [0, 10**12]}):
        with pytest.raises(ValueError):
            check(bad)
