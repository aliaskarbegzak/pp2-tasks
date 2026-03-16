# enumerate() - adds an index to each element during iteration
fruits = ["apple", "banana", "cherry", "mango"]

# Without enumerate:
for i in range(len(fruits)):
    print(i, fruits[i])
"""
0 apple
1 banana
2 cherry
3 mango
"""
print("---------")

# With enumerate:
for i, fruit in enumerate(fruits):
    print(i, fruit)
"""
0 apple
1 banana
2 cherry
3 mango
"""
print("---------")

# Custom start index
for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)
"""
1 apple
2 banana
3 cherry
4 mango
"""

# zip() - combines multiple iterables element by element
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["Astana", "Almaty", "Aktau"]

# Zip two lists
print(zip(names, ages))  # <zip object at 0x0000016F38457C80>
print(type(zip(names, ages))) # <class 'zip'>

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
"""
Alice is 25 years old
Bob is 30 years old
Charlie is 35 years old
"""
print("---------")

# Zip three lists
for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age}, from {city}")
"""
Alice, 25, from Astana
Bob, 30, from Almaty
Charlie, 35, from Aktau
"""
print("---------")

# Convert to a list of tuples
pairs = list(zip(names, ages))
print(pairs) # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# If lists have different lengths, zip stops at the shortest
short = [1, 2]
long = [10, 20, 30, 40]
print(list(zip(short, long)))  # [(1, 10), (2, 20)]