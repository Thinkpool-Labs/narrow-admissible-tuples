# Narrower admissible tuples

**For each k, find k integers packed as tightly as primes could ever be.**
A Prometheus pool on Thinkpool, in the line of Polymath8.

A set of k integers is *admissible* if, for every prime p, it misses at least one residue class mod p.
The prime k-tuples conjecture says every admissible pattern occurs infinitely often among the primes.
In the proof that infinitely many pairs of primes differ by at most 246 (Maynard, Tao, Polymath8b), the
last step is this question: the narrowest admissible 50-tuple has width 246.

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

A narrower tuple is a new record, credited by name. The k from 343 to 5000 feed no current bound on
prime gaps: this is a combinatorial benchmark, and a good one because the records are old and the
construction methods are the interesting part. Describe your method in `method`.

- **Priority** goes to the earliest pull request (or Thinkpool submission) that carries the result, not
  the first merge. A tuple shifted or mirrored from someone else's is the same tuple.
- **One idea, one credit.** A record for k often contains narrower windows for smaller k. The host adds
  those rows to `RECORDS.json` as derived, credited to the same contributor once, not as separate records.
- **"New here" and "new to the literature" are different.** The public table has not changed since 2019
  and takes improvements by email to its maintainer, so a result may already be known. We ask before
  calling anything new to the literature, and forward accepted records with the contributor's consent.
- Authorship lives in `RECORDS.json`, which only the host writes. Contributions add files; they never
  change or remove one.

## How to attack it

Where the gap to the records is (k around 2515 to 2570 first), the methods and honest odds: [SOLVING.md](SOLVING.md).

## Work that set no record

Days without a record still count here: add what you tried, how far it got and why it stopped to the attempts log. It earns no record, and it saves the next person the same days. See [ATTEMPTS.md](ATTEMPTS.md).

## Licence and sources

Code Apache-2.0, tuples CC-BY-4.0. Baseline widths: the table at https://math.mit.edu/~primegaps/
(T. Engelsma, A. V. Sutherland and others), snapshot 2026-11-27. Polymath8: https://arxiv.org/abs/1407.4897
