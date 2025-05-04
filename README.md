# 🧪 trybox

**trybox** is a local-first utility for Python developers to write, save, and safely execute code snippets in isolated subprocesses. It offers a clean interface to tag and timestamp experiments, making it easy to organize, revisit, and rerun them at any time. Built entirely on the Python standard library, trybox runs fully offline, without telemetry or cloud dependencies, and is ideal for quick prototyping, testing ideas, or maintaining a persistent scratchpad.

## ✨ Features

- 📝 Save Python snippets with descriptions and timestamps  
- 🧱 Run snippets in isolated subprocess environments  
- 📂 Browse and rerun previous experiments easily  
- 🔒 Fully offline — no telemetry or cloud sync  
- 🐍 Built with the Python standard library only  

## ❓ Why trybox?

While traditional IDEs like PyCharm or quick ad hoc scripts like `test.py` are common for experimenting with Python, they both come with limitations.

**trybox** is designed for developers who want a fast, organized, and terminal-based way to write, save, and run short Python experiments — without managing files manually or switching out of the terminal.

## 🆚 Why not just use PyCharm?

Even if you already use PyCharm or another IDE, trybox still fills an important gap:

- **🚧 Isolation** – You can prototype without touching your project structure  
- **⚡ Speed** – No need to open a GUI or manage files — launch from the terminal instantly  
- **📁 Clean Workspace** – Keeps scratch code out of your repo  
- **🧠 Snippet History** – Snippets are saved, timestamped, and searchable — unlike PyCharm scratch files  
- **🖥 Headless Support** – Perfect for remote servers, SSH, or containers where GUI tools aren’t available  
- **💥 Safety** – Snippets run in isolated subprocesses, with support for timeouts and future sandboxing

**TryBox complements IDEs** — it’s not a replacement. Use your IDE for structured dev work, and use trybox when you just want to experiment.

## 🆚 Why not just use a script like `python test.py`?

Yes, you *can* just write `scratch.py` or `test.py` and run it. But TryBox exists to solve the common pain points of doing that repeatedly:

| Problem                         | What Developers Typically Do                 | How TryBox Solves It                                   |
|----------------------------------|-----------------------------------------------|--------------------------------------------------------|
| 💥 Workspace clutter             | Create lots of throwaway files: `test1.py`, `scratch.py` | Automatically tags and organizes saved snippets        |
| 🧠 Forgetting useful code        | Lose valuable experiments or overwrite them    | Keeps everything archived, timestamped, and reusable   |
| 🗂️ Poor snippet management       | Manually manage files or use vague names       | Built-in history, tagging, and snippet preview         |
| 🧪 Lack of isolation             | Runs all code in the same environment          | Executes snippets in a subprocess for safety           |
| 🐍 Reuse is tedious              | Copy/paste or retype code when needed again    | Rerun old snippets from the list in one command        |
| ⚡ Slower workflow               | Create, save, run — all manually               | Write, save, and run directly from the terminal/editor |

TryBox is like a personal Python scratchpad — but with memory, structure, and zero setup.

**trybox is ideal for:**

- ⚡ Rapid prototyping or testing one-off ideas  
- 🧪 Running isolated code safely without polluting your workspace  
- 🧠 Keeping a searchable archive of past experiments  
- 🖥 Working in minimal or remote environments without a GUI  
- 🧰 Building a habit of local, organized experimentation  

It's a personal Python scratchpad — clean, efficient, and always ready in your terminal.

## 📦 Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/youruser/trybox.git
   cd trybox
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python -m trybox.main

## 🧪 Example

1. Open a terminal and activate your virtual environment, if using one:
    ```
    source venv/bin/activate
    ```

2. Run the main interface:
    ```
    python -m trybox.main
    ```

3. Choose option `[1]` to create a new snippet  
   You'll be prompted to enter a description and write your code in your editor.

4. Example input:
    ```
    Enter tag/description: greet user
    ```

    In your editor, write the following code and save:

    ```python
    name = input("What is your name? ")
    print(f"Hello, {name}! Welcome to TryBox.")
    ```

5. After saving, your snippet will be stored.  
   If auto-run is enabled, you’ll immediately see something like:

    ```
    What is your name? Alice
    Hello, Alice! Welcome to TryBox.
    ```

6. Or, choose option `[2]` from the main menu to run it manually later.

## ⚖️ License

📜 This project is licensed under the Apache License, Version 2.0.
