# any() - returns True if at least one element is truthy
# all() - returns True if all elements are truthy

numbers = [0, 0, 0, 1]
print(any(numbers))  # True - at least one non-zero
print(all(numbers))  # False - not all are non-zero

numbers = [1, 2, 3]
print(any(numbers))  # True
print(all(numbers))  # True

numbers = [0, 0, 0]
print(any(numbers))  # False
print(all(numbers))  # False

# Practical use: check conditions across a collection
ages = [18, 21, 16, 25, 14]

all_adults = all(age >= 18 for age in ages)
any_adults = any(age >= 18 for age in ages)

print(f"All adults: {all_adults}")   # False
print(f"Any adults: {any_adults}")   # True

# sorted() - returns a new sorted list
# Works with any iterable, does NOT modify the original
numbers = [5, 2, 8, 1, 9, 3]

print(sorted(numbers))               # [1, 2, 3, 5, 8, 9]
print(sorted(numbers, reverse=True)) # [9, 8, 5, 3, 2, 1]
print(numbers)                       # [5, 2, 8, 1, 9, 3] - unchanged

# sorted() with key - sort by a custom criterion
words = ["banana", "apple", "cherry", "date"]
print(sorted(words))                        # alphabetical
print(sorted(words, key=len))               # by length
print(sorted(words, key=lambda w: w[-1]))   # by last character
"""
['apple', 'banana', 'cherry', 'date']
['date', 'apple', 'banana', 'cherry']
['banana', 'apple', 'date', 'cherry']
"""

# Sorting a list of tuples
students = [
    ("Alice", 88),
    ("Bob", 95),
    ("Charlie", 72),
    ("Diana", 91),
]

by_name = sorted(students, key=lambda s: s[0])
by_grade = sorted(students, key=lambda s: s[1], reverse=True)

print(by_name)
print(by_grade)
"""
[('Alice', 88), ('Bob', 95), ('Charlie', 72), ('Diana', 91)]     
[('Bob', 95), ('Diana', 91), ('Alice', 88), ('Charlie', 72)]
"""