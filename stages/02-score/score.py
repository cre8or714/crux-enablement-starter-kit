"""Stage 02: score. Reads collected.json, writes scored.json.
Two fixed deterministic rules, no model call, no judgment."""
import json
import sys
from pathlib import Path

IN = Path(__file__).parent.parent / "01-collect" / "collected.json"
OUT = Path(__file__).parent / "scored.json"

RULE_VERSION = "crux-enablement-v1"


def fluency_tier(person: dict) -> dict:
    """Floor / Building / Ceiling, straight off the posting's own
    raise-the-floor / raise-the-ceiling language. Fixed point rule,
    no partial credit for intentions, only for what was actually shipped."""
    points = 0
    reasons = []
    if person["uses_ai_daily"]:
        points += 1
        reasons.append("uses AI daily (+1)")
    if person["has_shipped_tool"]:
        points += 2
        reasons.append("has shipped a tool with AI help (+2)")
    if person["tool_has_other_users"]:
        points += 3
        reasons.append("someone else actually uses it (+3)")
    if person["has_coached_someone"]:
        points += 2
        reasons.append("has coached a colleague (+2)")

    if points >= 7:
        tier = "Ceiling"
    elif points >= 2:
        tier = "Building"
    else:
        tier = "Floor"

    return {
        "id": person["id"], "name_or_role": person["name_or_role"],
        "rule_version": RULE_VERSION, "points": points, "tier": tier,
        "reasons": reasons,
    }


def compliance_gate(workflow: dict) -> dict:
    """CLEARED or NEEDS_REVIEW. Any one of these flips it, no exceptions,
    straight off the posting's own compliance language."""
    trigger_fields = {
        "touches_customer_pii": "touches customer PII",
        "touches_investor_communications": "touches investor communications",
        "touches_trade_or_deal_data": "touches trade or deal data",
        "is_externally_facing": "externally facing",
    }
    reasons = [label for field, label in trigger_fields.items() if workflow.get(field)]
    status = "NEEDS_REVIEW" if reasons else "CLEARED"

    return {
        "id": workflow["id"], "name": workflow["name"],
        "rule_version": RULE_VERSION, "status": status,
        "reasons": reasons if reasons else ["no compliance triggers present"],
        "uses_third_party_ai_api": workflow.get("uses_third_party_ai_api", False),
    }


def run(collected: dict):
    scored = {
        "people": [fluency_tier(p) for p in collected["people"]],
        "workflows": [compliance_gate(w) for w in collected["workflows"]],
    }
    OUT.write_text(json.dumps(scored, indent=2))
    return scored


if __name__ == "__main__":
    collected = json.loads(IN.read_text())
    scored = run(collected)
    print(f"Scored {len(scored['people'])} people, {len(scored['workflows'])} workflows -> {OUT}",
          file=sys.stderr)
