#   Map
# https://docs.python.org/3/library/functions.html
lst = [1, 2, 3]
map_result = map(lambda x: 2*x, lst)
print(type(map_result)) # <class 'map'>
print(list(map_result)) # [2, 4, 6]
for num in map(lambda x: 2*x, lst):
    print(num)

# filter() - keeps only elements that satisfy a condition
# Returns an iterator, like map().
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens) # [2, 4, 6, 8, 10]
# same results, but using a list comprehension instead
evens = [x for x in numbers if x % 2 == 0]
print(evens) # [2, 4, 6, 8, 10]

# filter with a named function
def is_positive(n):
    return n > 0

mixed = [-3, -1, 0, 2, 5, -7, 8]
positives = list(filter(is_positive, mixed))
print(positives)  # [2, 5, 8]

# Combining map and filter:
# Get squares of even numbers only
result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(result)  # [4, 16, 36, 64, 100]