#!/usr/bin/env python3
"""food-picture-01 v3 entrypoint.

Copies ``entry.png`` (sitting beside this file) to ``$MAKEFUN_OUTPUT_DIR/entry.png``
(default ``/output``), byte for byte, so the judge sees exactly these bytes.
Deterministic: the same input always produces the same output.
Python 3.13, standard library only.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
TARGET = OUTPUT_DIR / "entry.png"


def main() -> int:
    if not SOURCE.is_file():
        print(f"error: {SOURCE} not found", file=sys.stderr)
        return 1
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, TARGET)
    # Validate the copy: the judge must see exactly the source bytes.
    source_hash = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    target_hash = hashlib.sha256(TARGET.read_bytes()).hexdigest()
    if source_hash != target_hash:
        print("error: output bytes differ from source", file=sys.stderr)
        return 1
    print(f"wrote {TARGET} ({TARGET.stat().st_size} bytes, sha256 {target_hash[:16]}...)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
