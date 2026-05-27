# Project Overview

## Name

Beautiful Deep Mind (BDM)

## One-line description

An experimental cognitive architecture and research framework for investigating what consciousness is and why current computational systems cannot be minds the way a human brain is.

## Primary goal

> BDM investigates the question of consciousness and the gap between computation and cognition — by building software models of memory, reflection, self-modeling, and continuity, and studying where those models succeed, where they fail, and what those failures reveal.

The framework (memory layers, reflection loop, self-model, continuity) is an instrument of investigation, not a product. The question is not "how do we build a better AI assistant." The question is: what is missing from a computer that a brain has — and is that gap an engineering problem or something more fundamental?

BDM does not claim to create consciousness.
BDM does not make medical claims.
BDM does not claim to copy, upload, or preserve a human mind.
It is software research. Every claim is a hypothesis until tested.

## What BDM is building

A layered system where:

1. **Memory** — the system stores structured records of events, facts, and interactions
2. **Attention** — the system retrieves relevant memory in response to current input
3. **Reflection** — the system checks new outputs against prior ones for consistency
4. **Learning loop** — the system updates stored beliefs based on feedback and corrections
5. **Self-model** — the system maintains a structured record of its own knowledge state
6. **Continuity** — the system preserves context across sessions
7. **LLM Integration** — these layers augment an LLM as a substrate

## What BDM is not building

- A general-purpose AI assistant (not the goal)
- A brain simulation (not attempted)
- A consciousness engine (explicitly disclaimed)
- A medical tool (explicitly disclaimed)
- A commercial product (not yet, possibly never)

## Repository owner

Boring Code — hello@boringcode.pl

## License

Source-available, all rights reserved. See `LICENSE.md`.

## Development language

Python 3.11+

## Package layout

```
packages/
├── bdm-core/     — core cognitive architecture layers
└── bdm-cli/      — command-line interface (Milestone 6)
```

## Current development phase

**Milestone 1 — Memory Core** (in progress)

See `.ai/milestones.md` for full breakdown.
