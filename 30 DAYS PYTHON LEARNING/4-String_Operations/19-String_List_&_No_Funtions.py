#String List & Number Functions:

text = "banana"
print(text.count("a"))

print("hello.py".endswith("py"))

print("Sales.csv".startswith("Sales"))

print("123".isdigit())

print("ABC".isalpha())

print("AI07".isalnum())

print("Line1\nLine2")
      
print("Line1\nLine2".splitlines())


#List Functions:
nums = [4,7,4,3,9,0,1,2,5,6]
nums.sort()
print(nums)


fruits = ["Banana","Chickoo","Apple"]
print(sorted(fruits))

marks = [ 45,65,23,87,97,10]
print(min(marks),max(marks),sum(marks))

my_list = [1,2,1,3,1]
print(my_list.count(1))
print(my_list.index(2))

a = [1,2]
b = [3,4]
a.extend(b)
print(a)


#Number Functions:

print(round(3.678,2))   #roundoff

print(abs(-50))   #absolute

print(pow(2,3))    #Power(2*2*2)

print(divmod(10,3))  #output(3,1) ----3 means quotient and 1 means remainder

print(sum([5,5,5],5))


#Practical example:

products = ["laPTOP","    MUMbai","DELhi     "]
clean = [p.strip().title()for p in products]
clean.sort()
print(clean)    


emails = ['samu@gmail.com','abc@yahoo.com']
domains = [mail[mail.find("@")+1:] for mail in emails]
print(domains)


mobiles = ["1234567890","124RYu4566","1234665"]
valid = [m for m in mobiles if m.isdigit() and len(m)==10]
print(valid)