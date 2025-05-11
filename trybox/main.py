import os
import sys
import tempfile
import subprocess
import time
from datetime import datetime
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.markdown import Markdown
from rich.traceback import install

install(show_locals=True)

console = Console()

SNIPPET_DIR = os.path.join(os.path.dirname(__file__), "../snippets")
LAST_SNIPPET_FILE = os.path.join(SNIPPET_DIR, ".last_snippet")
os.makedirs(SNIPPET_DIR, exist_ok=True)

def run_snippet(code: str):
    exec(code, {})

def get_user_code_via_editor() -> str:
    editor = os.environ.get("EDITOR", "vi")
    with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as tmp:
        tmp_path = tmp.name
    subprocess.call(["sh", "-c", f"{editor} '{tmp_path}'"])
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
    console.print(f"[green]📤 Exported to {md_filename}[/green]")

def save_last_snippet_path(path: str):
    with open(LAST_SNIPPET_FILE, "w") as f:
        f.write(os.path.abspath(path))

def load_last_snippet_path() -> str:
    if os.path.exists(LAST_SNIPPET_FILE):
        with open(LAST_SNIPPET_FILE, "r") as f:
            return f.read().strip()
    return ""

def suggest_tags(existing_tags):
    if not existing_tags:
        return ""
    console.print("\n[cyan]💡 Existing tags:[/cyan]", ", ".join(existing_tags))

def time_and_run(code):
    try:
        start = time.perf_counter()
        run_snippet(code)
        duration = time.perf_counter() - start
        console.print(f"[green]✅ Snippet completed in {duration:.2f} seconds.[/green]")
    except Exception:
        console.print("[bold red]❌ An error occurred while running the snippet:[/bold red]")
        raise

def new_snippet():
    from trybox.utils import save_snippet, list_snippets
    snippets = list_snippets(SNIPPET_DIR)
    existing_tags = list(set(tag for _, tag in snippets))
    suggest_tags(existing_tags)

    tag = input("[cyan]Enter tag/description (or 'b' to go back): [/cyan]").strip()
    if tag.lower() == 'b':
        console.print("[cyan]↩️ Back to main menu.[/cyan]")
        return
    if not tag:
        console.print("[red]❌ Tag is required.[/red]")
        return

    console.print("[blue]📝 Opening your editor to write the snippet...[/blue]")
    code = get_user_code_via_editor()

    if not code.strip():
        console.print("[yellow]⚠️ No code entered. Snippet not saved.[/yellow]")
        return

    filename = save_snippet(code, tag, SNIPPET_DIR)
    save_last_snippet_path(os.path.abspath(filename))
    console.print(f"[green]✅ Snippet saved to [bold]{filename}[/bold][/green]")
    console.rule("Running Snippet")
    time_and_run(code)
    console.rule("End of Output")

def run_existing():
    from trybox.utils import list_snippets, load_snippet
    snippets = list_snippets(SNIPPET_DIR)
    if not snippets:
        console.print("[yellow]📭 No saved snippets found.[/yellow]")
        return

    search_term = input("[cyan]🔍 Enter search term (or 'b' to go back): [/cyan]").strip().lower()
    if search_term == 'b':
        console.print("[cyan]↩️ Back to main menu.[/cyan]")
        return

    console.print("\n[bold magenta]📋 Saved Snippets:[/bold magenta]")
    indexed = []
    for i, (fname, tag) in enumerate(snippets):
        with open(fname, "r") as f:
            first_line = f.readline().strip()
        timestamp = datetime.fromtimestamp(os.path.getctime(fname)).strftime("%b %d, %Y %H:%M")
        entry = f"[{i}] {os.path.basename(fname)} — {first_line or '(empty)'} (saved on {timestamp})"
        if not search_term or search_term in entry.lower():
            console.print(entry)
            indexed.append((i, fname))

    console.print("[cyan]Enter the number to run, or 'b' to go back.[/cyan]")
    choice = input("[cyan]Select snippet to run or export: [/cyan]").strip()
    if choice.lower() == 'b':
        console.print("[cyan]↩️ Back to main menu.[/cyan]")
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
        console.rule("Running Snippet")
        time_and_run(code)
        console.rule("End of Output")
    except (ValueError, IndexError):
        console.print("[red]❌ Invalid selection.[/red]")

def run_last_snippet():
    from trybox.utils import load_snippet
    path = load_last_snippet_path()
    if not path or not os.path.exists(path):
        console.print("[yellow]⚠️ No last snippet found.[/yellow]")
        return
    code = load_snippet(path)
    console.print(Panel(code, title="🧾 Last Snippet", subtitle=path))
    console.rule("Running Snippet")
    time_and_run(code)
    console.rule("End of Output")

def show_recent_snippets(n=5):
    console.print("\n[bold]🕘 Recent Snippets:[/bold]")
    snippets = sorted(os.listdir(SNIPPET_DIR), key=lambda f: os.path.getctime(os.path.join(SNIPPET_DIR, f)), reverse=True)
    count = 0
    for fname in snippets:
        if fname.startswith(".") or not fname.endswith(".py"):
            continue
        path = os.path.join(SNIPPET_DIR, fname)
        timestamp = datetime.fromtimestamp(os.path.getctime(path)).strftime("%b %d, %Y %H:%M")
        console.print(f"• {fname} (saved on {timestamp})")
        count += 1
        if count >= n:
            break

def search_by_tag():
    from trybox.utils import list_snippets, load_snippet
    snippets = list_snippets(SNIPPET_DIR)
    if not snippets:
        console.print("[yellow]📭 No saved snippets found.[/yellow]")
        return

    tag_term = input("[cyan]🔎 Enter tag to search: [/cyan]").strip().lower()
    console.print("[bold magenta]📋 Matching Snippets:[/bold magenta]")
    found = False
    for i, (fname, tag) in enumerate(snippets):
        if tag_term in tag.lower():
            timestamp = datetime.fromtimestamp(os.path.getctime(fname)).strftime("%b %d, %Y %H:%M")
            console.print(f"[{i}] {os.path.basename(fname)} — [italic cyan]{tag}[/italic cyan] (saved on {timestamp})")
            found = True
    if not found:
        console.print("[dim]No matching snippets found.[/dim]")

def main():
    console.print(Panel.fit("[bold cyan]🧪 TryBox[/bold cyan]\nWelcome to your Python snippet lab! 🎉", title="Welcome"))
    show_recent_snippets()

    while True:
        console.print("[1] ✍️  New Snippet")
        console.print("[2] ▶️  Run Existing")
        console.print("[3] ♻️  Run Last Snippet")
        console.print("[4] 🔎 Search by Tag")
        console.print("[5] ❌ Exit")
        choice = Prompt.ask("👉 Select an option", choices=["1", "2", "3", "4", "5"], default="1")

        if choice == "1":
            new_snippet()
        elif choice == "2":
            run_existing()
        elif choice == "3":
            run_last_snippet()
        elif choice == "5":
            search_by_tag()
        elif choice == "4":
            console.print("[blue]👋 Exiting TryBox. Goodbye![/blue]")
            break

if __name__ == "__main__":
    main()

