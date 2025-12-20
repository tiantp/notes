# History Context Guidance

**Type:** #method
**Status:** #seed
**Parent:** [[Temporal Consistency]]

---

## The Claim
Explicitly encoding previous frames as conditioning latents for the current generation step, rather than relying solely on implicit hidden states, to enforce temporal coherence.

## Context & Constraints
*   **Context:** Long-form video generation where keeping a character's shirt color constant across 5 minutes is difficult.
*   **Failure Mode:** Can lead to "locking" where the model refuses to change the scene even when requested, because the history condition is too strong.

## Why it works
It treats the past as a localized "prompt" for the future, providing a reference signal that aligns the pixel statistics of the new frame with the old one.

## Connections
*   **Source:** [[LongVie2_Ingestion]]
*   **Related:** [[Context Window in LLMs]]
