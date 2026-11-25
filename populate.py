import os
import sys

CODE_FOLDER_PATH = "./Code"
PARTICIPANT_NAMES = ["Connor", "Steven", "Max"]
DAYS = 31

## Get confirmation first
print("WARNING, THIS WILL CLEAR ALL PREVIOUSLY WRITTEN CODE. DO YOU WANT TO CONTINUE?")
confirmation = input("Type 'y' to confirm: ")
if confirmation != 'y':
    sys.exit(1)

## Clear Code folder first
for root, dirs, files in os.walk(CODE_FOLDER_PATH, topdown=False):
    for file in files:
        os.remove(os.path.join(root, file))
    for dir_name in dirs:
        os.rmdir(os.path.join(root, dir_name))

## Create and provision folders
for i in range(1, DAYS+1, 1):
    os.makedirs(CODE_FOLDER_PATH + "/Day " + str(i), exist_ok=True)
    for person in PARTICIPANT_NAMES:
        os.makedirs(CODE_FOLDER_PATH + "/Day " + str(i) + "/" + person, exist_ok=True)
        os.makedirs(CODE_FOLDER_PATH + "/Day " + str(i) + "/_inputs", exist_ok=True)
        file_path = CODE_FOLDER_PATH + "/Day " + str(i) + "/" + person + "/"
        with open(file_path + "part1.py", "w", encoding="utf-8") as f:
            f.write("#inputs are at ../_inputs\n\nprint('Hello, world!')")
        with open(file_path + "part2.py", "w", encoding="utf-8") as f:
            f.write("#inputs are at ../_inputs\n\nprint('Hello, world!')")