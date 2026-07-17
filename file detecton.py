import os

file_path = "C:/Users/HomePC/Desktop"

if os.path.exists(file_path):
    print(f"The location '{file_path} exists ")

    if os.path.isfile(file_path):
        print("this is a file")
    elif os.path.isdir(file_path):
        print("this is a directory")

else:
    print("location does not exist")