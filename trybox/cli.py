import os
from typing import Optional
import typer
from rich import print
from trybox.main import new_snippet, run_existing, run_last_snippet, show_recent_snippets
from trybox.utils import list_snippets, load_snippet

app = typer.Typer()

@app.callback()
def callback():
    """TryBox CLI - A tool for saving and running code snippets."""
    pass

@app.command()
def version():
    """Show TryBox version."""
    print("TryBox version 0.1.0")

@app.command(name="list")
def list_snippets_cmd():
    """List all saved snippets."""
    snippets = list_snippets(os.path.join(os.path.dirname(__file__), "../snippets"))
    if not snippets:
        print("📭 No snippets found.")
        return
    for i, (fname, tag) in enumerate(snippets):
        print(f"[{i}] {os.path.basename(fname)} — {tag}")

@app.command()
def new(tag: str):
    """Create a new snippet."""
    os.environ["TRYBOX_TAG"] = tag
    new_snippet()

@app.command()
def run(index: Optional[int] = typer.Option(None, help="Index of the snippet to run")):
    """Run an existing snippet by index."""
    if index is None:
        run_existing()
    else:
        snippets = list_snippets(os.path.join(os.path.dirname(__file__), "../snippets"))
        try:
            filename = snippets[index][0]  # Adjusted to access first element
            code = load_snippet(filename)
            print(f"Running snippet: {filename}")
            exec(code, {})
        except (IndexError, ValueError):
            print("❌ Invalid index provided.")

@app.command()
def last():
    """Run the last saved snippet."""
    run_last_snippet()

if __name__ == "__main__":
    app()
