# Prompt 06 — Dataset and comparator validation sheet

## Dataset
Start with a custom, manually verified JSONL pilot containing source snippets, questions, gold answers and gold supporting snippet IDs. It is a controlled pilot, not a public benchmark or novelty claim.

Benefits: allows evidence position/distractor control, human-checked labels, and avoids unnecessary full-paper redistribution. Risks: synthetic tasks may be easier than real scientific synthesis and have limited ecological validity.

## Comparators
1. **Direct full-context:** provide the condition's snippets and ask for answer plus supporting IDs.
2. **Evidence-first full-context:** ask for evidence IDs/key evidence first, then answer from the selected evidence.
3. **Optional later comparator:** fixed lexical retriever (e.g., BM25) top-k snippets, only after the baseline works.

These are proposed study conditions, not reproductions of complete published methods.

## Evaluation protocol
- Debug on pilot tasks; do not tune using held-out evaluation results.
- Keep task IDs and gold labels matched across conditions.
- If the dataset grows, split by underlying task/source family to prevent near-duplicate leakage.
- Record checkpoint, tokenizer, prompt, generation settings, package versions and seeds.
- Report denominators and invalid/missing output rates.
- No model training for the initial inference-only pilot.

## Checks
- [ ] Verify model license and access terms.
- [ ] Confirm checkpoint fits the actual Colab GPU.
- [ ] Record source/license if a public benchmark subset is later used.
- [ ] Keep credentials out of notebooks/repository.
- [ ] Document task authorship and human verification.

Do not begin model inference until environment test passes and model ID/access are confirmed.
