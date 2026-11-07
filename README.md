# Crux enablement starter kit

A real, runnable tool, not a write-up. Built for the AI Enablement
Lead posting at Crux, as ICM (Interpretable Context Methodology,
Jake Van Clief, https://github.com/RinDig/Interpretable-Context-Methodology):
one agent, one job per numbered stage, plain text handoff, no
framework. See `CONTEXT.md` for the stage map.

It operationalizes two things the posting names directly, in its own
words:

> "The gap is not awareness or appetite. It is activation energy,
> scaffolding, and someone whose job is to coach and support."

> "In a broker-dealer context, know when a workflow touches
> compliance obligations and raise it before it ships."

## Run it

    python3 run.py              # walks all 3 stages, prints the review
    python3 run.py --json       # machine-readable
    python3 test_score.py       # real tests, including the compliance gate

## What it does

**A fluency tier, one per person.** The posting says owning "our
fluency rubric" is part of the role. This is a small, fixed,
deterministic version of one: Floor (aware, not yet building),
Building (shipped something with AI help), Ceiling (shipped something
someone else actually uses, and has coached a colleague through it).
No partial credit for good intentions, only for what was actually
shipped and used.

**A compliance gate, one per workflow.** The posting is explicit that
a broker-dealer context means some workflows need a compliance check
before they ship. This gate flags any workflow that touches customer
PII, investor communications, trade or deal data, or is externally
facing, CLEARED or NEEDS_REVIEW, with the exact reasons shown, never
just the label. A single trigger forces review, no matter how useful
the workflow otherwise is. `test_score.py` proves that gate actually
holds, not just claimed.

## Stages

1. `stages/01-collect`, sample people and sample workflows, nothing computed
2. `stages/02-score`, the two fixed rules above
3. `stages/03-review`, the one human-readable output, `review.md`

Each stage has its own `CONTEXT.md` with Inputs, Process, Outputs,
Checkpoint, Audit. Open any of them directly, no code required.

## What this is not

Not a real survey tool, not connected to Crux's actual systems, not a
claim about any real Crux employee or workflow. The people and
workflows in `stages/01-collect` are explicitly labeled "sample" in
every record. This is sized to show the method, a working fluency
rubric and a working compliance gate, that could be pointed at real
data on day one.
