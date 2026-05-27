# list:
fruits = ["Apple","Banana","Mango"]
print(fruits)

# indexing:
fruits = ["Apple","Banana","Mango"]
print(fruits[0])
print(fruits[-1])

# Update list:
fruits = ["Apple","Banana","Mango"]
fruits[1] = "Orange"
print(fruits)

# Add items:
fruits = ["Apple","Banana","Mango"]
fruits.append("Grapes")
fruits.insert(1,"Papaya")
print(fruits)

# Remove items:
fruits = ["Apple","Banana","Mango"]
fruits.remove("Mango")
fruits.pop()   #pop(1),pop(2)
print(fruits)

#slicing:
nums = [10,20,30,40,50]
print(nums[3:])
print(nums[:3])
print(nums[1:3])
print(nums[:-3])
print(nums[-3:])

# Looping:
fruits = ["Apple","Banana","Mango"]
for f in fruits :
    print("Fruit :",f)
    
#clean:
raw = ["DelHI","MUMbai","PUNE"]
clean = []

for c in raw:
    clean.append(c.strip().title())
print(clean)

#Replace wrong spelling:
wrong = ["kolkatta","Bengluru"]
fixed = []

for c in wrong:
    c = c.replace("kolkatta","Kolkata").replace("Bengluru","Bengaluru")
    fixed.append(c)
print(fixed)   

# extract years:
codes = ["Laptop-2024","Phone-2023"]
years = []

for c in codes:
    years.append(c[-4:])
print(years)    