# Progressive Video Training

**Type:** #method
**Status:** #seed
**Parent:** [[Machine Learning Training Strategies]]

---

## The Claim
A training strategy that separates conflicting objectives (control, quality, consistency) into sequential stages rather than optimizing them all end-to-end simultaneously.

## Context & Constraints
*   **Context:** Useful for complex generative tasks like long-video generation where objectives compete (e.g., strong control vs. natural motion).
*   **Failure Mode:** If earlier stages (like control injection) differ too much from the base model's distribution without regularization, later stages may fail to recover quality.

## Why it works
By isolating objectives, the model can converge on "easy" tasks (like following a depth map) before tackling "hard" tasks (like maintaining consistency over 5 minutes). This avoids the "tug-of-war" in gradients when optimizing for everything at once.

## Connections
*   **Source:** [[LongVie2_Ingestion]]
*   **Related:** [[Curriculum Learning]]
