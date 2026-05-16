import os

filename = "check.txt"

if os.path.exists(filename):
    with open(filename, "r") as f:
        print("File exists. Content:\n", f.read())
else:
    with open(filename, "w") as f:
        f.write("This file was just created.")
    print("File created and text written.")
