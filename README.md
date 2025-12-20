# Exoskeleton for the Mind

> A system to wrap around your cognition—helping you remember, reason, and make better decisions.

This repository is structured as a **Cognitive Exoskeleton** based on principles of Intelligence Amplification, distributed cognition, and active recall. It is not just a storage bin for notes; it is a machine for **processing** and **synthesizing** information.

## 📂 Structure

The directory structure mirrors the cognitive pipeline: `Ingest` → `Process` → `Store` → `Act`.

*   **`00_Map/`**: **The Global Shape**. Visual concept maps, dependency trees, and "Maps of Ignorance". Start here to orient yourself in a domain.
*   **`01_Inbox/`**: **Raw Signal**. Dump papers, PDFs, and brain-dumps here. They are temporary.
*   **`02_Atomic/`**: **The Knowledge Base**.
    *   `Concepts/`: Definitions and core objects.
    *   `Principles/`: Invariants and Rules (Claims).
    *   `Models/`: Systems and relationships.
    *   `Evidence/`: Case studies and data points.
*   **`03_Procedures/`**: **Algorithms**. Runnable checklists and thinking tools (e.g., "Debugging Loop", "Decision Razor").
*   **`04_Memory/`**: **Flashcards**. Source files for Anki/Spaced-Repetition.
*   **`05_Projects/`**: **Output**. Active work utilizing the exoskeleton.
*   **`99_System/`**: **The Engine**. Templates and scripts to maintain the exoskeleton.

## ⚙️ The Workflow

### 1. Ingestion (Turning Noise into Signal)
When you find a new paper/article:
1.  Full file goes into `01_Inbox`.
2.  Create a processing note using `99_System/Templates/Source_Ingestion.md`.
3.  **Do not copy-paste.** Extract the *structure*, *reconstruct* the idea, and *bind* it to existing links.

### 2. Atomization (Permament Storage)
Once you understand an idea:
1.  Create a note in `02_Atomic/`.
2.  Use the `Atomic_Node.md` template.
3.  **Rule**: One Idea = One File.
4.  **Rule**: Title must be a claim or object name, not a sentence.

### 3. Resurfacing (The "Alive" Component)
This system is designed to force recombination. Run the resurfacing script to see random ideas and find new connections:

```bash
./99_System/Scripts/resurface.py
```

## 🛠 Templates & Tools

Located in `99_System/`:

*   **Templates**:
    *   `Source_Ingestion.md`: For deeply reading a paper.
    *   `Atomic_Node.md`: For storing a permanent concept.
    *   `Procedure.md`: For codifying a habit or workflow.
*   **Scripts**:
    *   `resurface.py`: Randomly picks 3 notes for review.

## 🧠 Philosophy

*   **Reconstruction > Storage**: If you can't reconstruct it, you didn't learn it.
*   **Procedures > Facts**: Knowing *how* to think is better than knowing *what* to think.
*   **Living Edges**: Always leave a "Live Edge" (a question or confusion) to hook future insights.
