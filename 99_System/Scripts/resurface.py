#!/usr/bin/env python3
import os
import random
from pathlib import Path

# Configuration
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
ATOMIC_DIR = REPO_ROOT / "02_Atomic"

def get_markdown_files(directory):
    """Recursively find all .md files in the given directory."""
    md_files = []
    if not directory.exists():
        return md_files
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                md_files.append(os.path.join(root, file))
    return md_files

def format_preview(filepath):
    """Read specific lines to generate a preview (e.g., Title + Claim)."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        # Basic parsing: First line is title, look for "The Claim"
        title = lines[0].strip().replace("# ", "")
        claim = "No claim extracted."
        
        for i, line in enumerate(lines):
            if "The Claim" in line:
                # Grab the next non-empty line
                for next_line in lines[i+1:]:
                    if next_line.strip() and not next_line.strip().startswith("#"):
                        claim = next_line.strip().replace("> ", "")
                        break
                break
        
        return f"\n📄 **{title}**\n   path: ...{str(filepath)[-40:]}\n   💡 {claim}"
    except Exception as e:
        return f"Error reading {filepath}: {e}"

def main():
    print("🧠 **Mind Exoskeleton Resurfacer** 🧠\n")
    
    files = get_markdown_files(ATOMIC_DIR)
    
    if not files:
        print(f"No atomic notes found in {ATOMIC_DIR}. Start writing!")
        return

    # Pick 3 random files
    selection = random.sample(files, min(3, len(files)))
    
    print(f"Found {len(files)} atomic nodes. Here are 3 for your review:\n")
    
    for note in selection:
        print(format_preview(note))
        print("-" * 40)

    print("\n👉 **Prompt**: Can you connect any two of these? Does one contradict the other?")

if __name__ == "__main__":
    main()
