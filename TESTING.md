# Running the tests

These tests use Python's standard library. They do not require a GPU,
internet connection, Hugging Face account, or model download.

## 1. Open the repository root

Open a terminal in the folder that contains `README.md`, `src/`, and `tests/`.

## 2. Check Python

```bash
python --version
```

Python 3.10 or newer is recommended. On some systems use `python3` instead
of `python`.

## 3. Run all unit tests

```bash
python -m unittest discover -s tests -v
```

Expected: seven tests pass and the final status is `OK`.

## 4. Validate the supplied synthetic fixtures

```bash
python src/validate_tasks.py --input data/pilot_tasks.jsonl
```

Expected summary:

```text
records=3 unique_ids=3 errors=0
```

## 5. What the tests cover

- TC-01: gold evidence is placed at the beginning.
- TC-02: gold evidence is placed in the middle.
- TC-03: gold evidence is placed at the end.
- TC-04: evidence-first prompt construction requests evidence IDs before the answer.
- TC-05: valid JSON predictions are parsed.
- TC-06: malformed JSON is handled without assigning unsupported evidence IDs.
- TC-07: the three supplied synthetic task fixtures pass schema/reference validation.

The tests validate software behavior and the synthetic fixture schema only.
They do not run a language model and do not establish research findings.

## 6. Run one test

Example (the test class and method names are in `tests/test_pipeline.py`):

```bash
python -m unittest test_pipeline.PipelineTests.test_position_middle -v
```

If importing an individual test fails, run the full discovery command in step 3.

## 7. Run tests automatically on GitHub

The repository includes `.github/workflows/python-tests.yml`. GitHub Actions
runs the unit tests and fixture validator on pushes and pull requests.
Open the repository's **Actions** tab to inspect the actual run status.

## 8. Model inference is a separate step

`src/run_inference.py` requires the model dependencies and a verified research
dataset. It is not part of the seven unit tests. Follow `README.md` and the
Colab protocol before running it. Do not use the three synthetic fixtures as
research evidence or report synthetic test results as model performance.
