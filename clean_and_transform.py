import subprocess
import os

def run_vbscript(script_name):
    script_path = os.path.abspath(f"vb_scripts/{script_name}")
    result = subprocess.run(["cscript", script_path], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"Error in {script_name}: {result.stderr}")
    else:
        print(f"{script_name} executed successfully.")

if __name__ == "__main__":
    print("Running cleaning script...")
    run_vbscript("clean.vbs")
    
    # Run transformation script
    print("Running transformation script...")
    run_vbscript("transform.vbs")
