# Research Hypotheses

This document records BDM's initial research hypotheses. Each hypothesis is stated precisely, accompanied by a rationale, a possible experiment, and acknowledged limitations.

These are working hypotheses. None are established results. The purpose of recording them here is to make the project's assumptions explicit, testable, and open to revision.

---

## H1 — Persistent Memory Improves Interaction Continuity

**Hypothesis:**
A system with persistent, structured memory of prior interactions will produce more contextually coherent responses across multi-session interactions than a system without persistent memory.

**Rationale:**
Without persistent memory, each session begins in a blank state. The system cannot reference prior commitments, correct prior errors, or build on prior exchanges. If continuity of context matters for coherent interaction — and there is reason to believe it does — then the absence of persistent memory is a structural limitation. Structured memory provides the raw material for continuity.

**Possible Experiment:**
Design a multi-session interaction protocol in which a user asks follow-up questions across multiple sessions. Compare a baseline (no persistent memory) against a memory-augmented system. Evaluate whether the memory-augmented system correctly references prior interactions, avoids contradicting prior statements, and requires fewer re-explanations from the user.

**Limitation:**
Coherence is difficult to measure objectively. Automatic metrics (e.g., embedding similarity to prior responses) may not capture meaningful consistency. Human evaluation is more reliable but harder to scale. The experiment will need careful evaluation design. Additionally, memory retrieval quality affects the outcome: poor retrieval of irrelevant prior context could degrade rather than improve coherence.

---

## H2 — Reflection Loops Improve Reasoning Consistency

**Hypothesis:**
A system that applies a reflection step — reviewing new outputs against stored prior outputs before finalizing a response — will produce fewer detectable inconsistencies over extended interactions than a system without reflection.

**Rationale:**
LLMs generate outputs without access to a structured record of what they have previously said. Over multiple interactions or sessions, they may contradict prior statements. A reflection step that explicitly compares new outputs to prior ones creates an opportunity to detect and correct inconsistencies before they are surfaced to the user.

**Possible Experiment:**
Run a series of interactions designed to produce opportunities for inconsistency — factual questions asked in varied forms across sessions, position questions asked again after several exchanges. Compare outputs with and without a reflection module. Measure the rate of detectable contradictions.

**Limitation:**
Reflection adds latency. A reflection step that is too slow may be impractical. Additionally, the reflection module itself may produce errors: it may flag legitimate updates to prior positions as inconsistencies, or fail to detect subtle ones. The quality of the reflection module is a confounding variable.

---

## H3 — A Self-Model Improves Uncertainty Representation

**Hypothesis:**
A system with access to a structured self-model — a representation of what it knows, what it does not know, and what confidence levels attach to its stored beliefs — will produce more accurate uncertainty statements than a system without one.

**Rationale:**
LLMs are known to produce confident-sounding outputs even in areas where their knowledge is limited or uncertain. A self-model that tracks known knowledge gaps and confidence levels could provide explicit signals that constrain the system's outputs in uncertain domains, leading to more appropriately hedged responses.

**Possible Experiment:**
Evaluate responses to questions in domains known to be outside the system's stored knowledge, comparing a baseline LLM to a self-model-augmented version. Measure the rate of inappropriate confidence (false certainty) and appropriate hedging (correct acknowledgment of uncertainty).

**Limitation:**
The self-model is only as accurate as the update mechanism that maintains it. A stale or inaccurate self-model could produce worse uncertainty representation than no self-model at all. Additionally, distinguishing "correct" uncertainty levels is itself a difficult evaluation challenge.

---

## H4 — Context Continuity Is Necessary for Long-Term Adaptive Behavior

**Hypothesis:**
A system that lacks continuity of internal context across sessions will fail to exhibit adaptive behavior — adjusting responses based on accumulated experience — beyond the duration of a single session.

**Rationale:**
Adaptation requires that prior experience inform current behavior. Without context continuity, there is no mechanism by which prior experience can influence a new session. This is a structural claim: continuity is a necessary (though not sufficient) condition for long-term adaptation.

**Possible Experiment:**
Design a scenario in which adaptation should occur over multiple sessions: the user repeatedly provides feedback on a type of response. Evaluate whether a system with continuity adapts its behavior across sessions, while a baseline without continuity does not.

**Limitation:**
This hypothesis tests a structural claim rather than an optimization claim. Even a system with continuity may fail to adapt if its learning loop is poorly designed. The experiment tests whether continuity is necessary, but does not tell us whether it is sufficient.

---

## H5 — Episodic Memory Improves Distinction Between Facts, Events, and Prior Interactions

