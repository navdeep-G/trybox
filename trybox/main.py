import sys
import os
from sandbox import run_snippet
from utils import save_snippet, list_snippets, load_snippet

SNIPPET_DIR = os.path.join(os.path.dirname(__file__), "../snippets")
os.makedirs(SNIPPET_DIR, exist_ok=True)

def new_snippet():
    tag = input("Enter tag/description: ").strip()
    if not tag:
        print("❌ Tag is required.")
        return

    print("📝 Opening your editor to write the snippet...")
    code = get_user_code_via_editor()

    if not code.strip():
        print("⚠️ No code entered. Snippet not saved.")
        return

    filename = save_snippet(code, tag, SNIPPET_DIR)
    print(f"✅ Snippet saved to {filename}")

    print("\n🚀 Running your snippet...\n")
    run_snippet(code)

def run_existing():
    snippets = list_snippets(SNIPPET_DIR)
    for i, (fname, tag) in enumerate(snippets):
        print(f"[{i}] {tag} ({fname})")
    choice = int(input("Select snippet to run: "))
    filename, _ = snippets[choice]
    code = load_snippet(filename)
    run_snippet(code)

import os
import tempfile
import subprocess

def get_user_code_via_editor() -> str:
    editor = os.environ.get("EDITOR", "vi")
    with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as tmp:
        tmp_path = tmp.name

    subprocess.call([editor, tmp_path])

    with open(tmp_path, "r") as f:
        code = f.read()

    os.remove(tmp_path)
    return code

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
