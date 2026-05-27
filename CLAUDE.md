# CLAUDE.md — Beautiful Deep Mind

This file is read automatically by Claude Code at the start of every session.
It defines how Claude should behave in this repository.

---

## Read this first

**Current work, active task, and why:** `.ai/current.md`

Always read `.ai/current.md` before starting any task. It tells you what is being worked on right now, which branch of the project it belongs to, and what is explicitly out of scope. If the user asks you to do something not covered there, confirm before proceeding.

---

## Project identity

**Beautiful Deep Mind (BDM)** is an experimental cognitive architecture project.
It explores persistent memory, reflection loops, self-modeling, and context continuity in AI-assisted systems.

It does **not** claim to create consciousness. It does **not** make medical claims.
It is software research. Treat it as such.

Full context: `.ai/project.md`
Behavioral rules: `.ai/behavior.md`
Architecture decisions: `.ai/architecture.md`
Current milestone: `.ai/milestones.md`

---

## Current focus

See `.ai/current.md` — that file is the authoritative source of what is active right now.
Never rely on this file for current task context; it may be stale. `current.md` is always up to date.

---

## Running the project

```bash
# Install in development mode (from packages/bdm-core/)
pip install -e ".[dev]"

# Run tests
pytest

# Run with coverage
pytest --cov=bdm
```

---

## Key rules (summary)

1. Write only in **English** — code, comments, docstrings, commit messages, everything.
2. No consciousness claims in any code, comment, or string.
3. No medical claims anywhere.
4. Every new module needs tests before it is considered done.
5. Do not add features beyond what the current milestone requires.
6. Do not create `*.md` files unless the user asks.
7. Keep comments minimal — only write one if the WHY is non-obvious.
8. Run `pytest` before declaring any task complete.

Full rules: `.ai/behavior.md`

---

## Package structure

```
packages/
└── bdm-core/
    ├── src/bdm/
    │   ├── memory/       ← Milestone 1 (active)
    │   ├── reflection/   ← Milestone 2
    │   ├── self_model/   ← Milestone 3
    │   └── continuity/   ← Milestone 4
    └── tests/
```

---

## Naming conventions

Branch names, issue titles, PR titles, commit messages: `.ai/git-conventions.md`

Short version:
```
branch:  feat/sqlite-long-term-store
issue:   [feat] SQLite persistence for LongTermStore
PR:      feat(memory): add SQLite persistence to LongTermStore (#12)
commit:  feat(memory): add SQLite persistence to LongTermStore
```

---

## What Claude should never do in this repo

- Claim BDM is or could become conscious
- Add features not requested in the current milestone
- Skip writing tests for new code
- Write multi-paragraph docstrings or inline comment blocks
- Create planning documents or analysis files without being asked
- Modify `LICENSE.md`, `CONTRIBUTING.md`, or `.ai/behavior.md` without explicit instruction
- Push to remote without explicit user confirmation
- Use `git add -A` or `git add .` — always stage specific files
