"""Check an admissible k-tuple and measure its width.

    python checker/verify.py tuples/k10-w32-primes.json

A k-tuple of distinct integers is admissible when, for every prime p, it misses at least one residue
class mod p. Only primes p <= k need checking: k numbers can't fill more than k classes. The width is
max - min. Prints one JSON line. Exit 0 = VALID, 1 = INVALID, 2 = malformed.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

MAX_K = 5000
MAX_ABS = 10**9


def primes_upto(n: int) -> list[int]:
    if n < 2:
        return []
    sieve = bytearray([1]) * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i * i :: i] = bytearray(len(sieve[i * i :: i]))
    return [i for i, v in enumerate(sieve) if v]


def check(doc: dict) -> dict:
    extra = set(doc) - {"k", "tuple", "author", "note", "method"}
    if extra:
        raise ValueError(f"unknown keys: {sorted(extra)}")
    k, t = doc["k"], doc["tuple"]
    if not isinstance(k, int) or isinstance(k, bool) or not (2 <= k <= MAX_K):
        raise ValueError(f"k is an integer from 2 to {MAX_K}")
    if not isinstance(t, list) or len(t) != k:
        raise ValueError("tuple must list exactly k integers")
    if any(not isinstance(x, int) or isinstance(x, bool) or abs(x) > MAX_ABS for x in t):
        raise ValueError("entries are integers of size at most 1e9")
    if len(set(t)) != k:
        return {"verdict": "INVALID", "k": k, "reason": "entries repeat"}
    for p in primes_upto(k):
        if len({x % p for x in t}) == p:
            return {"verdict": "INVALID", "k": k, "reason": f"covers every residue class mod {p}"}
    return {"verdict": "VALID", "k": k, "width": max(t) - min(t)}


def main(argv) -> int:
    if len(argv) != 2:
        print(__doc__)
        return 2
    try:
        out = check(json.loads(Path(argv[1]).read_text(encoding="utf-8")))
    except Exception as e:
        print(json.dumps({"verdict": "MALFORMED", "reason": str(e)}))
        return 2
    print(json.dumps(out))
    return 0 if out["verdict"] == "VALID" else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
