This is a **serious, well-posed problem**, and fortunately there *is* a fairly coherent body of work on what actually works in practice. Below I’ll organize this as **a design-oriented related-work map**—not hype, but *mechanisms that demonstrably improve human thinking* and how they compose into a **cognitive exoskeleton**.

I’ll bias toward **methods that scale to large domains**, **improve internalization**, and **enable insight**, since that’s clearly your goal.

---

# Cognitive Exoskeleton: What Actually Works

## 0. Unifying Frame (important)

The most successful systems all share this property:

> **They externalize cognition into structured artifacts, then repeatedly force active reconstruction—not passive consumption.**

This is consistent across learning science, expert reasoning, HCI, and even top-tier research workflows.

---

## 1) Mapping Large Domains of Knowledge (Mental Cartography)

### 1.1 Concept Maps & Knowledge Graphs (but used correctly)

**What works**

* Hierarchical + relational representations
* Explicit causal, functional, or dependency links
* Progressive refinement (coarse → fine)

**Evidence**

* Concept mapping improves transfer and deep understanding vs linear notes
* Experts organize knowledge around **principles**, not facts

**Key insights**

* Flat graphs fail.
* Successful systems enforce:

  * *Why* links (causal, constraint, trade-off)
  * *Abstraction layers*

**Exoskeleton pattern**

```
Domain
 ├── Core principles
 │    ├── Constraints
 │    ├── Invariants
 │    └── Failure modes
 ├── Canonical problems
 └── Variations / edge cases
```

**Related work**

* Novak & Cañas — Concept Mapping
* Chi et al. — Expert vs novice knowledge structure
* Knowledge graphs for sense-making (HCI literature)

---

### 1.2 Zettelkasten (when not used naïvely)

**What works**

* Atomic notes
* Dense cross-linking
* Notes written as *claims*, not summaries

**What fails**

* Dumping facts
* No forcing function for synthesis

**Effective variants**

* “Permanent notes” that state:

  * A claim
  * Evidence
  * Implication

**Why it works**

* Mirrors associative memory
* Enables combinatorial recombination → insight

**Exoskeleton role**

> Long-term semantic substrate that insight engines can traverse.

---

## 2) Building and Invoking Thought Processes (Cognitive Programs)

This is *critical* and often missed.

### 2.1 Externalized Reasoning Templates (Cognitive Algorithms)

Experts don’t “think harder”—they **run procedures**.

**Examples**

* Feynman technique
* First-principles decomposition
* Inversion (“how would this fail?”)
* Hypothesis → test → update loops

**Evidence**

* Problem-solving research shows large gains when novices are taught **process**, not facts
* Checklists outperform memory under complexity (Atul Gawande)

**Exoskeleton pattern**

```
Thinking Module:
- When to use
- Inputs required
- Steps
- Failure checks
- Output format
```

This is essentially **procedural memory augmentation**.

---

### 2.2 Metacognitive Scaffolding (this is huge)

What reliably improves thinking:

* Prompts to explain reasoning
* Confidence calibration
* Forced alternative hypotheses
* “What would change my mind?”

**Related work**

* Metacognitive agents (misinformation defense)
* Self-explanation effect
* Cognitive forcing functions (medicine, aviation)

**Exoskeleton function**

> The system *interrupts* bad thinking automatically.

---

## 3) Recall of Important Facts (Memory That Actually Sticks)

### 3.1 Active Recall + Spaced Repetition (but structured)

**What works**

* Retrieval beats re-reading
* Spacing beats cramming

**What doesn’t**

* Isolated flashcards without conceptual hooks

**Best practice**

* Facts tied to:

  * A principle
  * A mental model
  * A failure case

**Exoskeleton pattern**

```
Fact → Why it matters → Where it breaks → What it connects to
```

**Evidence**

* Robust across decades of cognitive psychology

---

### 3.2 Memory Palaces / Spatial Encoding (underused but powerful)

**Why it works**

* Leverages ancient spatial memory circuits
* Used by memory champions *and* elite scientists historically

**Modern form**

* Visual dashboards
* Stable spatial layouts
* AR / whiteboard ecosystems

**Exoskeleton role**

> Gives memory *addresses*, not just labels.

---

## 4) Internalizing Concepts (From Knowing → Being Able to Use)

### 4.1 Generative Learning

People internalize concepts when they:

* Teach it
* Derive it
* Apply it to novel cases
* Explain failures

**Related work**

* Self-explanation effect
* Learning-by-teaching
* Productive failure

**Exoskeleton design**

* System forces:

  * Re-derivation
  * Counterexamples
  * Transfer tasks

---

### 4.2 Multiple Representations

Deep understanding requires:

* Verbal
* Mathematical
* Visual
* Procedural forms

**Evidence**

* Experts switch representations fluidly
* Misconceptions persist when only one form is used

**Exoskeleton role**

> Automatically translates concepts across representations.

---

## 5) Generating Innovative Insights (The Hard Part)

### 5.1 Insight = Structured Recombination

Breakthroughs often come from:

* Crossing domains
* Recombining abstractions
* Violating implicit constraints

**What helps**

* Dense cross-domain linking
* Explicit abstraction layers
* “Analogy engines”

**Related work**

* Analogical reasoning (Gentner)
* Conceptual blending
* Design cognition research

---

### 5.2 Incubation + External Persistence

Insights appear when:

* Problem is well-structured externally
* Mind is allowed to wander
* System preserves partial thoughts

**Exoskeleton function**

> Persistent external working memory + resurfacing unfinished structures.

---

## 6) A Practical Architecture (Synthesis)

Here’s a **working mental model** for a cognitive exoskeleton:

```
[Knowledge Substrate]
  - Concept maps
  - Atomic notes
  - Cross-domain links

[Process Library]
  - Thinking templates
  - Metacognitive checks
  - Decision protocols

[Memory Engine]
  - Structured recall
  - Spaced resurfacing
  - Spatial anchors

[Insight Engine]
  - Analogy prompts
  - Constraint violation probes
  - Synthesis tasks

[Human-in-the-loop]
  - Active reconstruction
  - Teaching / explaining
  - Judgment & taste
```

LLMs are **excellent glue** for:

* Translation across representations
* Prompting metacognition
* Surfacing distant links

But **humans must still own**:

* Goal selection
* Value judgment
* Sense of importance
