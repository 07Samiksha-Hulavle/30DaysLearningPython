#Functions:

#Without Parameters:

def greet():
    print("Hello Friends!")

greet()   


#Single Parameter:
def welcome(name):
    print("Welcome",name)

welcome("Samiksha")


#Multi-Parameters:
def add(a,b):
    c = a+b
    # print(c)
    #  ORRRRRRR
    print(f"{a}+{b}={c}")

add(10,20)

#The function that cam be used multiple times:
def add(a,b):
    return a+b

sum = add(10,20)
print(sum)

#calling add functio in multiply:
def multiple(x):
    return x*2

result = multiple(sum)
# ORRR
result = multiple(add(10,20))
print(result)


#Clean the Text:
def clean_text(value):
    return value.strip().title()

output = clean_text("     MuMBAi    ")
print(output)


#fix city:
def fix_city(city):
    city = city.lower().strip()
    city = city.replace("mombay","mumbai")
    city = city.replace("kolkatta","kolkata")
    return city.title()

print(fix_city("   mombay"))


#get year:
def get_year(code):
    return code[-4:]

print(get_year("laptop-2006"))


#valid ot invalid email:
def is_email_valid(email):
    return '@' in email and '.' in email

print(is_email_valid("sam07@gmail.com"))


#total salary by adding bonus:
def total_salary(basic,bonus):
    return basic + bonus

print(total_salary(5000,1000))


#stats:
def stats(nums):
    return min(nums),max(nums),sum(nums),len(nums),sum(nums)/len(nums)

print(stats([10,20,30]))


#clean list:
def clean_list(values):
    cleaned = []
    for v in values:
        cleaned.append(v.strip().title())
    return cleaned
print(clean_list(["    PUNE","mumBaI     ","   DelHI    "]))        
