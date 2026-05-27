# For Loop

#print 1-10:
for i in range (1,11):
    print(i)


 # print 2 characters:
word = "Python"
for alphabet in word[0:3]:
    print(alphabet)


#SQL word 20 times:
word="SQL"
for j in range(1,11):
    print(word)


#loop through list:
items = ["Pen","Book","Pencil"]
for item in items:
    print(item)


#even number
for n in range(0,21,2):
    print(n)    


#odd number
for n in range(1,21,2):
    print(n)    


#total calculations:   
marks = [78, 82, 90, 65, 76, 45]
total = 0
for m in marks:
    total += m
print("Total:",total)


#clean city names:
cities = ["MumBaI "," pune"," DELHI  "]
cleaned = []
for c in cities:
    cleaned.append(c.strip().title())
print(cleaned)    


#loops with if condition:
nums = [5, 12, 3, 18, 7]
for n in nums:
    if n > 10:
        print(n,"is greater than 10")
    else:
        print(n,"is not greater than 10")

nums = [5, 12, 3, 18, 7]
for n in nums:
    if n%2 == 0:
        print(n,"is even number")
    else:
        print(n,"is odd number")

#extract last 4 digits
ids = ["EMP-001122", "EMP-889900"]  
for emp in ids:
    print(emp[-6:])      