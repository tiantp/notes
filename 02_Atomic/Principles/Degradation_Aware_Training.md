# Degradation-aware training prevents autoregressive error accumulation

**Type:** #principle
**Status:** #seed
**Parent:** [[Autoregressive Generation]]

---

## The Claim
Training a generative model on intentionally degraded inputs forces it to learn error-correction, preventing the "telephone game" effect where minor artifacts compound into severe hallucinations over long sequences.

## Context & Constraints
*   **Context:** Critical for autoregressive video or image generation where the output of step T becomes the input of step T+1.
*   **Failure Mode:** If degradation during training doesn't match the actual inference-time drift, the model may over-correct or fail to recognize valid artifacts.

## Why it works
It shifts the model's task from "generate X from perfect input Y" to "recover X from imperfect input Y'", making the inference process robust to its own structural imperfections.

## Connections
*   **Source:** [[LongVie2_Ingestion]]
*   **Related:** [[Denoising Autoencoders]]
