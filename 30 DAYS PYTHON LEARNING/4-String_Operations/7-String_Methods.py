# String Methods:

text1 ="      hello, world!      "
print("Space:",text1)


#strip removes space from left & right side
print("Removes Space:",text1.strip())


#Convert to Captial(upper) letters:
text1 ="      hello, world!      "
print("Capital Letters:",text1.upper().strip())


#Convert to Proper Case:
text1 ="      hello, world!      "
print("Proper Letters:",text1.title().strip())


#Convert to Small(lower) case:
text1 ="      HELLO, WORLD!      "
print("Small letters:",text1.lower().strip())


# Replace:
text1 ="      hello, world!      "
print("Replace World with Samiksha:",text1.replace("world","Samiksha").strip())


#Count Occurences of a letter of word:
text = "Samiksha"
print("Count of a:",text.count("a"))


# Check if text starts with something:
text1 = "hello,world!"
print("Starts with hello?",text1.strip().startswith("hello"))


#Check if only numbers are present in data
mobile = "1234567890"
print("Is Numeric:",mobile.isnumeric())

mobile = "qwerty"
print("Is Numeric:",mobile.isnumeric())


#Split string into list of words:
msg = "Welcome to Python learning"
word = msg.split()
print("Word List :",word)


# Join with hyphen:
msg = "Welcome to Python learning"
word = msg.split()
join_text = "-".join(word)
print("join_text:",join_text)


#Position of letter:
msg = "Welcome to Python learning"
print("Index of P:",msg.find("P"))

# extract domain:
email ="student@gmail.com"
domain = email[email.find("@")+1:]
print("Domain:",domain)

