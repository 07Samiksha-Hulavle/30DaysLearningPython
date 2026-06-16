#create tuple:
fruits = ("Apple","Banana","Mango")
print(fruits)

#indexing:
print(fruits[0])
print(fruits[-1])

#slicing:
nums = (10,20,30,40,50)
print(nums[1:4])

#looping:
colors = ("Red","Blue","Green")
for c in colors:
    print(c)

#tuple(length):
print(len(colors))    

#concatenation:
a = (1,2)
b = (3,4)
print(a + b)

#packing and unpacking:
data = ("Laptop",45000,"Black")
Product,Price,Color = data
print(f"Product : {Product}, Price : {Price} and Color : {Color}")
print(Product,Price,Color)

#Nested tuples inside list:
employees = [("E101","Samiksha","pune"),("E102","Anu","Mumbai")]
for eid,name,city in employees:
    print(eid, name, city)