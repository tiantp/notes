# SoFlow

**Type:** #model
**Status:** #seed
**Parent:** [[Generative Models]]

---

## The Claim
SoFlow is a one-step generative framework that directly learns the ODE solution function (noise-to-image mapping) by coupling a Flow Matching loss with a JVP-free Solution Consistency loss.

## Context & Constraints
* **Context:** Used for training high-speed image generation models where inference latency (one-step) and training efficiency (low VRAM) are critical.
* **Failure Mode:** Fails if the velocity field is not smooth (Lipschitz violation) or if the Flow Matching loss does not converge, leaving the consistency loss without a directional guide (Guidance Collapse).

## Why it works
It bypasses the need for iterative solvers by training a network to predict the final integration result ($x_0$) directly. It ensures accuracy not by simulation, but by enforcing a geometric constraint: if the model takes a small step in the direction of the learned velocity, its prediction of the final destination should not change.

## Connections
* **Source:** [[SoFlow: Solution Flow Models for One-Step Generative Modeling]]
* **Related:** [[Flow Matching]]
* **Related:** [[Consistency Models]]
