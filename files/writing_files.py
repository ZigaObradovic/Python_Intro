### .txt files
txt_data = "I like pizza"

file_path = "files/output.txt"
file_path2 = "C:/Users/Uporabnik/Desktop/output.txt" # če želimo določiti mesto

# drugi parameter je mode: "w" - write, "x" - tudi write, če output file ne obstaja, če pa obstaja, bomo nobili napako, "a" - append, "r" - read
with open(file=file_path, mode="w") as file:
    file.write(txt_data)
    print(f"txt file '{file_path}' was created")


# z "x":

try:
    with open(file=file_path, mode="x") as file:
        file.write(txt_data)
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("That file already exists")

# z "a" samo dodajamo na konec:
with open(file=file_path, mode="a") as file:
    file.write("\n" + txt_data)
    print("appedning succesfull")

employees = ["Žiga", "Mia", "Jan", "Kaja"]
file_path3 = "files/output2.txt"

with open(file=file_path3, mode="w") as file:
    for employee in employees:
        file.write(employee + "\n")
    print(f"txt file '{file_path3}' was created")


### .json files
import json

employee = {
    "name": "Mia",
    "age": 22,
    "studij": "FMF"
}
file_path = "files/output.json"

try:
    with open(file=file_path, mode="w") as file:
        json.dump(employee, file, indent=4)
        print(f"json file '{file_path}' was created")
except FileExistsError:
    print("That file already exists")


### .csv files
import csv

employees = [["Name", "Age", "Job"], ["Žiga", "Mia", "Pika"], ["Močen", "Lepa", "Pridna"]]
file_path = "files/output.csv"

try:
    with open(file=file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print("That file already exists")

