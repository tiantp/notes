#!/usr/bin/env python3
import os
from pathlib import Path

# Configuration
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
ATOMIC_DIR = REPO_ROOT / "02_Atomic"

def get_existing_notes():
    """Scans the 02_Atomic directory and returns a structured list of existing notes."""
    categories = ["Concepts", "Principles", "Models", "Evidence"]
    output = []
    
    for category in categories:
        dir_path = ATOMIC_DIR / category
        if dir_path.exists():
            files = [f for f in os.listdir(dir_path) if f.endswith(".md")]
            if files:
                output.append(f"### {category}")
                for f in sorted(files):
                    # We could read the file to get the 'Claim' or just use the filename
                    # Using filename for speed and compactness
                    name = f.replace(".md", "")
                    output.append(f"- {name}")
    
    return "\n".join(output)

def main():
    print("--- START OF EXISTING NOTES CONTEXT ---")
    print(get_existing_notes())
    print("--- END OF EXISTING NOTES CONTEXT ---")
    print("\n✅ Copy the above block and paste it into the 'Context' section of the Atomization Prompt.")

if __name__ == "__main__":
    main()
