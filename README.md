# Exoskeleton for the Mind

> A system to wrap around your cognition—helping you remember, reason, and make better decisions.

This repository is structured as a **Cognitive Exoskeleton** based on principles of Intelligence Amplification, distributed cognition, and active recall. It is not just a storage bin for notes; it is a machine for **processing** and **synthesizing** information.

## 📂 Structure

The directory structure mirrors the cognitive pipeline: `Ingest` → `Process` → `Store` → `Act`.

*   **`00_Map/`**: **The Global Shape**. Visual concept maps, dependency trees, and "Maps of Ignorance". Start here to orient yourself in a domain.
*   **`01_Inbox/`**: **Raw Signal**. Dump papers, PDFs, and brain-dumps here. They are temporary.
*   **`02_Atomic/`**: **The Knowledge Base**.
    *   `Concepts/`: Definitions and core objects (Nouns).
    *   `Principles/`: Invariants and Rules (Claims/Verbs).
    *   `Models/`: Systems and relationships.
    *   `Evidence/`: Case studies and data points.
*   **`03_Procedures/`**: **Algorithms**. Runnable checklists and thinking tools (e.g., "Debugging Loop", "Decision Razor").
*   **`04_Memory/`**: **Flashcards**. Source files for Anki/Spaced-Repetition.
*   **`05_Projects/`**: **Output**. Active work utilizing the exoskeleton.
*   **`99_System/`**: **The Engine**. Templates, prompts, and scripts to maintain the exoskeleton.

## ⚙️ The Workflow

### 1. Ingestion (Turning Noise into Signal)
**Goal:** Extract structure from a source (PDF/Article) without checking duplication yet.
*   **Manual**: Use `99_System/Templates/Source_Ingestion.md`.
*   **Automated (Recommended)**:
    1.  Copy the system prompt from `99_System/Prompts/Ingest_Material.md`.
    2.  Paste it into an LLM (Claude/Gemini/GPT) along with the text of your source.
    3.  Save the LLM's output as a new markdown file in `01_Inbox/`.

### 2. Atomization (Process & Integrate)
**Goal:** Break the processed ingestion note into permanent atomic notes, while checking for duplicates.
1.  **Get Context**: Run the helper script to get a list of what you already know.
    ```bash
    ./99_System/Scripts/list_nodes.py
    ```
2.  **Prepare Prompt**:
    *   Open `99_System/Prompts/Atomize_Source.md`.
    *   Paste the output of `list_nodes.py` into the **Context** section of the prompt.
    *   Paste your Ingestion Note (from Step 1) into the **Input** section.
3.  **Generate**: Feed this full prompt to your LLM.
4.  **Action**:
    *   **New Ideas**: Create new files in `02_Atomic/`.
    *   **Existing Ideas**: Follow the LLM's instructions to update existing files with new nuances/evidence.

### 3. Resurfacing (The "Alive" Component)
**Goal:** Force active recall and recombination of ideas.
Run the resurfacing script to see random ideas and find new connections:
```bash
./99_System/Scripts/resurface.py
```

## 🛠 Templates & Tools

Located in `99_System/`:

*   **Templates** (`/Templates`):
    *   `Source_Ingestion.md`: Structure for processing a source.
    *   `Atomic_Node.md`: Structure for a permanent concept.
    *   `Procedure.md`: Structure for a thinking algorithm.
*   **Prompts** (`/Prompts`):
    *   `Ingest_Material.md`: System prompt for LLM ingestion.
    *   `Atomize_Source.md`: System prompt for converting ingestion notes into atomic nodes (duplicates-aware).
*   **Scripts** (`/Scripts`):
    *   `list_nodes.py`: Generates the "Context" list of existing notes for the Atomizer.
    *   `resurface.py`: Randomly picks 3 notes for review.

## 🧠 Philosophy

*   **Reconstruction > Storage**: If you can't reconstruct it, you didn't learn it.
*   **Procedures > Facts**: Knowing *how* to think is better than knowing *what* to think.
*   **Living Edges**: Always leave a "Live Edge" (a question or confusion) to hook future insights.
