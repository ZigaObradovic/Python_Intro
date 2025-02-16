import os

file_path = "files/test.txt"
file_path2 = "C:/Users/Uporabnik/Documents/Python_Intro/files/test.txt" ### v Raziskovalcu right-click na datoteko in klikneš lastnosti ( zamenjaj \ v /!)
folder_path = "C:/Users/Uporabnik/Documents/Python_Intro/files"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(folder_path):
        print("That is a directory")
else:
    print("That location doesn't exist")