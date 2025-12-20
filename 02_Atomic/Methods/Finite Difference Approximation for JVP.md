# Finite Difference Approximation for JVP

**Type:** #method
**Status:** #seed
**Parent:** [[Optimization Techniques]]

---

## The Claim
Expensive Jacobian-Vector Product (JVP) computations in neural network training can be replaced by a finite difference approximation (comparing $f(x)$ and $f(x + \epsilon)$) to significantly reduce memory usage without sacrificing convergence.

## Context & Constraints
* **Context:** Useful in training geometric or physics-informed deep learning models where derivatives of the output with respect to the input are required in the loss function.
* **Failure Mode:** If the step size ($\epsilon$) is too large, approximation error leads to bias. If too small, numerical instability (vanishing signal) occurs.

## Why it works
The definition of a derivative is the limit of the difference quotient. In high-dimensional optimization, computing the exact derivative (Jacobian) is memory-intensive ($O(N^2)$ or similar depending on implementation), whereas computing the difference between two forward passes is memory-efficient ($O(N)$).

## Connections
* **Source:** [[SoFlow: Solution Flow Models for One-Step Generative Modeling]]
* **Related:** [[Taylor Expansion]]
