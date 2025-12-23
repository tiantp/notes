# Denoising Diffusion Probabilistic Models

**Authors:** Jonathan Ho, Ajay Jain, Pieter Abbeel

**Source:** [https://arxiv.org/pdf/2006.11239](https://arxiv.org/pdf/2006.11239)

**Tags:** #inbox #processing #generative_models #ddpm

## 1. Classification
*Type:* Method

**Intent (Inferred):** *To gain the capability to...* generate high-fidelity data samples (images) by learning to reverse a gradual noise-addition process, stabilizing training compared to GANs.

---

## 2. Core Structure (The Signal)

* **Problem:** Generative Adversarial Networks (GANs) are unstable to train; Likelihood-based models (VAEs, Flows) often sacrifice sample quality or are computationally expensive to sample from.
* **Mechanism/Core Idea:** A parameterized Markov chain that learns to *reverse* a fixed diffusion process. The key differentiator is **predicting the noise** ($\epsilon$) added at each step rather than predicting the clean image directly, using a simplified weighted variational bound.
* **Assumptions:**
    * The forward destruction process is Gaussian and Markovian.
    * If the noise step size ($\beta_t$) is small enough, the reverse transition can also be approximated as a Gaussian.
* **Success Criteria:** State-of-the-art FID scores (image quality metric) on CIFAR-10 and LSUN datasets, beating or matching GANs without adversarial training.

---

## 3. Reconstruction (The Explanation)
*The core logic in plain English:*
> Nature tends to dissipate structure into randomness (diffusion). If we record this process of an image slowly turning into static noise, we can train a neural network to predict the exact "blob" of noise added at any single snapshot. By starting with pure static and iteratively subtracting the predicted noise (using the network) over thousands of small steps, we can reverse time and "crystallize" a coherent image out of randomness.

---

## 4. Bindings (Suggested)
* **Extends:** Non-equilibrium thermodynamics, Denoising Score Matching, Langevin Dynamics.
* **Contradicts:** The prevailing belief that adversarial objectives (discriminators) are necessary for high-fidelity image synthesis.
* **Similar to:** Autoregressive decoding (but acting on "noise levels" rather than pixel positions).

---

## 5. Cognitive Assets Extraction

* **Principles (Invariants):**
    * **Closed-Form Forward Step:** You can jump to any noise level $t$ instantly without iterating intermediate steps ($q(x_t|x_0)$ is Gaussian).
    * **Reverse Parameterization:** It is easier to learn the *noise* component ($\epsilon$) of a noisy image than the *mean* of the posterior.
    * **Simplified Loss:** Discarding the theoretically correct weighting term in the Variational Lower Bound (ELBO) leads to better sample quality (focuses learning on harder, lower-noise levels).

* **Procedures (Runnable):**

    * **1. Training Loop (Algorithm 1):**
        * Repeat until converged:
            1.  Sample a clean image $x_0$ from the dataset.
            2.  Sample a timestep $t \sim \text{Uniform}(\{1, \dots, T\})$.
            3.  Sample noise $\epsilon \sim \mathcal{N}(0, \mathbf{I})$.
            4.  Take a gradient descent step on the loss:
                $$\nabla_\theta \| \epsilon - \epsilon_\theta(\sqrt{\bar{\alpha}_t} x_0 + \sqrt{1-\bar{\alpha}_t}\epsilon, t) \|^2$$
                *(Essentially: Can the net guess what noise was added?)*

    * **2. Sampling Loop (Algorithm 2):**
        * Start with pure noise $x_T \sim \mathcal{N}(0, \mathbf{I})$.
        * For $t = T, \dots, 1$:
            1.  Sample $z \sim \mathcal{N}(0, \mathbf{I})$ (if $t > 1$, else $z=0$).
            2.  Update $x_{t-1}$ by subtracting predicted noise:
                $$x_{t-1} = \frac{1}{\sqrt{\alpha_t}} \left( x_t - \frac{1-\alpha_t}{\sqrt{1-\bar{\alpha}_t}} \epsilon_\theta(x_t, t) \right) + \sigma_t z$$

* **Failure Modes:**
    * **Slow Sampling:** Requires $T$ (often 1000) sequential forward passes of the network to generate one image.
    * **Pixel-Space Limitation:** Standard DDPM operates in pixel space, making it computationally expensive for high-resolution images (later solved by Latent Diffusion).

---

## 6. Live Edge
* [ ] **Likelihood vs. Quality:** The "simplified" loss function yields better samples but technically optimizes a different objective than the true log-likelihood. Why does this discrepancy exist?
* [ ] **Optimal Variance Schedule:** The paper uses a fixed linear schedule for $\beta_t$, but is this optimal? (Later research suggests cosine schedules).
