# ADR-0001: Initial Approach

## Context
We selected **String Calculator** (tiny scope). Constraint: **Lazy Coder**.

## Decision
Follow strict Red→Green cycles with minimal implementation; defer refactors. Historian captures one pattern per loop.

## Alternatives
A) Refactor-as-you-go – rejected (blurs learning focus)  
B) Broader scope – rejected (risk of shallow docs)

## Consequences
+ Fast feedback, clearer learning capture  
− Requires discipline to defer refactors

## Links
PR: (add) • Tests: `tests/test_string_calculator.py`
