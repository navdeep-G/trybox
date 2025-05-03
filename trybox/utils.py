import os
from datetime import datetime

def save_snippet(code: str, tag: str, directory: str) -> str:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{tag.replace(' ', '_')}_{timestamp}.py"
    filepath = os.path.join(directory, filename)
    with open(filepath, "w") as f:
        f.write(code)
    return filepath

def list_snippets(directory: str):
    files = sorted(os.listdir(directory))
    result = []
    for fname in files:
        tag = fname.rsplit("_", 1)[0].replace("_", " ")
        result.append((os.path.join(directory, fname), tag))
    return result

def load_snippet(path: str) -> str:
    with open(path, "r") as f:
        return f.read()