**Hypothesis:**
A system with an episodic memory structure — records that include temporal and contextual metadata — will better distinguish between general facts, time-bound events, and prior interaction history than a system that stores all information in a flat, undifferentiated log.

**Rationale:**
Not all stored information is the same. A general fact (water boils at 100°C) is different from a prior interaction event (the user said X two sessions ago) and from a time-bound assertion (the current project status as of a given date). Mixing these without distinction degrades retrieval quality. Episodic records with appropriate metadata allow the system to apply different reasoning to different record types.

**Possible Experiment:**
Compare retrieval quality between a flat log system and an episodic memory system across query types: general knowledge queries, event-recall queries, and interaction-history queries. Evaluate whether episodic structure improves precision for each query type.

**Limitation:**
Assigning and maintaining episodic metadata correctly is non-trivial. If metadata is inaccurate or inconsistent, episodic structure may not improve retrieval. The experiment depends on having reliable ground truth for what type each record should be, which requires careful dataset construction.

---

---

## H6 — Computational Memory Is Structurally Different From Biological Memory

**Hypothesis:**
Even a well-designed persistent memory system in software will exhibit fundamental differences from biological memory that cannot be resolved through better engineering alone — specifically in how memory is encoded, decayed, reconstructed, and integrated with experience.

**Rationale:**
Biological memory is not storage. It is reconstruction. Every time a human recalls an event, the memory is partially rebuilt from stored traces, influenced by current context, emotion, and subsequent experience. It is also lossy by design — forgetting is not failure, it is a feature that maintains relevance. Computational memory, by contrast, is typically exact, persistent, and context-free. These are not just implementation differences. They may reflect something deeper about what memory is for in a conscious system.

**Possible Experiment:**
Design a series of recall tasks that exploit the reconstructive nature of biological memory (e.g., tasks where context changes the content of recall, tasks where emotional salience affects retention). Run equivalent tasks on a software memory system. Document systematically where the analogy breaks down and why.

**Limitation:**
This hypothesis is partly philosophical. "Fundamental difference" is hard to operationalize. The experiment will likely produce observations rather than a clean falsifiable result. That is acceptable — the goal is to characterize the gap, not to close it.

---

## H7 — A System Without Embodiment Cannot Develop Grounded Meaning

**Hypothesis:**
A software system that lacks embodiment — sensory experience, physical needs, temporal existence in the world — cannot develop meaning in the way a human brain does, regardless of how sophisticated its memory or reasoning structures become.

**Rationale:**
Meaning in human cognition is grounded in experience: the word "pain" means something because you have felt it; "hunger" because you have been hungry; "tomorrow" because you have lived through time. An LLM processes statistical relationships between tokens. It has no referent outside language. This may be a fundamental constraint on what such systems can understand, as opposed to what they can process.

**Possible Experiment:**
This hypothesis is difficult to test directly. An indirect approach: design tasks that require grounded reasoning — tasks where the correct answer depends on understanding what something feels like, not just what it is described as. Compare performance of memory-augmented and non-augmented systems. Evaluate whether adding memory changes anything for these tasks, or whether the limitation is structural.

**Limitation:**
The concept of "grounded meaning" is contested in philosophy of mind. This hypothesis may not be falsifiable in any strict sense. It is recorded here as a research direction and a framing device, not as a claim that can be resolved through software experiments alone.

---

## H8 — The Gap Between Computation and Consciousness Is Not Just a Matter of Scale or Architecture

**Hypothesis:**
Current AI systems are not non-conscious simply because they are not large enough, not complex enough, or not architecturally sophisticated enough. There is something categorically different about biological consciousness that is not addressed by scaling or architectural refinement alone.

**Rationale:**
A common implicit assumption in AI research is that consciousness will emerge from sufficient complexity or capability. BDM treats this as an open hypothesis, not a settled fact. The alternative — that consciousness requires something not present in current computational paradigms, such as embodiment, causal continuity, or a specific kind of physical substrate — is equally worth investigating. BDM's framework is designed to probe this boundary by adding cognitive-adjacent properties and observing what changes and what does not.

**Possible Experiment:**
After completing the core framework (memory, reflection, self-model, continuity), design a structured evaluation of what the augmented system can and cannot do compared to a baseline. Specifically look for capabilities that are expected to emerge if consciousness is a matter of architecture, and document which do not appear. Use this as evidence for or against the scaling hypothesis.

**Limitation:**
This hypothesis is extremely broad and will not be resolved by this project alone. BDM can contribute observations and structured arguments, not a proof. The value is in the rigor of the investigation, not in the finality of the conclusion.

---

*All hypotheses are subject to revision as the project develops. Hypotheses that are falsified will be recorded as such, with notes on what was learned.*
