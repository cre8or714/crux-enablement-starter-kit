# CONTEXT: 01-collect

**Inputs:** none, this is the entry point.

**Process:** hold two small, honest sample data sets as plain Python,
nothing computed or scored here.

- `PEOPLE`: sample self-assessment answers, the kind a real fluency
  survey would collect (used AI daily, shipped something with AI
  help, someone else actually uses it, has coached a colleague).
- `WORKFLOWS`: sample workflow descriptions with the attributes that
  actually matter for a compliance read, not invented ones, pulled
  straight from the posting's own language (customer data, investor
  communications, trade or deal data, externally facing).

**Outputs:** `collected.json`, written by `collect.py`.

**Checkpoint:** every person record has all four fluency inputs set
to true or false, no missing fields. Every workflow record has all
five compliance inputs set the same way.

**Audit:** `collected.json` is plain JSON, open it directly to see
exactly what entered the pipeline before any rule touched it.
