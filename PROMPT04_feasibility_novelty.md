# Prompt 04 — Feasibility and novelty verification

## Proposed idea
Test how context length and supporting-evidence position affect correctness and source selection in a small multi-document task, comparing direct answering with evidence-first answering.

| Neighboring work | Verified contribution at a high level | Difference to test | Still missing |
|---|---|---|---|
| *Lost in the Middle* | Position-sensitive evaluation for multi-document QA and key-value retrieval. | Source-grounded synthesis and explicit supporting-source IDs. | Full protocol/model/metric comparison. |
| LongBench | Broad long-context benchmark with QA, summarization and other tasks. | Narrow controlled pilot rather than broad benchmark. | Suitable subset/license/scoring details. |
| NoLiMa | Long-context tasks with reduced lexical overlap. | Paraphrased source evidence in a small pilot. | Exact task construction and overlap audit. |
| *Context Length Alone Hurts...* | Tests length degradation despite perfect retrieval and evidence recitation. | Source-evidence synthesis plus source-ID tracking. | Whether exact conditions already exist in the original study or related work. |

## Feasibility
- Environment: Google Colab with NVIDIA GPU (user-reported); exact GPU/VRAM is **UNKNOWN** until diagnostic output.
- Dataset: manually checked small JSONL pilot. This is custom data, not a public benchmark.
- Time and runtime: **UNKNOWN**; start with 20 tasks only after environment/model checks.
- Model: do not freeze until GPU memory, access terms, license and runtime are checked.
- Fallback: smaller compatible open model or permitted API after documenting cost/access. Never silently switch.

## Novelty search strings
- `"long-context" "multi-document question answering" position`
- `"long context" evidence attribution summarization LLM`
- `"context length" "evidence recitation" LLM`
- `"effective context" benchmark synthesis`
- `"long document" claim-level attribution LLM evaluation`

**Decision: CONDITIONAL GO for a pilot, not novelty clearance.** Do not claim novelty or improvement. Verify original methods and run the Colab diagnostic first.
