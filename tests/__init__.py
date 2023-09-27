
import sys
import pathlib 

# Temporarily add test dir to PATH
CURRENT_DIR = pathlib.Path(__file__).parent
sys.path.append(CURRENT_DIR.__str__())
