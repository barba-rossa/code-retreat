# Prompt Library

## Historian – Learning Capture
Summarize our last change set:
- Goal
- What the AI misunderstood
- Fix we applied
- Lesson or pattern (≤50 words)
Output valid Markdown to append to `docs/learn.md`.

## Reviewer – Explain Before Doing
Restate the intent in your own words, list 3 steps, predict the next failing test. Ask 1 clarifying question. **Do not code yet.**

## Referee – Constraint Check
Check the diff against rule “[One level of indentation]”. List violations with file:line and a short fix suggestion.

## Coder – Minimal Pass
Implement the smallest change to make the **current failing test** pass. No refactors. Show only changed lines.
