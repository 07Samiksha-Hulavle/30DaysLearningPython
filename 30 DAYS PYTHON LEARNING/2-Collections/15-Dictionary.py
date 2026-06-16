#dictionary:

students = {"Name": "Samiksha","Age": 21,"City": "Pune"}
print(students)

#accessing values:
students = {"Name": "Samiksha","Age": 21,"City": "Pune"}
print(students["Name"])
print(students["City"])

#adding and updating:
students = {"Name": "Samiksha","Age": 21,"City": "Pune"}
students["Marks"] = 85
students["City"] = "Mumbai"
print(students)

#removing:
students = {"Name": "Samiksha","Age": 21,"City": "Pune"}
students.pop("Age")
print(students)

#dictionary methods:
students = {"Name": "Samiksha","Age": 21,"City": "Pune"}
print(students.keys())
print(students.values())
print(students.items())
print(students.get("Name"))

#looping:
students = {"Name": "Samiksha","Age": 21,"City": "Pune"}
for k in students:
    print(k,students[k])


 #nested dictionary:
employees = {
     "E101" : {"Name" : "Rohit","City" : "Pune"},
     "E102" : {"Name" : "Samiksha","City" : "Mumbai"}
}
print(employees["E102"]["Name"])

#mapping wrong --> Correct
mapper ={
    "mombai" : "Mumbai",
    "kolkatta" : "Kolkata"
}
print(mapper["mombai"])
print(mapper["kolkatta"])