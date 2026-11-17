# MNS2026001 — Context-Window Degradation and Long-Document Research Synthesis

Implementation project prepared for Google Colab Free / NVIDIA T4. No paid API is required by the current design.

## Current state

The repository preserves the earlier review, decision log, gap matrix, synthetic pilot fixtures, task validator and environment test. It adds prompt updates 03–18, an inference scaffold, evaluator, configuration template and an implementation report. **Model inference has not yet been executed**; no performance metrics or research conclusions are claimed.

## Quick start

```bash
python src/validate_tasks.py --input data/pilot_tasks.jsonl
```

This validates three synthetic fixtures only. It does not run a model.

## Research inference [TEST REQUIRED]

After preparing a manually verified `data/research_tasks.jsonl`, selecting an openly licensed model and recording its exact revision:

```bash
pip install -r requirements_candidate.txt
python src/run_inference.py --input data/research_tasks.jsonl --model [VERIFIED_MODEL_ID] --output results/predictions.jsonl
python src/evaluate.py --input results/predictions.jsonl --output results/metrics.csv
```

Run in Colab after confirming the actual GPU, memory, Python and library versions. The existing `[3, 15]` context settings are snippet counts, not token counts. Freeze token lengths using the selected tokenizer before the experiment.

## Structure

- `prompts/` — prompt-by-prompt updated status and evidence boundaries
- `src/` — task validation, inference and evaluation code
- `configs/` — experiment configuration template
- `data/` — synthetic fixtures; not a research benchmark
- `evidence/` — existing Colab execution evidence
- `notebooks/` — uploaded executed notebook
- `results/` — output destination; no fabricated result files
- `paper/` — manuscript resources
- `IMPLEMENTATION_REPORT.md` — full implementation and status report

## Reproduction checklist

1. Verify task sources, licenses, gold answers and evidence IDs.
2. Record model ID, immutable revision, tokenizer and license.
3. Record Colab runtime, GPU, Python and package versions.
4. Freeze task set, token-length conditions, evidence positions, generation parameters, seed and metrics.
5. Run inference and preserve raw outputs/logs.
6. Run evaluator and manually audit predictions.
7. Reproduce tables/figures from saved outputs only.
8. Record all deviations and AI-assisted changes in the provenance log.

## License and data

No blanket license is asserted for included papers or datasets. Check source and model licenses before redistribution. Synthetic fixtures are for software testing only. Add a project license only after confirming rights for all included materials.

## Citation

[TO VERIFY] Add the final implementation-paper citation after the manuscript is accepted or submitted. Cite all original methods and datasets using verified bibliographic metadata.

## Evaluator guide

See `TA_EVALUATION_GUIDE.md` for the topic explained in plain language, glossary, test-case walkthrough, commands, expected checks and viva questions.

## Unit tests

```bash
python -m unittest discover -s tests -v
```

## Test cases

See `tests/TEST_CASES.md` for expected behavior and `TA_EVALUATION_GUIDE.md` for a TA-oriented explanation of the topic and demonstration.


## Test instructions

See [`TESTING.md`](TESTING.md) for step-by-step local testing instructions. GitHub Actions is configured in `.github/workflows/python-tests.yml` to run the unit tests and fixture validator automatically.
