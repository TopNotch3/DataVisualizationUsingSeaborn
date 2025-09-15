import os
import subprocess

SCRIPTS_DIR = os.path.join(os.path.dirname(__file__), "scripts")

scripts = [
    'data_load_and_clean.py',
    'top_emitters.py',
    'trends_top10.py',
    'distribution_and_boxplots.py',
    'missing_heatmap.py',
    'correlation.py',
    'rolling_and_change.py',
    'pca_kmeans.py'
]

for script in scripts:
    script_path = os.path.join(SCRIPTS_DIR, script)
    print(f"\nRunning {script} ...")
    try:
        subprocess.run(["python", script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error while running {script}: {e}")
    
print('All scripts finished. Check outputs/figures and data/ (cleaned CSV).')