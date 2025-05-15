import os
import json
from pathlib import Path

filepath = Path(__file__).resolve().parent.parent / 'Data' / 'records.json'

#print(filepath)
#print(.//records.json")

with open(filepath,"w") as f:
    f.write("hello")