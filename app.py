# app.py
from utils import add_entry, read_entries, delete_last_entry

add_entry("A iteration")

delete_last_entry()
add_entry("B: replaced deleted entry")

for line in read_entries():
    print(line)
    
    
    
 