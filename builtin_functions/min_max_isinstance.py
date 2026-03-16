# min() / max() with key - find extreme values by a custom criterion
words = ["cherry", "apple", "banana", "date"]

print(min(words))                  # "app-e" — alphabetically first
print(max(words))                  # "da-e" — alphabetically last

print(min(words, key=len))         # "da-e" — shortest word
print(max(words, key=len))         # "banana" or "cher-y" — first encountered longest word

print(max(sorted(words), key=len)) # "banana" - longest word that is also alphabetically first

# With a list of dicts
students = [
    {"name": "Alice", "grade": 88},
    {"name": "Bob", "grade": 95},
    {"name": "Charlie", "grade": 72},
]

best = max(students, key=lambda s: s["grade"])
worst = min(students, key=lambda s: s["grade"])

print(f"Best: {best['name']} ({best['grade']})") # Best: Bob (95)
print(f"Worst: {worst['name']} ({worst['grade']})") # Worst: Charlie (72)


# isinstance() - check if an object is an instance of a type (or tuple of types)
# example without isinstance()
print(type(42) == type(int()))     # True    

print(isinstance(42, int))         # True
print(isinstance(3.14, float))     # True
print(isinstance("hi", str))       # True
print(isinstance([1, 2], list))    # True

# Check against multiple types at once
print(isinstance(42, (int, float)))         # True
print(isinstance("hi", (int, float)))       # False
print(isinstance("hi", (int, float, str)))  # True

# Practical use: handling mixed input
def double(value):
    if isinstance(value, (int, float)):
        return value * 2
    elif isinstance(value, str):
        return value + value
    elif isinstance(value, list):
        return value + value
    else:
        return None

print(double(5))          # 10
print(double("ha"))       # "haha"
print(double([1, 2]))     # [1, 2, 1, 2]
print(double({1, 2}))     # None