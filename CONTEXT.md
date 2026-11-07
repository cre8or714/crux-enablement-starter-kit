# CONTEXT: Crux enablement starter kit

ICM-style layout (Jake Van Clief, Interpretable Context Methodology,
https://github.com/RinDig/Interpretable-Context-Methodology). One
agent, one job per numbered stage, plain text handoff, no framework.

This operationalizes two things the Crux AI Enablement Lead posting
names directly: owning a fluency rubric, and knowing when a workflow
touches compliance obligations before it ships. Both are small,
deterministic, and real, not a mockup.

## Stage map

1. `stages/01-collect`, sample people and sample workflows, nothing computed
2. `stages/02-score`, two fixed deterministic rules: a fluency tier
   per person, a compliance gate per workflow
3. `stages/03-review`, the one human-readable output

## Run it

    python3 run.py              # walks all 3 stages, prints the review
    python3 run.py --json       # machine-readable
    python3 test_score.py       # real tests, including the compliance gate
