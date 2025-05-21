from pathlib import Path
from datetime import datetime
from typing import List, Tuple

def save_snippet(code: str, tag: str, directory: str) -> str:
    """
    Save a code snippet to a file with a timestamped filename.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_tag = "_".join(tag.strip().split())
    filename = f"{safe_tag}_{timestamp}.py"
    filepath = Path(directory) / filename
    filepath.write_text(code)
    return str(filepath)

def list_snippets(directory: str) -> List[Tuple[str, str]]:
    """
    List all snippet files in a directory, returning their paths and human-readable tags.
    """
    path = Path(directory)
    snippets = []
    for file in sorted(path.glob("*.py")):
        parts = file.stem.rsplit("_", 1)
        if len(parts) == 2 and parts[1].isdigit():
            tag = parts[0].replace("_", " ")
        else:
            tag = file.stem.replace("_", " ")
        snippets.append((str(file), tag))
    return snippets

def load_snippet(path: str) -> str:
    """
    Load the contents of a snippet file.
    """
    return Path(path).read_text()

