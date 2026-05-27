# Beautiful Deep Mind (BDM)

An experimental cognitive architecture and research framework for investigating what consciousness is and why current computational systems cannot be minds the way a human brain is.

---

## What is BDM?

BDM asks one central question:

> What is consciousness, and why can a computer — at least as we currently build them — not have it the way a human brain does?

The framework (persistent memory, reflection loops, self-modeling, context continuity) is an instrument of investigation, not a product. It is built to probe the boundary between computation and cognition — to study where software models of cognitive properties succeed, where they fail, and what those failures reveal.

BDM does **not** claim to create consciousness. It does **not** make medical claims. It is software research.

---

## What BDM Is Not

- Not a medical product or clinical tool
- Not a consciousness engine or proof of machine sentience
- Not a brain simulation or connectome model
- Not a mind-upload or mind-transfer technology
- Not a general-purpose AI assistant
- Not production software (early research phase)

---

## Main Goals

1. Explore whether persistent memory, reflection, self-modeling, and continuity produce measurably different system behavior
2. Study where software analogues of cognitive properties break down and what that reveals
3. Investigate the structural gap between computational memory and biological memory
4. Probe the boundary between capable computation and genuine cognition
5. Publish all findings — including negative results — openly

---

## Conceptual Modules

| Module | Description |
|---|---|
| Memory Layer | Stores episodic, semantic, and working memory structures |
| Attention Layer | Selects relevant context from memory and input |
| Reflection Layer | Reviews prior outputs for consistency |
| Learning Loop | Updates internal state based on feedback and new experience |
| Self-Model Layer | Maintains a lightweight record of the system's own state |
| Context Continuity | Preserves thread of context across sessions |
| Interface Layer | Connects layers to external inputs and LLMs |

---

## Repository Status

**Milestone 1 — Memory Core — in progress.**

M0 (documentation and foundation) is complete. Active work is in `packages/bdm-core/src/bdm/memory/`.

---

## Repository Structure

```
bdm/
├── README.md
├── CLAUDE.md                       — Claude Code session context
├── CONTRIBUTING.md                 — contribution rules
├── LICENSE.md                      — source-available, all rights reserved
│
├── .ai/                            — AI assistant context directory
│   ├── README.md
│   ├── project.md                  — project overview and goals
│   ├── behavior.md                 — rules for AI assistants
│   ├── architecture.md             — architectural decisions
│   ├── milestones.md               — milestone status tracker
│   ├── current.md                  — active task and focus
│   ├── git-conventions.md          — branch, issue, PR naming
│   └── specs/                      — per-module specifications
│       ├── memory-event.md
│       ├── memory-store.md
│       ├── reflection-loop.md
│       ├── self-model.md
│       └── continuity.md
│
├── docs/
│   ├── en/                         — English documentation
│   │   ├── manifesto.md
│   │   ├── theory.md
│   │   ├── roadmap.md
│   │   ├── glossary.md
│   │   ├── architecture.md
│   │   └── ethics.md
│   └── pl/                         — Dokumentacja po polsku
│       ├── manifest.md
│       ├── teoria.md
│       ├── mapa-drogowa.md
│       ├── slownik.md
│       ├── architektura.md
│       └── etyka.md
│
├── concepts/
│   ├── en/                         — English concept files
│   │   ├── memory.md
│   │   ├── attention.md
│   │   ├── reflection.md
│   │   ├── learning-loop.md
│   │   ├── self-model.md
│   │   └── continuity.md
│   └── pl/                         — Koncepcje po polsku
│       ├── pamiec.md
│       ├── uwaga.md
│       ├── refleksja.md
│       ├── petla-uczenia.md
│       ├── model-siebie.md
│       └── ciaglosc.md
│
├── research/
│   ├── en/                         — English research documents
│   │   ├── hypotheses.md
│   │   ├── experiments.md
│   │   └── reading-list.md
│   └── pl/                         — Dokumenty badawcze po polsku
│       ├── hipotezy.md
│       ├── eksperymenty.md
│       └── lista-lektur.md
│
├── packages/
│   ├── bdm-core/                   — Core cognitive architecture package
│   │   ├── pyproject.toml
│   │   ├── src/bdm/
│   │   │   ├── memory/             — M1: MemoryEvent, stores, episodic (active)
│   │   │   ├── reflection/         — M2: ReflectionLoop (stub)
│   │   │   ├── self_model/         — M3: SelfModelState (stub)
│   │   │   └── continuity/         — M4: ContinuityContext (stub)
│   │   └── tests/
│   └── examples/
│       └── memory_demo.py
│
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── task.md
│   │   ├── bug.md
│   │   └── experiment.md
│   └── PULL_REQUEST_TEMPLATE.md
│
└── .gitignore
```

---

## License and Contributions

Beautiful Deep Mind is source-available, but it is not open source.

All rights are reserved by Boring Code. You may read and evaluate the repository, but you may not copy, redistribute, commercialize, or create derivative works without written permission.

Contributions are welcome under the rules described in `CONTRIBUTING.md`. By submitting a contribution, you agree to the contribution terms described in `LICENSE.md`.

See:

- [`LICENSE.md`](./LICENSE.md)
- [`CONTRIBUTING.md`](./CONTRIBUTING.md)

---

## Disclaimer

BDM does not make medical claims. It does not claim to create, simulate, or replicate consciousness. It does not claim that software can copy, upload, transfer, or preserve a human mind. This project is software research inspired by cognitive science concepts. All claims are framed as hypotheses or research directions, not established results.
