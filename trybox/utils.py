from pathlib import Path
from datetime import datetime
from typing import List, Tuple

def save_snippet(code: str, tag: str, directory: str) -> str:
    """
    Save a code snippet to a file with a timestamped filename.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_tag = tag.replace(' ', '_')
    filename = f"{safe_tag}_{timestamp}.py"
    filepath = Path(directory) / filename
    filepath.write_text(code)
    return str(filepath)

def list_snippets(directory: str) -> List[Tuple[str, str]]:
    """
    List all snippet files in a directory, returning their paths and human-readable tags.
    """
    path = Path(directory)
    result = []
    for file in sorted(path.glob("*.py")):
        # Remove timestamp to extract tag
        name_parts = file.stem.rsplit("_", 1)
        tag = name_parts[0].replace("_", " ") if len(name_parts) == 2 else file.stem
        result.append((str(file), tag))
    return result

def load_snippet(path: str) -> str:
    """
    Load the contents of a snippet file.
    """
    return Path(path).read_text()

