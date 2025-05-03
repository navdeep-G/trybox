# 🧪 trybox

**trybox** is a local-first utility for Python developers to write, save, and safely execute code snippets in isolated subprocesses. It offers a clean interface to tag and timestamp experiments, making it easy to organize, revisit, and rerun them at any time. Built entirely on the Python standard library, trybox runs fully offline, without telemetry or cloud dependencies, and is ideal for quick prototyping, testing ideas, or maintaining a persistent scratchpad.

## ✨ Features

- 📝 Save Python snippets with descriptions and timestamps  
- 🧱 Run snippets in isolated subprocess environments  
- 📂 Browse and rerun previous experiments easily  
- 🔒 Fully offline — no telemetry or cloud sync  
- 🐍 Built with the Python standard library only  

## 📦 Installation

📄 Instructions for installing trybox will be added here.

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
