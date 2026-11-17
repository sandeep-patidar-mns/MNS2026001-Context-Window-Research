# TA Evaluation Guide — MNS2026001

## Project in one minute

**Topic:** Context-window degradation and its impact on long-document research synthesis.

A language model may accept a long input but still fail to use all of its information reliably. In particular, it may overlook supporting evidence when that evidence appears in the middle of a long context. This project studies whether evidence location and answer procedure affect answer correctness and source attribution.

**Simple example:** A question asks which treatment improved an outcome. The supporting sentence is placed at the start, middle or end of the supplied document snippets. The question and evidence remain the same; only evidence position changes. The system is asked to answer and identify the snippet IDs that support its answer.

## Terms the evaluator needs

| Term | Plain-language meaning |
|---|---|
| Context window | The text a model receives in one input. |
| Context length | Number of tokenizer tokens in that input, not number of paragraphs/snippets. |
| Evidence position | Where the relevant source passage appears: beginning, middle or end. |
| Distractor | A passage included in the input that does not answer the question. |
| Direct answering | Model answers the question from all supplied text. |
| Evidence-first | Model first identifies supporting source IDs, then answers from them. |
| Gold answer | Reference answer prepared before model evaluation. |
| Gold evidence IDs | IDs of the source snippets that support the reference answer. |
| Exact match | Whether normalized model answer matches the reference answer. |
| Evidence F1 | Harmonic mean of evidence-ID precision and recall. |

## Research questions

- **RQ1:** Under a fixed model and task set, does answer quality vary with evidence position and tokenizer-measured context length?
- **RQ2:** Does an evidence-first response procedure change answer correctness and supporting-evidence coverage compared with direct answering?

These are questions to test, not findings already established by this repository.

## What is currently real and what is illustrative

- The uploaded Colab notebook records three synthetic source tasks and 18 context variants, with the reported variant audits showing zero errors.
- The three tasks in `data/pilot_tasks.jsonl` are fictional software fixtures named Atlas, Birch and Delta. They are deliberately simple so that a reviewer can understand the data format and validate code.
- `[3, 15]` in the earlier notebook are snippet counts, not token lengths.
- Synthetic fixtures and their tests demonstrate the pipeline only. They are not a real research dataset, do not validate a scientific hypothesis and must not be described as experimental LLM results.
- No model inference, measured model accuracy, model comparison or research conclusion is claimed by the existing notebook.

## How to inspect the project

1. Open `README.md` for setup and project structure.
2. Open `IMPLEMENTATION_REPORT.md` for the implementation status and evidence boundary.
3. Open `prompts/` for the updated deliverable/status for each prompt.
4. Open `data/pilot_tasks.jsonl` to see the three synthetic tasks and evidence annotations.
5. Open `src/validate_tasks.py`, `src/run_inference.py` and `src/evaluate.py` for the pipeline.
6. Open `tests/test_pipeline.py` for deterministic software tests.
7. Open `notebooks/Untitled3_executed.ipynb` for the supplied Colab execution record.

## Re-run the deterministic tests

From the repository root:

```bash
python -m unittest discover -s tests -v
python src/validate_tasks.py --input data/pilot_tasks.jsonl
```

Expected test suite: 7 tests pass. Expected validator summary: `records=3 unique_ids=3 errors=0`.

These tests verify prompt construction, evidence reordering, JSON-output parsing and fixture schema validation. They do not call an LLM.

## How the intended experiment works

For each task, construct controlled conditions:

- answer procedure: `direct` or `evidence_first`;
- evidence position: `beginning`, `middle` or `end`;
- context length: defined in tokens using the selected model's tokenizer and frozen before evaluation.

Keep the model checkpoint, tokenizer, task content, generation settings and scoring code fixed across comparisons. Save raw model outputs and the exact configuration. Evaluate answer correctness and evidence-ID coverage. Include latency and input-token counts as resource measures. A valid study needs a verified research-task set, not only the three synthetic fixtures.

## What a TA can reasonably grade now

The TA can inspect whether the project explains its research question, defines the factors and metrics, validates its synthetic input format, constructs controlled evidence-position prompts, records limitations and provides reproducibility scaffolding. The TA cannot infer scientific performance or accept claims of improvement without actual model outputs and a real, verified task set.

## Viva questions and concise answers

**Q: What is the problem?**  
A: A model's nominal ability to accept long text does not guarantee that it can reliably use evidence wherever it appears in that text.

**Q: What is the independent variable?**  
A: Evidence position and answer procedure; context length is another planned factor once token-based conditions are frozen.

**Q: What is the dependent variable?**  
A: Answer correctness and evidence-ID precision/recall/F1. Input tokens and latency are resource outcomes.

**Q: Why are the examples synthetic?**  
A: They are software fixtures for checking data validation and controlled prompt construction. They are not research observations.

**Q: What is the main threat to validity?**  
A: A tiny synthetic fixture set cannot support generalization. The real study requires manually verified multi-document tasks, correct gold evidence, token-based context lengths and executed model comparisons.

**Q: What would count as a negative result?**  
A: No consistent change across evidence positions, or an evidence-first procedure that does not improve correctness/attribution. Such outcomes must be reported as observed.

**Q: Has the model experiment been completed?**  
A: Not in the supplied execution record. The current package contains a runnable inference scaffold and tests; model inference must be executed in the target Colab session before empirical claims can be made.

## Evaluation integrity

Do not award or claim experimental completion solely because a notebook runs or a paper is fluent. Check raw predictions, task provenance, frozen settings, metric computation and traceability from each table to its output file. All unresolved execution steps are explicitly marked `[TEST REQUIRED]`.
