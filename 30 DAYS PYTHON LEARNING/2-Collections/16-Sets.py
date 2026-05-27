#sets:

#create set:
fruits = {"Apple","Banana","Apple","Mango"}
print(fruits)

#add items :
fruits.add("Orange")
print(fruits)

#remove items:
fruits.discard("Banana")
print(fruits)

#set operators:
a = {1,2,3}
b = {3,4,5}

print("Union: ",a | b)
print("Intersection: ",a & b)
print("Difference: ",a-b) #output({1,2})
print("Difference: ",b-a) #output({4,5)
print("Symmetric Difference: ",a ^ b)

#remove duplicates:
cities = ["Pune","Mumbai","Delhi","Mumbai"]
unique = set(cities)
print("Unique Cities: ",unique)

#missing values:
list1 = {"SQL","Excel","Power BI"}
list2 = {"SQL","Power BI"}
missing = list1 - list2
print("Missing: ",missing)

#common skills:
deptA =  {"SQL","Excel","Python"}
deptB = {"Excel","Python","Power BI"}
print("Common Skills : ",deptA & deptB)
