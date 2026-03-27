# app.py
from utils import add_entry, read_entries

add_entry("B: first change")

for line in read_entries():
    print(line)