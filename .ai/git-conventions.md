# Git Conventions

Naming conventions for branches, issues, and pull requests in BDM.
These apply to all contributors and to AI assistants working in this repository.

---

## Structure

```
GitHub Milestone  →  big goal, several weeks (M1, M2, M3...)
GitHub Issue      →  one concrete task, 1-3 days
Branch            →  one branch per issue
PR                →  one PR per branch, references the issue
```

Module numbers (M1.1, M1.4...) exist only in `.ai/milestones.md` as internal tracking.
They do not appear in branch names, issue titles, or PR titles.

---

## Branches

### Format

```
<type>/<short-description>
```

### Types

| Type | When to use |
|---|---|
| `feat/` | New functionality |
| `fix/` | Bug fix |
| `test/` | Tests only, no production code changes |
| `docs/` | Documentation only |
| `research/` | Hypotheses, experiment designs, research notes |
| `probe/` | Measurement and evaluation layer |
| `refactor/` | Internal restructure, no behavior change |
| `chore/` | Tooling, CI, config, dependencies |

### Examples

```
feat/sqlite-long-term-store
feat/memory-text-search
feat/memory-scoring
feat/reflection-engine
feat/self-model-goals
fix/short-term-buffer-eviction-index
test/episodic-record-coverage
docs/manifesto-consciousness-framing
research/h6-memory-reconstruction
probe/continuity-cross-session
probe/consistency-self-contradiction
chore/ci-pytest-workflow
```

### Rules

- All lowercase, words separated by hyphens
- No slashes inside the description part
- Describe the change, not the process
- Never commit directly to `main`
- One branch per issue, one PR per branch

---

## Issues

### Format

```
[<tag>] Short description of what to build or fix
```

### Tags

| Tag | When to use |
|---|---|
| `[feat]` | New functionality tied to a milestone |
| `[bug]` | Something is broken |
| `[test]` | Tests missing or broken |
| `[research]` | Hypothesis, experiment design, reading |
| `[probe]` | Measurement or evaluation task |
| `[docs]` | Documentation task |
| `[chore]` | Tooling, CI, config |
| `[discussion]` | Open question, not yet a concrete task |

### Examples

```
[feat] SQLite persistence for LongTermStore
[feat] Text search in memory query
[feat] Importance and confidence scoring
[feat] Rule-based reflection engine
[feat] Add ActiveGoal to SelfModelState
[bug] ShortTermBuffer leaves stale entry in index after eviction
[test] Add coverage for EpisodicRecord
[test] Add coverage for ContinuityContext
[research] Design experiment for H6 — memory reconstruction
[research] Add hypothesis — embodiment as prerequisite for meaning
[probe] Cross-session continuity probe
[probe] Self-contradiction consistency probe
[docs] Update roadmap with M1 completion
[chore] Add pytest GitHub Actions workflow
[discussion] SQLite FTS5 vs embedding search for text memory query
```

### GitHub Milestone assignment

Every `[feat]`, `[bug]`, `[test]` issue must be assigned to a GitHub Milestone (M1, M2...).
`[research]`, `[probe]`, `[docs]`, `[chore]`, `[discussion]` may be unassigned or assigned to the relevant milestone.

### Labels

| Label | Color | Description |
|---|---|---|
| `milestone:m1` | `#0052cc` | Milestone 1 — Memory Core |
| `milestone:m2` | `#0052cc` | Milestone 2 — Reflection Loop |
| `milestone:m3` | `#0052cc` | Milestone 3 — Self-Model |
| `milestone:m4` | `#0052cc` | Milestone 4 — Continuity |
| `milestone:m5` | `#0052cc` | Milestone 5 — LLM Integration |
| `milestone:m6` | `#0052cc` | Milestone 6 — CLI |
| `milestone:m7` | `#0052cc` | Milestone 7 — Experiments |
| `type:feat` | `#0e8a16` | New feature |
| `type:fix` | `#e11d48` | Bug fix |
| `type:test` | `#7c3aed` | Tests only |
| `type:docs` | `#f59e0b` | Documentation |
| `type:research` | `#06b6d4` | Research |
| `type:probe` | `#06b6d4` | Measurement / evaluation |
| `type:chore` | `#6b7280` | Tooling, CI, config |
| `branch:framework` | `#1d4ed8` | Work in packages/ |
| `branch:research` | `#0891b2` | Work in research/ or docs/ |
| `branch:probe` | `#0891b2` | Work in bdm.probe |
| `status:blocked` | `#dc2626` | Cannot proceed — reason in issue |
| `status:needs-discussion` | `#d97706` | Open question before work starts |

---

## Pull requests

### Title format

```
<type>(<scope>): <short description> (#<issue-number>)
```

### Scope

Use the milestone name or module name — short, lowercase:

```
feat(memory): add SQLite persistence to LongTermStore (#12)
feat(memory): add text search to memory query (#15)
fix(memory): remove stale index entry on buffer eviction (#8)
test(memory): add coverage for EpisodicRecord (#14)
feat(reflection): implement rule-based reflection engine (#20)
docs(manifesto): reframe primary goal around consciousness research (#3)
research(h6): add memory reconstruction experiment design (#19)
probe(continuity): implement cross-session continuity probe (#21)
chore(ci): add pytest GitHub Actions workflow (#5)
```

### Rules

- Title must reference the issue number
- One PR per issue — do not bundle unrelated changes
- All tests must pass before requesting merge
- Use `.github/PULL_REQUEST_TEMPLATE.md` for the description
- Squash merge for `feat` and `fix` to keep `main` history clean
- Merge commit acceptable for large `research` or `docs` PRs

---

## Commit messages

```
<type>(<scope>): <short description>

feat, fix, test, docs, research, probe, chore, refactor
scope = module or area name (memory, reflection, self_model, continuity, ci...)
```

Examples:
```
feat(memory): add SQLite backend to LongTermStore
feat(memory): create table schema on first init
test(memory): add persistence tests for LongTermStore
fix(memory): remove stale index entry on buffer eviction
```

---

## Branch lifecycle

```
main
 └── feat/sqlite-long-term-store    ← branch from main
      └── [commits]
      └── PR → tests pass → squash merge to main
      └── branch deleted after merge
```

- Branch from `main`
- Work on the branch
- Open PR when ready, reference the issue
- Merge to `main` after review
- Delete branch after merge

No long-lived feature branches. No `develop` branch. `main` is always the working branch.
