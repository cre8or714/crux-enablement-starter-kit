#!/usr/bin/env python3
"""Single entry point. Walks stages 01 through 03 in order.

Run: python3 run.py
Run: python3 run.py --json
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT / "stages" / "01-collect"))
sys.path.insert(0, str(ROOT / "stages" / "02-score"))
sys.path.insert(0, str(ROOT / "stages" / "03-review"))

import collect as stage01   # noqa: E402
import score as stage02     # noqa: E402
import review as stage03    # noqa: E402


def main():
    collected = stage01.run()
    scored = stage02.run(collected)

    if "--json" in sys.argv:
        print(json.dumps(scored, indent=2))
        return

    print(stage03.run(scored))


if __name__ == "__main__":
    main()
