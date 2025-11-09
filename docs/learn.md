# Learning Log (Historian)

> Add a new section every loop. Keep it short and actionable.

# Bowling Game Implementation - Lesson Learned

## Goal
Implement `BowlingGame` so `test_bowling.py` can import it and the basic bowling scoring tests can run.

## What the AI Misunderstood
I focused on fixing the missing import and attempted to run pytest as a binary (not available), so I didn't fully verify test execution to completion.

## Fix We Applied
Added `bowling.py` with a `BowlingGame` class implementing `roll(pins)` and `score()` (including spare/strike handling) so the test import error is resolved.

## Lesson or Pattern
When tests fail with `ModuleNotFoundError`, add the minimal module implementing the expected public API; prefer `python -m pytest` if `pytest` isn't on PATH; make minimal, test-driven changes.




