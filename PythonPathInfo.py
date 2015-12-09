import sys
import os


for p in sys.path:
   print(p)

print(os.environ['PYTHONPATH'].split(os.pathsep))