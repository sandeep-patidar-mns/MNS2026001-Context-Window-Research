# Prompt 03 — Literature-to-experiment mapping

**Student:** Sandeep Patidar | **Roll no.:** MNS2026001  
**Review:** *Context-Window Degradation and Its Impact on Long-Document Research Synthesis*

## Source-grounded resources

| Published work | Verified high-level contribution | Use in this project | Boundary |
|---|---|---|---|
| Liu et al., *Lost in the Middle* (TACL 2024) | Tests position sensitivity for relevant information in multi-document QA and key-value retrieval. | Protocol precedent: keep evidence fixed and move it to beginning, middle, end. | Our task/model results are unknown; not a reproduction unless details are matched. |
| Bai et al., *LongBench* (ACL 2024) | 21 datasets across six long-context task categories, including multi-document QA and summarization. | Guides task selection and evaluation discipline. | A small pilot is not a LongBench reproduction. |
| Modarressi et al., *NoLiMa* (ICML 2025) | Tests long-context evaluation with reduced lexical overlap and reports length-related degradation. | Avoid trivial lexical-copy tasks; use paraphrased evidence. | Our custom pilot is not NoLiMa. |
| Du et al., *Context Length Alone Hurts LLM Performance Despite Perfect Retrieval* (Findings EMNLP 2025) | Studies length-related performance degradation and evidence-recitation as a mitigation. | Candidate comparison: direct answering vs evidence-first answering. | Published effects do not predict our results. |

## Pathways
- **A — Reproduction plus extension:** reproduce a narrow evidence-position test, then extend to source-grounded multi-document synthesis.
- **B — Controlled comparison:** full context vs retrieval vs compression/hybrid. More engineering and resource accounting.
- **C — Targeted modification:** direct answer vs evidence-first prompt, holding model, question and evidence fixed.

**Provisional recommendation (INFERRED):** begin with A and one isolated procedure comparison. Do not add a full retrieval pipeline until the baseline is validated.

## Minimal pilot
- Task: answer synthesis questions from 2–4 source snippets with gold answer and supporting snippet IDs.
- Factors: short/long context; evidence at beginning/middle/end.
- Conditions: direct answer; evidence-first then answer.
- Outputs: raw answer, predicted source IDs, correctness, evidence coverage, input-token count and latency.
- Evidence needed: task JSONL, prompt templates, model/version, generation settings, raw outputs and scoring script.

## Status
**VERIFIED from primary publisher pages:** bibliographic records and high-level descriptions of the four works above. **INFERRED:** proposed pilot design. **UNKNOWN:** novelty of this exact combination, exact model feasibility, and full methodological overlap after primary-paper audit.
