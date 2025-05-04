# 🧪 trybox

**trybox** is a local-first utility for Python developers to write, save, and safely execute code snippets in isolated subprocesses. It offers a clean interface to tag and timestamp experiments, making it easy to organize, revisit, and rerun them at any time. Built entirely on the Python standard library, trybox runs fully offline, without telemetry or cloud dependencies, and is ideal for quick prototyping, testing ideas, or maintaining a persistent scratchpad.

## ✨ Features

- 📝 Save Python snippets with descriptions and timestamps  
- 🧱 Run snippets in isolated subprocess environments  
- 📂 Browse and rerun previous experiments easily  
- 🔒 Fully offline — no telemetry or cloud sync  
- 🐍 Built with the Python standard library only  

## ❓ Why trybox?

While traditional IDEs like PyCharm or VS Code are powerful, they can feel heavy for quick tasks. **trybox** is designed for developers who want a fast, terminal-based way to write, save, and run short Python experiments without switching context or managing scratch files.

**trybox is ideal for:**

- ⚡ Rapid prototyping or testing one-off ideas  
- 🧪 Running isolated code safely without polluting your workspace  
- 🧠 Keeping a searchable archive of past experiments  
- 🖥 Working in minimal or remote environments without a GUI  
- 🧰 Building a habit of local, organized experimentation  

It's a personal Python scratchpad — clean, efficient, and always ready in your terminal.

## 🆚 Why not just use PyCharm?

Even if you already use PyCharm or another IDE, trybox still fills an important gap:

- **🚧 Isolation** – You can prototype without touching your project structure  
- **⚡ Speed** – No need to open a GUI or manage files — launch from the terminal instantly  
- **📁 Clean Workspace** – Keeps scratch code out of your repo  
- **🧠 Snippet History** – Snippets are saved, timestamped, and searchable — unlike PyCharm scratch files  
- **🖥 Headless Support** – Perfect for remote servers, SSH, or containers where GUI tools aren’t available  
- **💥 Safety** – Snippets run in isolated subprocesses, with support for timeouts and future sandboxing

**TryBox complements IDEs** — it’s not a replacement. Use your IDE for structured dev work, and use trybox when you just want to experiment.

## ▶️ Usage

📄 Details on how to use trybox will be added here.

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
