#File Handling (Text File):


# 1)Reading Full File:
with open("sample.txt","r") as f:
    print(f.read())

# Reading Line By Line:
with open("sample.txt","r") as f:
    for line in f:
        print(line.strip().title())  


# Writing (Overwrite):
with open("notes.txt","w") as f:
    f.write("Day - 20 File Handling \n")
    f.write("Learning Read and Write \n")


# Appending:
with open("notes.txt","a") as f:
    f.write("Appending New Content \n")


# Cleaning Data in a File:  
cleaned = []
with open("sample.txt","r") as f:  
    for line in f:
        cleaned.append(line.strip().title())

with open("cleaned_output.txt","w") as f:
    for city in cleaned:
        f.write(city + "\n")


# Counting Lines:
count = 0
with open("sample.txt","r") as f:
    for _ in f:
        count += 1
print("Total Lines" , count)        