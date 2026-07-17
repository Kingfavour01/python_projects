import csv
import json



txt_data = " i love you"
employees = ["mr", "mrs"]
employee2 = { "name" : "spongebob",
              "age" : 30,
              "job": "cook"
}

workstation_inventory = [
    ["WS-01", "Core i5", "8GB", "Windows 10"],
    ["WS-02", "Core i7", "16GB", "Ubuntu Linux"],
    ["WS-03", "M2 Chip", "16GB", "macOS"],
    ["WS-04", "Core i9", "64GB", "Windows 11"]
]


file_path = "C:/Users/HomePC/Desktop/output.txt"
try:
    with open(file = file_path, mode ="w") as file:
        for employee in employees:
         file.write("\n" + employee)
        print(f"text file {file_path} was created")

except FileExistsError:
    print("this file already exists! ")

file_path = "C:/Users/HomePC/Desktop/output1.txt"
try:
    with open(file=file_path, mode="w") as file:
            json.dump(employee2, file,indent=4)
            print(f"json {file_path} was created")
except FileExistsError:
    print("this file already exists! ")
file_path = "C:/Users/HomePC/Desktop/output2.txt"
try:
    with open(file=file_path, mode="w", newline="") as file:
           writer = csv.writer(file)
           for row in workstation_inventory:
               writer.writerow(row)
           print(f"csv {file_path} was created")
except FileExistsError:
    print("this file already exists! ")