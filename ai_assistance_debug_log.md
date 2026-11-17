# AI assistance and debugging log

Append one entry per genuine code generation, run, failure, fix and verification.

## Entry template
- Date/time:
- Prompt/task:
- Code file and version:
- Expected behavior:
- Actual command/cell:
- Actual output/traceback (verbatim):
- Confirmed evidence:
- Hypotheses:
- Smallest correction:
- Verification test:
- Edge case:
- Earlier results requiring rerun:
- Human decision/outcome:

## Current status
No Prompt 11 debugging case is recorded yet because no actual traceback or unexpected output has been supplied. Do not invent a failure.


## Update — 17 November 2026

- AI-assisted review compared notebook outputs with assignment requirements and project files.
- Human-verifiable correction: the generated context sizes `[3, 15]` are snippet counts, not token lengths; they must not be reported as token-window sizes.
- Human-verifiable correction: the three fictional task records and 18 variants are pipeline fixtures, not an independently sampled research benchmark.
- Human-verifiable integrity decision: no model results, accuracy, latency comparison, debugging incident or GitHub push is claimed without corresponding execution/remote evidence.
- Added inference and evaluation scaffolds. They are unexecuted and marked `[TEST REQUIRED]`.
