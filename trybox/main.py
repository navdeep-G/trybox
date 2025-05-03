import sys
import os
from sandbox import run_snippet
from utils import save_snippet, list_snippets, load_snippet

SNIPPET_DIR = os.path.join(os.path.dirname(__file__), "../snippets")
os.makedirs(SNIPPET_DIR, exist_ok=True)

def new_snippet():
    tag = input("Enter tag/description: ")
    print("Enter your Python code. End with a blank line.")
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    code = "\n".join(lines)
    filename = save_snippet(code, tag, SNIPPET_DIR)
    print(f"Saved to {filename}")

def run_existing():
    snippets = list_snippets(SNIPPET_DIR)
    for i, (fname, tag) in enumerate(snippets):
        print(f"[{i}] {tag} ({fname})")
    choice = int(input("Select snippet to run: "))
    filename, _ = snippets[choice]
    code = load_snippet(filename)
    run_snippet(code)

def main():
    print("TryBox - Python Snippet Runner")
    print("[1] New Snippet")
    print("[2] Run Existing")
    choice = input("Select option: ")
    if choice == "1":
        new_snippet()
    elif choice == "2":
        run_existing()
    else:
        print("Invalid choice")

if __name__ == '__main__':
    main()
