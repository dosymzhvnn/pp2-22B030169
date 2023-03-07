import string
import os


file_names = [c + ".txt" for c in string.ascii_uppercase]

for file_name in file_names:
    with open(file_name, "w") as f:
        f.write("This is the file " + file_name)