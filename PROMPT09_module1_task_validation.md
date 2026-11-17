# Prompt 09 — Module 1: Task schema and validation

**Purpose:** Validate the input format before model inference. This module does not download a model, call an API, or produce experiment results.

## Files
- `data/pilot_tasks.jsonl`: three toy, fictional, manually inspectable records for schema testing only.
- `src/validate_tasks.py`: validates JSONL syntax, required fields, unique IDs, and evidence-ID references.

## Run in Colab
Upload both files preserving the `data/` and `src/` folders, or put the JSONL file at `/content/pilot_tasks.jsonl` and run:

```python
!python /content/validate_tasks.py /content/pilot_tasks.jsonl
```

If using the project directory, run from the project root:

```python
!python src/validate_tasks.py
```

## Expected behavior
A successful run prints `validation_status: PASS` and the number of records validated. This expected behavior is a description of the script, not a claimed execution result. Copy the actual output back before we proceed.

## Manual checks still required
Schema validation cannot verify whether the gold answers and evidence IDs are semantically correct. Inspect each toy record and confirm the answer follows from the named evidence snippet. These records are synthetic test fixtures, not literature data and not the final 20-task pilot.
