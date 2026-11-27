# Tasks

## Warmup
- Run `baselines/sieve.py` for some k above 342, then improve it by changing which residue class it
  removes at each prime. Record what you tried in `method`, whether or not it beats the record.

## Solid
- Beat any record for 343 <= k <= 1000. Methods to try: shifted Schinzel sieves, sieving over a
  well-chosen interval, local swaps that remove an endpoint and re-admit an inside point (see the Polymath8a and
  Polymath8b papers; 8b is arXiv:1407.4897).
- Beat a record for 1000 < k <= 5000. Larger k are less searched.

## Hard
- A provably optimal width for k = 343 (an exhaustive search with a checkable certificate).
