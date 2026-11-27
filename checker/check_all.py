"""The pool's check: every tuple is admissible, and at least one is narrower than the record.

    python checker/check_all.py

Exit 0 when every file in tuples/ is VALID and at least one is strictly narrower than RECORDS.json
holds for its k. Thinkpool runs this without and with a contribution's diff: a new record fails
before and passes after.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "checker"))

from hygiene import problems  # noqa: E402
from verify import check  # noqa: E402

MAX_FILES = 6000


def main() -> int:
    bad = problems(ROOT, "tuples")
    if bad:
        print(json.dumps({"summary": "the tree is not the pool\'s", "problems": bad[:20]}))
        return 1
    recs = {r["k"]: r["width"] for r in json.loads((ROOT / "RECORDS.json").read_text(encoding="utf-8"))["records"]}
    files = sorted((ROOT / "tuples").glob("*.json"))
    if len(files) > MAX_FILES:
        print(json.dumps({"summary": "too many files", "limit": MAX_FILES}))
        return 1
    ok, new = True, []
    for f in files:
        try:
            if f.is_symlink() or not f.is_file():
                raise ValueError("not a regular file")
            out = check(json.loads(f.read_text(encoding="utf-8")))
        except Exception as e:
            out = {"verdict": "MALFORMED", "reason": str(e)}
        out["file"] = f.name
        print(json.dumps(out))
        if out["verdict"] != "VALID":
            ok = False
        elif out["width"] < recs[out["k"]]:
            new.append({"file": f.name, "k": out["k"], "width": out["width"], "record": recs[out["k"]]})
    print(json.dumps({"summary": "ok" if ok and new else "no new record" if ok else "a tuple is not valid", "new": new}))
    return 0 if ok and new else 1


if __name__ == "__main__":
    sys.exit(main())
