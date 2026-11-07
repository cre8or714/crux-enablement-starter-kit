# CONTEXT: 02-score

**Inputs:** `../01-collect/collected.json`.

**Process:** two separate, fixed, deterministic rules.

- **Fluency tier**, one per person: Floor (aware, not yet building),
  Building (has shipped something with AI help), or Ceiling (built
  something others actually use, and has coached someone else). No
  model call, no judgment, a fixed point rule over the four inputs.
- **Compliance gate**, one per workflow: CLEARED or NEEDS_REVIEW,
  with the exact reason codes that triggered it. A workflow that
  touches investor communications, trade or deal data, customer PII,
  or is externally facing is NEEDS_REVIEW, no exceptions, regardless
  of how useful or well-built it is.

**Outputs:** `scored.json`.

**Checkpoint:** the compliance gate cannot be talked out of a flag.
A workflow with every fluency-adjacent field green and one
compliance-triggering field still comes back NEEDS_REVIEW. Proven in
`../../test_score.py`, not just claimed here.

**Audit:** every scored record shows the exact inputs that produced
its tier or gate result, next to the result itself.
