"""Stage 01: collect. Writes collected.json from sample people and
sample workflows. Nothing computed here, just the real inputs."""
import json
import sys
from pathlib import Path

OUT = Path(__file__).parent / "collected.json"

# Sample people, the kind a real fluency self-assessment would collect.
# Field names match the posting's own "raise the floor / raise the
# ceiling" language: has someone gone from aware, to building, to
# building something OTHERS use and coaching someone else through it.
PEOPLE = [
    {
        "id": "P1", "name_or_role": "Ops analyst, sample",
        "uses_ai_daily": True, "has_shipped_tool": False,
        "tool_has_other_users": False, "has_coached_someone": False,
    },
    {
        "id": "P2", "name_or_role": "Deal associate, sample",
        "uses_ai_daily": True, "has_shipped_tool": True,
        "tool_has_other_users": False, "has_coached_someone": False,
    },
    {
        "id": "P3", "name_or_role": "Senior engineer, sample",
        "uses_ai_daily": True, "has_shipped_tool": True,
        "tool_has_other_users": True, "has_coached_someone": True,
    },
    {
        "id": "P4", "name_or_role": "New hire, sample",
        "uses_ai_daily": False, "has_shipped_tool": False,
        "tool_has_other_users": False, "has_coached_someone": False,
    },
]

# Sample workflows, attributes pulled from the posting's own compliance
# language: "In a broker-dealer context, know when a workflow touches
# compliance obligations and raise it before it ships."
WORKFLOWS = [
    {
        "id": "W1", "name": "Internal meeting notes summarizer, sample",
        "touches_customer_pii": False, "touches_investor_communications": False,
        "touches_trade_or_deal_data": False, "is_externally_facing": False,
        "uses_third_party_ai_api": True,
    },
    {
        "id": "W2", "name": "Draft investor update email, sample",
        "touches_customer_pii": False, "touches_investor_communications": True,
        "touches_trade_or_deal_data": True, "is_externally_facing": True,
        "uses_third_party_ai_api": True,
    },
    {
        "id": "W3", "name": "Internal onboarding FAQ bot, sample",
        "touches_customer_pii": False, "touches_investor_communications": False,
        "touches_trade_or_deal_data": False, "is_externally_facing": False,
        "uses_third_party_ai_api": True,
    },
    {
        "id": "W4", "name": "Customer-facing deal status chatbot, sample",
        "touches_customer_pii": True, "touches_investor_communications": False,
        "touches_trade_or_deal_data": True, "is_externally_facing": True,
        "uses_third_party_ai_api": True,
    },
]


def run():
    data = {"people": PEOPLE, "workflows": WORKFLOWS}
    OUT.write_text(json.dumps(data, indent=2))
    return data


if __name__ == "__main__":
    data = run()
    print(f"Collected {len(data['people'])} people, {len(data['workflows'])} workflows -> {OUT}",
          file=sys.stderr)
