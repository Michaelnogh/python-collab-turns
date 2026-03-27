# app.py
from utils import add_entry, read_entries

add_entry("A: refining update")

for line in read_entries():
    print(line)