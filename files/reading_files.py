
file_path = "C:/Users/Uporabnik/Documents/Python_Intro/files/output.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read this file")


import json

file_path = "C:/Users/Uporabnik/Documents/Python_Intro/files/output.json"

try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read this file")

import csv

file_path = "C:/Users/Uporabnik/Documents/Python_Intro/files/output.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)
        
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read this file")