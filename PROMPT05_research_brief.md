# Prompt 05 — Research brief and success criteria

## Problem
The review distinguishes nominal context capacity from effective evidence use and discusses evidence position, distractors and distributed evidence. The proposed experiment is an inference derived from that review.

## Primary research question
In a controlled multi-document evidence task, how do context length and supporting-evidence position affect answer correctness and evidence selection for an open-weight language model?

## Secondary question
Does identifying supporting evidence before answering change correctness or evidence-selection accuracy relative to direct answering?

## Hypotheses (INFERRED)
- H1: Correctness and/or evidence-selection accuracy may differ by evidence position.
- H2: Evidence-first prompting may change performance relative to direct answering.
These are hypotheses, not results. Null or contrary results are valid.

## Variables and measures
- Independent variables: context (short/long), evidence position (beginning/middle/end), procedure (direct/evidence-first).
- Controls: same checkpoint, question, source content, output format, decoding settings and scoring.
- Primary metric: answer correctness using a predefined normalized exact-match/rubric rule.
- Secondary: supporting-source ID exact-set accuracy, invalid source-ID rate, input tokens and latency.
- Decision rule: report observed differences and denominators; treat a small pilot as feasibility/effect-estimation, not definitive proof.
- Contrary observation: no meaningful differences, or evidence-first reduces correctness/increases unsupported source IDs.

## Input/output
Input JSONL: `task_id`, `question`, `evidence_snippets`, `distractor_snippets`, `gold_answer`, `gold_evidence_ids`.  
Output JSONL: raw output, parsed answer/IDs, correctness, evidence score, token count, latency and parse errors.

## Limitations
A small synthetic pilot may not represent real papers, tables, contradictory studies or full literature synthesis. Human-checked gold labels are required.
