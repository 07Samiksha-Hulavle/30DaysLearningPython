# Data Types:

# 1)Text: used to store text 
# String:

customer_name = "Samiksha"
print("Customer Name is :",customer_name)
print("Customer Name Data Type is : ",type(customer_name))


# 2)Numeric: used to store numbers like integer, float, decimal
# 2.1)Integer :- complete number

product_quantity = 100
orders = 2000

print("product_quantity Data Type is :",type(product_quantity))
print("orders Data Type is : ",type(orders))


# 2.2)Float :- Decimal Number:

salary=59401.96

print("salary Data Type is :",type(salary))


# 2.3)Complex Number:

a = 7+21j

print(type(a))


# 3)Boolean :- True/False

is_active = True

print(type(is_active))


# 4)Sequence:
# 4.1)List:

cities = ['Pune','Mumbai','Chennai','Delhi']
print(cities)

print(type(cities))

# 4.2)Tuple:

marks = (56,54,25,78,96)
print(marks)

print(type(marks))

# 4.3)Range:

#num = range(3) 
num = range(1,11)

print(list(num))   #[0,1,2,3,4] / [1,2,3,4,5,6,7,8,9,10]
print(type(num))
      

# 5)Dictionary:

dictionary = {
    'Name' : 'Sam',
    'Age' : 21, 
    'City' : 'Pune'
}
print(dictionary)

print(type(dictionary))


# 6)Set:
set = {1,2,3,5,6,4,2,3}
print(set)

print(type(set))

# 7)NoneType:
remark = None
print(remark,type(remark))


print(type("samii"))
print(type(3000))
print(type(7.21))
print(type(2+3j))
print(type(['sam']))
print(type((1,2,3,4,5,6,7)))
print(type({'sam':23,'tom':34}))
print(type(True))
