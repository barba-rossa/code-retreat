# Micro‑Mob Kata: **The Historian’s Loop**

Practice shipping a tiny feature **and** capturing learning with AI. Designed for **3–4 people** in **90–120 minutes**.

## Quick Start
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest -q        # run tests
# enable pre-commit docs gate
git init && git config core.hooksPath .hooks && chmod +x .hooks/pre-commit tools/check-docs.sh
```

## Roles
- **Driver**: types code.
- **Navigator**: sets intent, writes tests.
- **Historian**: maintains `docs/`, prompts AI to summarize.
- **AI Partner**: Coder + Reviewer + Referee (single chat/session).

## Session Plan (90 min)
1. **Kick‑off (10m)** – pick kata + constraint, create ADR.
2. **Loops ×3 (45m)** – Red→Green cycles; Historian captures learning.
3. **Reset Drill (15m)** – clear chat; rebuild only from docs.
4. **Refactor + Retro (15m)** – consolidate patterns/prompts.
5. **Show & Tell (5m)** – demo tests + docs.
   
## Katas (pick ONE small scope)
- **String Calculator**: `add("1,2") → 3` (incl. newlines).
- **Game of Life (single step)**: next generation on small grid.
- **Bowling Frame**: score a single frame incl. spare/strike.

## Light Constraints (pick ONE)
- **Lazy Coder** (minimal code per test)
- **Literate Programming** (code reads like prose)
- **One Level of Indentation**

## Learning Artifacts
- `docs/learn.md` – mini‑patterns, pitfalls, questions.
- `docs/prompts.md` – copy‑pasteable prompts.
- `docs/retro.md` – retro notes.
- `docs/20-ADRs/ADR-0001-initial-approach.md` – starter ADR.

## AI Prompt Cards
See `docs/prompt_cards.md` for ready‑to‑use Historian/Reviewer/Referee prompts.

Happy learning! 🚀
