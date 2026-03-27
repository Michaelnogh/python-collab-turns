# app.py
from utils import add_entry, read_entries

add_entry("A: second change")

for line in read_entries():
    print(line)