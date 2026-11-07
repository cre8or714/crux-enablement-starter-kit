# CONTEXT: 03-review

**Inputs:** `../02-score/scored.json`.

**Process:** turn the scored data into one plain-text report. No
scoring logic lives here, only formatting what already happened.

**Outputs:** `review.md`, printed and saved to disk.

**Checkpoint:** every person shows their tier and the exact reasons
behind it. Every workflow shows CLEARED or NEEDS_REVIEW and the exact
reasons behind that too, never just the final label alone.

**Audit:** `review.md` is the one file meant for a person to actually
read without running anything.
