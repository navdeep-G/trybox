import os
import sys
import tempfile
import subprocess
from datetime import datetime
from trybox.sandbox import run_snippet
from trybox.utils import save_snippet, list_snippets, load_snippet
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.markdown import Markdown

console = Console()

SNIPPET_DIR = os.path.join(os.path.dirname(__file__), "../snippets")
LAST_SNIPPET_FILE = os.path.join(SNIPPET_DIR, ".last_snippet")
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

def export_snippet_to_markdown(filename: str, code: str):
    base_name = os.path.basename(filename)
    md_filename = f"{base_name}.md"
    with open(md_filename, "w") as md_file:
        md_file.write(f"# Snippet: {base_name}\n\n")
        md_file.write(f"Saved on: {datetime.fromtimestamp(os.path.getctime(filename)).strftime('%b %d, %Y %H:%M')}\n\n")
        md_file.write("```python\n")
        md_file.write(code)
        md_file.write("\n```")
    print(f"[green]📤 Exported to {md_filename}[/green]")

def save_last_snippet_path(path: str):
    with open(LAST_SNIPPET_FILE, "w") as f:
        f.write(path)

def load_last_snippet_path() -> str:
    if os.path.exists(LAST_SNIPPET_FILE):
        with open(LAST_SNIPPET_FILE, "r") as f:
            return f.read().strip()
    return ""

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
    save_last_snippet_path(os.path.abspath(filename))
    print(f"[green]✅ Snippet saved to [bold]{filename}[/bold][/green]")
    print("\n🚀 Running your snippet...\n")
    run_snippet(code)

def run_existing():
    snippets = list_snippets(SNIPPET_DIR)
    if not snippets:
        print("[yellow]📭 No saved snippets found.[/yellow]")
        return

    search_term = input("🔍 Enter search term (press Enter to skip): ").strip().lower()

    print("\n[bold]📋 Saved Snippets:[/bold]")
    indexed = []
    for i, (fname, tag) in enumerate(snippets):
        with open(fname, "r") as f:
            first_line = f.readline().strip()
        timestamp = datetime.fromtimestamp(os.path.getctime(fname)).strftime("%b %d, %Y %H:%M")
        entry = f"[{i}] {os.path.basename(fname)} — {first_line or '(empty)'} (saved on {timestamp})"
        if not search_term or search_term in entry.lower():
            print(entry)
            indexed.append((i, fname))

    print("[b]Enter the number to run, or 'x' to exit.[/b]")
    choice = input("Select snippet to run or export: ").strip()
    if choice.lower() == 'x':
        print("[cyan]↩️ Back to main menu.[/cyan]")
        return

    try:
        index = int(choice)
        _, filename = indexed[index]
        code = load_snippet(filename)
        console.print(Panel(code, title="🧾 Snippet Preview", subtitle=filename))

        export = Prompt.ask("📤 Export to Markdown?", choices=["y", "n"], default="n")
        if export == "y":
            export_snippet_to_markdown(filename, code)

        save_last_snippet_path(os.path.abspath(filename))
        run_snippet(code)
    except (ValueError, IndexError):
        print("[red]❌ Invalid selection.[/red]")

def run_last_snippet():
    path = load_last_snippet_path()
    if not path or not os.path.exists(path):
        print("[yellow]⚠️ No last snippet found.[/yellow]")
        return
    code = load_snippet(path)
    console.print(Panel(code, title="🧾 Last Snippet", subtitle=path))
    run_snippet(code)

def show_recent_snippets(n=5):
    print("\n[bold]🕘 Recent Snippets:[/bold]")
    snippets = sorted(os.listdir(SNIPPET_DIR), key=lambda f: os.path.getctime(os.path.join(SNIPPET_DIR, f)), reverse=True)
    count = 0
    for fname in snippets:
        if fname.startswith(".") or not fname.endswith(".py"):
            continue
        path = os.path.join(SNIPPET_DIR, fname)
        timestamp = datetime.fromtimestamp(os.path.getctime(path)).strftime("%b %d, %Y %H:%M")
        print(f"• {fname} (saved on {timestamp})")
        count += 1
        if count >= n:
            break

def main():
    console.print(Panel.fit("[bold cyan]🧪 TryBox[/bold cyan]\nWelcome to your Python snippet lab! 🎉", title="Welcome"))
    show_recent_snippets()

    while True:
        print("\n[1] ✍️  New Snippet")
        print("[2] ▶️  Run Existing")
        print("[3] ♻️  Run Last Snippet")
        print("[4] ❌ Exit")
        choice = Prompt.ask("👉 Select an option", choices=["1", "2", "3", "4"], default="1")

        if choice == "1":
            new_snippet()
        elif choice == "2":
            run_existing()
        elif choice == "3":
            run_last_snippet()
        elif choice == "4":
            print("[blue]👋 Exiting TryBox. Goodbye![/blue]")
            break

