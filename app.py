# app.py
from utils import add_entry, read_entries

add_entry("A: refining update")

for line in read_entries():
    print(line)
    
    
    
def delete_last_entry():
    with open("data.txt", "r") as f:
        lines = f.readlines()
    with open("data.txt", "w") as f:
        f.writelines(lines[:-1])    