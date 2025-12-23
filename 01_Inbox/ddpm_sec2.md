# Section 2: Background (Derivation & Scaffolding)

**Source:** [https://arxiv.org/pdf/2006.11239](https://arxiv.org/pdf/2006.11239)
**Tags:** #math #derivation #variational_inference #markov_chains

## 1. Classification
*Type:* Foundational Theory / Mathematical Derivation

**Intent (Inferred):** *To gain the capability to...* mathematically formulate the intractable problem of "generating images from noise" as a tractable optimization problem using Variational Inference and Markov chains.

---

## 2. Core Structure (The Signal)

* **Problem:** Computing the exact log-likelihood $\log p_\theta(x_0)$ is intractable because it requires integrating over all possible latent trajectories $x_{1:T}$.
* **Mechanism:** The **Variational Lower Bound (ELBO)** combined with the **Markov property**. The loss is decomposed into minimizing the KL Divergence between the *learned* reverse step and the *tractable* forward posterior.
* **Assumptions:**
    * **Gaussian Transitions:** Both forward ($q$) and reverse ($p$) transitions are Gaussian.
    * **Markovian:** The state at $t$ depends *only* on $t-1$ (forward) or $t+1$ (reverse).
    * **Small Steps:** $\beta_t$ is small enough that the reverse distribution remains Gaussian.

---

## 3. Reconstruction (The Logic)
*The derivation logic in plain English:*
> We cannot calculate the probability of an image directly. Instead, we define a "forward" process that destroys the image into noise in a fixed, known way. We then mathematically demand that our neural network (the "reverse" process) match the behavior of this forward process running backward. By using Jensen's inequality, we swap the difficult integration problem for an easier expectation problem: minimizing the difference (KL divergence) between what the network predicts and what physics dictates the backward step *should* be given the starting image.

---

## 4. Bindings
* **Extends:** Variational Autoencoders (VAEs) — but effectively a VAE with $T$ hierarchical latent variables where the encoder is fixed (not learned).
* **Key Concept:** **Jensen’s Inequality** ($\log \mathbb{E}[x] \ge \mathbb{E}[\log x]$), used to establish the lower bound.

---

## 5. Cognitive Assets Extraction

### A. The Forward Process (Fixed Physics)
* **Definition:** A Markov chain that gradually adds Gaussian noise.
    $$q(x_t | x_{t-1}) := \mathcal{N}(x_t; \sqrt{1 - \beta_t}x_{t-1}, \beta_t \mathbf{I})$$
* **Invariant (The "Nice Property"):** We can sample $x_t$ at any timestep directly from $x_0$ without iterating, because the sum of Gaussians is Gaussian.
    $$q(x_t | x_0) = \mathcal{N}(x_t; \sqrt{\bar{\alpha}_t} x_0, (1 - \bar{\alpha}_t)\mathbf{I})$$
    *(Where $\alpha_t = 1 - \beta_t$ and $\bar{\alpha}_t = \prod \alpha_s$)*

### B. The Reverse Process (Learned Generative)
* **Definition:** A Markov chain with learned parameters $\theta$ that attempts to undo the noise.
    $$p_\theta(x_{t-1} | x_t) := \mathcal{N}(x_{t-1}; \mu_\theta(x_t, t), \Sigma_\theta(x_t, t))$$

### C. The Derivation Procedure (Optimization Target)
* **Step 1: Establish the Bound (ELBO)**
    Maximize the Lower Bound on the negative log-likelihood:
    $$\mathbb{E}[-\log p_\theta(x_0)] \leq \mathbb{E}_q \left[ -\log \frac{p_\theta(x_{0:T})}{q(x_{1:T}|x_0)} \right]$$

* **Step 2: Factorize via Markov Property**
    Expand terms based on the definition of the joint distribution:
    $$L = \mathbb{E}_q \left[ -\log p(x_T) - \sum_{t=1}^T \log \frac{p_\theta(x_{t-1}|x_t)}{q(x_t|x_{t-1})} \right]$$

* **Step 3: Rewrite as KL Divergence (The Runnable Loss)**
    Using Bayes' rule on the forward posterior $q(x_{t-1}|x_t, x_0)$, the loss separates into three distinct terms:
    $$L = L_T + L_{t-1} + L_0$$

    * **1. $L_T$ (Prior Matching):** $D_{KL}(q(x_T|x_0) || p(x_T))$
        * *Status:* **Constant**. Ignored during training (no parameters).
    * **2. $L_{t-1}$ (Denoising Step):** $\sum D_{KL}(q(x_{t-1}|x_t, x_0) || p_\theta(x_{t-1}|x_t))$
        * *Status:* **Primary Training Objective**. The network $p_\theta$ learns to predict the mean of $q(x_{t-1}|x_t, x_0)$.
        * *Why it works:* $q(x_{t-1}|x_t, x_0)$ is **tractable** (computable) because we know $x_0$.
    * **3. $L_0$ (Reconstruction):** $-\log p_\theta(x_0|x_1)$
        * *Status:* **Final Decoding**.

---

## 6. Live Edge
* [ ] **Variance Parameterization:** The derivation assumes $\Sigma_\theta$ matches the forward process variances $\sigma_t^2 \mathbf{I}$. Section 2 notes this is an assumption; later sections (and papers) explore learning $\Sigma_\theta$.
* [ ] **Discrete vs Continuous:** The derivation assumes continuous data structure ($x \in \mathbb{R}^D$), but image pixels are discrete integers $\{0...255\}$. Section 2 briefly mentions using a discrete log-likelihood decoder for $L_0$.
