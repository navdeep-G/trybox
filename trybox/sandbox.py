import subprocess
import tempfile
import os

def run_snippet(code: str):
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as tmp:
        tmp.write(code)
        tmp_filename = tmp.name
    print("\n--- Running ---")
    try:
        subprocess.run(["python", tmp_filename], timeout=5, check=True)
    except subprocess.CalledProcessError as e:
        print("Error:", e)
    except subprocess.TimeoutExpired:
        print("Execution timed out")
    finally:
        os.remove(tmp_filename)
