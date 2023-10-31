import os

# Get the current working directory
cwd = os.getcwd()

# Save the current working directory to a txt file
with open("working_directory.txt", "w") as f:
    f.write(cwd)
