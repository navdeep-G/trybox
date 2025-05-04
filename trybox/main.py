import sys
import os
from trybox.sandbox import run_snippet
from trybox.utils import save_snippet, list_snippets, load_snippet

SNIPPET_DIR = os.path.join(os.path.dirname(__file__), "../snippets")
os.makedirs(SNIPPET_DIR, exist_ok=True)

from rich import print
from rich.panel import Panel
from rich.prompt import Prompt
from rich.console import Console

console = Console()

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
    console.print(f"[green]✅ Snippet saved to [bold]{filename}[/bold][/green]")

    print("\n🚀 Running your snippet...\n")
    run_snippet(code)

from rich.panel import Panel
from rich.console import Console

console = Console()

def run_existing():
    snippets = list_snippets(SNIPPET_DIR)
    if not snippets:
        console.print("[yellow]📭 No saved snippets found.[/yellow]")
        return

    for i, (fname, tag) in enumerate(snippets):
        print(f"[{i}] {tag} ({fname})")

    try:
        choice = int(input("Select snippet to run: "))
        filename, _ = snippets[choice]
        code = load_snippet(filename)

        # 👇 Add this line here to preview the snippet before running
        console.print(Panel(code, title="🧾 Snippet Preview", subtitle=filename))

        run_snippet(code)
    except (IndexError, ValueError):
        console.print("[red]❌ Invalid selection.[/red]")

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
    console.print(Panel.fit("[bold cyan]🧪 TryBox[/bold cyan]\nLocal Python Snippet Runner", title="Welcome"))

    print("[1] ✍️  New Snippet")
    print("[2] ▶️  Run Existing")
    print("[3] ❌ Exit")

    choice = Prompt.ask("👉 Select an option", choices=["1", "2", "3"], default="1")

    if choice == "1":
        new_snippet()
    elif choice == "2":
        run_existing()
    else:
        print("Invalid choice")

if __name__ == '__main__':
    main()
