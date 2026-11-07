"""Stage 03: review. Reads scored.json, writes review.md. Pure
formatting, no logic that changes a tier or a gate result."""
import json
import sys
from pathlib import Path

IN = Path(__file__).parent.parent / "02-score" / "scored.json"
OUT = Path(__file__).parent / "review.md"


def build_review(scored: dict) -> str:
    lines = ["# Crux enablement starter kit, review\n", "## Fluency tiers\n"]
    for p in scored["people"]:
        lines.append(f"- [{p['id']}] {p['name_or_role']}: **{p['tier']}** ({p['points']} points)")
        for r in p["reasons"]:
            lines.append(f"    - {r}")
    lines.append("\n## Compliance gate\n")
    for w in scored["workflows"]:
        lines.append(f"- [{w['id']}] {w['name']}: **{w['status']}**")
        for r in w["reasons"]:
            lines.append(f"    - {r}")
    return "\n".join(lines)


def run(scored: dict):
    text = build_review(scored)
    OUT.write_text(text)
    return text


if __name__ == "__main__":
    scored = json.loads(IN.read_text())
    print(run(scored))
    print(f"\n(also written to {OUT})", file=sys.stderr)
