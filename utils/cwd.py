"""
Changes the current working directory (CWD) to MAIN_DIR.
MAIN_DIR is the path to the directory of the script being executed (i.e., __main__).
This ensures that any relative file operations in the script will be based on the
directory containing the main script, rather than the directory from which the script
was called.

:raises OSError: If changing the working directory fails (e.g., the path does not exist).
"""
import os
import sys
from pathlib import Path

# Define the main directory path based on the script location and change the current working directory to MAIN_DIR
MAIN_DIR = Path(sys.argv[0]).resolve().parent
os.chdir(MAIN_DIR)
