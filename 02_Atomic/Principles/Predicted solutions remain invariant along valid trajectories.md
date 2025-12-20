# Predicted solutions remain invariant along valid trajectories

**Type:** #principle
**Status:** #seed
**Parent:** [[Differential Equations]]

---

## The Claim
In a deterministic system (ODE), if a state $x_t$ is moving along a valid trajectory towards a final state $x_0$, the prediction of that final state must remain constant ($d/dt = 0$) as the system evolves over time.

## Context & Constraints
* **Context:** Essential for "Consistency Models" in machine learning, where the goal is to map every point on a trajectory to the same origin point.
* **Failure Mode:** Breaks in stochastic systems where the trajectory is not deterministic, or if the step size used to measure invariance is too large (discretization error).

## Why it works
It relies on the definition of a solution flow. Since the "solution" is the endpoint of the integral curve, and the integral curve is fixed, moving along the curve does not change which curve you are on.

## Connections
* **Source:** [[SoFlow: Solution Flow Models for One-Step Generative Modeling]]
* **Related:** [[Conservation Laws]]
