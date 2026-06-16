# String Indexing:

name ='Samiksha'
print(name)
print(name[0])
print(name[-5])


# String Slicing:

product = "Laptop pro 2024"
print(product[0:6])    #prints Laptop 
print(product[-4:-1])  #doesn't include 4 of 2024
print(product[-4:])    #prints 2024



text = "DataAnalysis"

#Extracting 1st four letters(data)
print("First 4 Letter :",text[0:4])

#Extracting middle letters(anslysis)
print("middle letters :",text[4:12]) 

#Extract from beginning(analaysis)
print("middle letters :",text[4:]) 

#Extract till end(data)
print("till end :",text[:4]) 

 #Extract last 5 characters(lysis)
print("Last five characters :",text[-5:])


# Skip Text:
text = "DataAnalysis"
print("Skip txt: ",text[0:12:2]) #DtAayi
print("Reverse: ",text[::-1]) #sisylanAataD

print("Reverse :",text[4::-1]) #AataD
print("Reverse :",text[:4:-1]) #sisylan

text = "DataAnalysis"
print("Reverse :",text[4::-2]) #AtD
print("Reverse :",text[:4:-2]) #ssln