# Current Work

This file defines what is being worked on right now, why, and how it fits into the larger project.
Update this file every time focus shifts — before starting new work, not after.

---

## Project branch

**Framework — `bdm-core`**

BDM has two parallel branches of work:

| Branch | Purpose |
|---|---|
| **Research** | Studying consciousness, documenting hypotheses, designing experiments |
| **Framework** | Building the software tools that make those experiments possible |
| **Probe** | Measurement layer — tests that compare BDM-augmented vs baseline systems |

Current work is in **Framework**, building the foundation that Research and Probe depend on.

---

## Active milestone

**M1 — Memory Core**

The memory layer is the prerequisite for everything else. Without persistent memory that survives across sessions, the research questions about continuity, identity, and consciousness gaps cannot be tested at all. You cannot study whether a system "remembers who it talked to yesterday" if the system has no yesterday.

---

## Current focus

**M1.4 — SQLite persistence for `LongTermStore`**

Right now `LongTermStore` is backed by a plain Python dict. It works, but it is completely ephemeral — all stored events disappear when the process ends. This makes it useless for any cross-session research.

The task is to replace the in-memory dict backend with SQLite so that `MemoryEvent` records survive across restarts.

**Why this specifically:**
- It is the smallest change that makes the memory layer actually useful for research
- SQLite is stdlib — no new dependencies
- The `MemoryStore` ABC means the swap is contained to `long_term.py` only
- Everything above it (`ShortTermBuffer`, `EpisodicRecord`, future layers) stays unchanged

---

## How this serves the main research goal

The main question BDM investigates is: *what is consciousness, and why can a computer not be a brain?*

One of the hypotheses (H6) is that computational memory is structurally different from biological memory — not just in implementation, but in what it is for. To study that difference, you first need a working memory system you can observe and probe. Without SQLite persistence, every experiment resets. You cannot accumulate observations. You cannot build a "history" to study.

SQLite persistence is not the research. It is what makes the research possible.

---

## What comes directly after

Once SQLite is working:

1. **`scoring.py`** (M1.7) — compute salience from recency and retrieval frequency
2. **`examples/memory_demo.py`** — end-to-end demo of adding, persisting, and querying memories
3. **`bdm.probe.continuity`** — first research probe: does the system know what happened in a prior session?

The probe is where Framework connects back to Research. It is the first measurable test of a research hypothesis using real persisted data.

---

## What is explicitly out of scope right now

- Reflection loop (M2) — depends on M1 being complete
- Self-model extensions (M3) — depends on M2
- LLM integration (M5) — depends on M1–M4
- CLI (M6) — last
- Any changes to documentation not directly related to current work
