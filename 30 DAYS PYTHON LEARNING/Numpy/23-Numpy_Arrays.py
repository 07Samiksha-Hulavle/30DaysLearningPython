import numpy as np

print("=== Creating Array ===")
arr = np.array([10,20,30,40,50,60,70])
print(arr)


print("\n=== Indexing & Slicing ===")
print(arr[2])
print(arr[0:4])


print("\n=== Vectorized Operations ===")
print(arr + 10)
print(arr * 2)
print(arr ** 2)


print("\n=== Numpy Functions ===")
print(arr.sum())
print(arr.mean())
print(arr.min(),arr.max())
   

print("\n=== Data Cleaning example ===")
data = np.array([10,-20,30,-40,50])
clean = data[data >= 0]
print("Cleaned Data:",clean)


# Replacing Average Of Non Negative Values:
marks = np.array([80,90,-1,75,-1,60])
marks[marks == -1] = marks[marks != -1].mean()
print("Filled Missing :",marks)

#Removing Leading ,Trailing Spaces & Capitalizing the First Letter of the cities :
cities = np.array(["    MumbAI","PUne   ","    DElhi   ","mumbAI   "])
cities = np.char.strip(cities)
cities = np.char.title(cities)
print(cities)
