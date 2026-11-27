# How to attack this pool

This is the warm-up pool: the checker is instant, the methods are well documented, and a good
implementation of known ideas gets close to the records within a day. Getting *past* them is the
harder part. Log every serious run in the attempts log ([ATTEMPTS.md](ATTEMPTS.md)).

## Where the gap is

The greedy sieve in `baselines/` lands 2-7% above the records (8360 against 7802 at k = 1000). The
records for k from 343 to 5000 were set in 2013 to 2019, almost all by three people: T. Engelsma (about
2,080 of them), A. V. Sutherland (about 2,000) and xfxie (about 570). Nobody has published a systematic
pass since.

A smooth fit of width against k log k and k shows where the table is uneven. The records run about 20
above the fit on average (one standard deviation), but the run **k ≈ 2515 to 2570** sits 45 to 58 above
it, about 0.25% wide, for fifty consecutive k. That run is the first place to look: either a method
that was used elsewhere was never run there, or the fit is wrong there for a reason worth knowing.
Other single points sit 50 above the fit at k = 4166 and 4639.

One record often contains narrower windows for smaller k, so improving one k can improve its
neighbours; the README says how those derived rows are credited.

## The methods (Polymath8b's write-up of narrow admissible tuples is the reference)

- **Schinzel sieve, and shifted.** Keep integers in an interval that are not ≡ 0 mod small primes up to
  a bound, then sieve the rest greedily. Shifting the interval (not starting at 0 or centring it) matters
  a lot; the best shift depends on k.
- **Hensley-Richards and its asymmetric form.** Take primes in a symmetric (or asymmetric) window around
  0 together with ±1; admissible by construction for the small primes, then fixed up for the rest.
- **Greedy-greedy** (Sutherland's name). Sieve the classes mod small primes in a fixed pattern, then for
  each larger prime remove the residue class that hits the fewest survivors, as the baseline does, but
  choosing the interval and the switch-over prime by search. This produced many of the 2013 records.
- **Local improvement** (Engelsma, Sutherland, xfxie). From a good tuple, try to drop an endpoint and
  add an interior point that keeps admissibility, or merge two near-optimal tuples' windows, and repeat.
  This is where the last few units of width came from in 2013.
- **Exhaustive search for small k** (Engelsma, to k = 342, which is why those records are optimal). Not
  a route above 342, but its pruning ideas help local search.

## Afternoon-sized pieces

1. Implement the shifted Schinzel sieve and greedy-greedy, with the shift and switch-over prime
   searched; reproduce the records at k = 343, 1000 and 5000 to within 0.5%. Publish the code.
2. Local improvement: endpoint swaps and window merges, run from (1)'s output.
3. Run (1) and (2) across k = 2515 to 2570 and log where you land against each record.
4. Recompute the fit residuals after any improvement and pick the next window.
5. A derived-windows tool: from one tuple, the narrowest window for every smaller k, to check a
   candidate against the whole table at once.

## Honest odds

A careful reimplementation of the 2013 methods should land within a few units of most records in a
day. Beating a record by one or two units somewhere in k = 343..5000 is likely for a group that
runs local search for a few days, because nobody has swept the table since 2019. Beating many is not.
None of this moves a prime-gap bound: the bounds use k = 50 (proved optimal), and the large-k widths
feed no current result. It is a clean benchmark of construction methods, and good practice for the
pool format.
