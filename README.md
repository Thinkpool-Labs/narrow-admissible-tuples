# Narrower admissible tuples

**For each k, find k integers packed as tightly as primes could ever be.**
A Prometheus pool on Thinkpool, in the line of Polymath8.

A set of k integers is *admissible* if, for every prime p, it misses at least one residue class mod p.
The prime k-tuples conjecture says every admissible pattern occurs infinitely often among the primes.
Zhang, Maynard and Tao turned bounded gaps between primes into this question: the narrowest admissible
50-tuple has width 246, and that is why we know infinitely many pairs of primes differ by at most 246.

`RECORDS.json` holds the narrowest known width for every k from 2 to 5000. Up to k = 342 they are proved
optimal. Above that, almost every record dates from 2013 and none is known to be optimal.

| k | record | a naive greedy sieve (`baselines/sieve.py`) |
| --- | --- | --- |
| 343 | 2340 | 2406 |
| 1000 | 7802 | 8360 |
| 5000 | 46806 | |

## Run the checker

```sh
python checker/verify.py tuples/k10-w32-primes.json
python checker/check_all.py
python baselines/sieve.py 1000 > tuples/my-try.json      # a valid start, far from a record
python -m pytest tests -q
```

## What a contribution is

A JSON file in `tuples/`: `{"k": 1000, "tuple": [...], "method": "how you found it"}`. It counts when it
is admissible and strictly narrower than the record for its k. The check takes well under a second for
k = 5000.

## Credit and honesty

A narrower tuple is a new record, credited by name, and the first one for a k takes it. Narrower tuples
for large k don't bring the twin prime conjecture closer; they matter through bounds such as the
Maynard–Tao one, and we say only that. Describe your method in `method`: the ideas are the point.

## Licence and sources

Code Apache-2.0, tuples CC-BY-4.0. Baseline widths: the table at https://math.mit.edu/~primegaps/
(T. Engelsma, A. V. Sutherland and others), snapshot 2026-11-27. Polymath8: https://arxiv.org/abs/1407.4897
