#!/usr/bin/env python3
"""Real tests. Run: python3 test_score.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "stages" / "02-score"))
from score import fluency_tier, compliance_gate, RULE_VERSION  # noqa: E402

passed = failed = 0


def check(name, condition):
    global passed, failed
    if condition:
        passed += 1
        print(f"PASS  {name}")
    else:
        failed += 1
        print(f"FAIL  {name}")


# Fluency tier tests
floor_person = {"id": "X", "name_or_role": "t", "uses_ai_daily": False,
                 "has_shipped_tool": False, "tool_has_other_users": False,
                 "has_coached_someone": False}
check("zero signals scores Floor", fluency_tier(floor_person)["tier"] == "Floor")

ceiling_person = {"id": "X", "name_or_role": "t", "uses_ai_daily": True,
                   "has_shipped_tool": True, "tool_has_other_users": True,
                   "has_coached_someone": True}
check("all four signals scores Ceiling", fluency_tier(ceiling_person)["tier"] == "Ceiling")

r1 = fluency_tier(ceiling_person)
r2 = fluency_tier(ceiling_person)
check("fluency scoring is deterministic", r1 == r2)

# Compliance gate tests, the core claim: this gate cannot be bypassed
clean_workflow = {"id": "W", "name": "t", "touches_customer_pii": False,
                   "touches_investor_communications": False,
                   "touches_trade_or_deal_data": False,
                   "is_externally_facing": False, "uses_third_party_ai_api": True}
check("workflow with no triggers is CLEARED", compliance_gate(clean_workflow)["status"] == "CLEARED")

risky_workflow = dict(clean_workflow)
risky_workflow["touches_investor_communications"] = True
check("a single compliance trigger forces NEEDS_REVIEW",
      compliance_gate(risky_workflow)["status"] == "NEEDS_REVIEW")
check("the reason is reported, not just the label",
      "touches investor communications" in compliance_gate(risky_workflow)["reasons"])

pii_workflow = dict(clean_workflow)
pii_workflow["touches_customer_pii"] = True
check("customer PII alone, with nothing else risky, still forces NEEDS_REVIEW",
      compliance_gate(pii_workflow)["status"] == "NEEDS_REVIEW")

print(f"\n{passed} passed, {failed} failed. Rule version under test: {RULE_VERSION}")
sys.exit(1 if failed else 0)
