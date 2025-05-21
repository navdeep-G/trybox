import subprocess
import tempfile
import os

def run_snippet(code: str):
    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as tmp:
        tmp.write(code)
        tmp_path = tmp.name

    print("\n--- Running ---")
    try:
        subprocess.run(["python", tmp_path], timeout=5, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    except subprocess.TimeoutExpired:
        print("Execution timed out")
    finally:
        try:
            os.remove(tmp_path)
        except OSError as e:
            print(f"Failed to delete temporary file: {e}")

