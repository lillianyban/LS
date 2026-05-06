import subprocess

scripts = [
    "Scripts/clean_and_merge.py",
    "Scripts/summarize_data.py",
    "Scripts/analysis.py",
    "Scripts/visualize.py"
]

for script in scripts:
    print(f"\nRunning {script}...")
    subprocess.run(["python3", script], check=True)

print("\nFull workflow completed successfully.")