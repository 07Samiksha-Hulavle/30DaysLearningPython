#Range & Loops:

#Print 1 to 5:
for i in range(1,6):
    print(i)


#Print Even No. (0-18):
for i in range(0,20,2):
    print(i)


#Print Countdown From 10 to 0:
for i in range(10,0,-1):
    print(i)


#Print Loop through List using Index:
items = ["Book","Pen","Laptop"]
for i in range(len(items)):
    print(i,items[i])


#Generate Employee IDs:
for i in range(1,6):
    print('Emp-',i)


#Create Years List:
years = []
for y in range(2006,2026):
    years.append(y)
print(years)


#Clean City Names Using Range:
cities = ["MuMBAI","PUne","delhI"]
for i in range(len(cities)):
    cities[i] = cities[i].strip().title()
print(cities)   


#Extract Last 4 Digits:
ids =["EMP-110022","EMP-330044","EMP-990011"]
for i in range(len(ids)):
    print(ids[i][-4:])


#Range in Range:
for i in range (1,4):
    for j in range(1,4):
        print(f"i value : {i}, j value : {j}")
