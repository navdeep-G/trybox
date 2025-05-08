import os
import sys
import tempfile
import subprocess
from trybox.sandbox import run_snippet
from trybox.utils import save_snippet, list_snippets, load_snippet
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

SNIPPET_DIR = os.path.join(os.path.dirname(__file__), "../snippets")
os.makedirs(SNIPPET_DIR, exist_ok=True)

def get_user_code_via_editor() -> str:
    editor = os.environ.get("EDITOR", "vi")
    with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as tmp:
        tmp_path = tmp.name
    subprocess.call([editor, tmp_path])
    with open(tmp_path, "r") as f:
        code = f.read()
    os.remove(tmp_path)
    return code

def new_snippet():
    tag = input("Enter tag/description: ").strip()
    if not tag:
        print("[red]❌ Tag is required.[/red]")
        return

    print("📝 Opening your editor to write the snippet...")
    code = get_user_code_via_editor()

    if not code.strip():
        print("[yellow]⚠️ No code entered. Snippet not saved.[/yellow]")
        return

    filename = save_snippet(code, tag, SNIPPET_DIR)
    print(f"[green]✅ Snippet saved to [bold]{filename}[/bold][/green]")
    print("\n🚀 Running your snippet...\n")
    run_snippet(code)

def run_existing():
    snippets = list_snippets(SNIPPET_DIR)
    if not snippets:
        print("[yellow]📭 No saved snippets found.[/yellow]")
        return

    print("\n[bold]📋 Saved Snippets:[/bold]")
    for i, (fname, tag) in enumerate(snippets):
        with open(fname, "r") as f:
            first_line = f.readline().strip()
        print(f"[{i}] {os.path.basename(fname)} — {first_line or '(empty)'}")
    print("[b]Enter the number to run, or 'x' to exit.[/b]")

    choice = input("Select snippet to run: ").strip()
    if choice.lower() == 'x':
        print("[cyan]↩️ Back to main menu.[/cyan]")
        return

    try:
        index = int(choice)
        filename, _ = snippets[index]
        code = load_snippet(filename)
        console.print(Panel(code, title="🧾 Snippet Preview", subtitle=filename))
        run_snippet(code)
    except (ValueError, IndexError):
        print("[red]❌ Invalid selection.[/red]")

def main():
    console.print(Panel.fit("[bold cyan]🧪 TryBox[/bold cyan]\nWelcome to your Python snippet lab! 🎉", title="Welcome"))

    while True:
        print("\n[1] ✍️  New Snippet")
        print("[2] ▶️  Run Existing")
        print("[3] ❌ Exit")
        choice = Prompt.ask("👉 Select an option", choices=["1", "2", "3"], default="1")

        if choice == "1":
            new_snippet()
        elif choice == "2":
            run_existing()
        elif choice == "3":
            print("[blue]👋 Exiting TryBox. Goodbye![/blue]")
            break

