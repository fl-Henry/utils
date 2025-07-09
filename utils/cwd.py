import os
import sys
from pathlib import Path

MAIN_DIR = Path(sys.argv[0]).resolve().parent
os.chdir(MAIN_DIR)
