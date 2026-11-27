"""A starting point, not a contender: sieve an interval [s, s + L) mod each prime p <= k by removing
the residue class that kills the fewest survivors, and keep the narrowest k survivors.

    python baselines/sieve.py 1000            # prints a tuples/ file to stdout
"""
from __future__ import annotations

import json
import sys

sys.path.insert(0, "checker")
from verify import primes_upto  # noqa: E402


def greedy(k: int, start: int, length: int):
    alive = list(range(start, start + length))
    for p in primes_upto(k):
        counts = [0] * p
        for x in alive:
            counts[x % p] += 1
        r = counts.index(min(counts))
        alive = [x for x in alive if x % p != r]
        if len(alive) < k:
            return None
    best = None
    for i in range(len(alive) - k + 1):
        w = alive[i + k - 1] - alive[i]
        if best is None or w < best[0]:
            best = (w, alive[i : i + k])
    return best


def main(k: int):
    best = None
    for length in range(int(k * 6), int(k * 14), max(1, k // 4)):
        for start in (-length // 2, 0):
            got = greedy(k, start, length)
            if got and (best is None or got[0] < best[0]):
                best = got
    w, t = best
    print(json.dumps({"k": k, "tuple": t, "method": "greedy sieve, baselines/sieve.py"}))
    print(f"k={k} width={w}", file=sys.stderr)


if __name__ == "__main__":
    main(int(sys.argv[1]))
