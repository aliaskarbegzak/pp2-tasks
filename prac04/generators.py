# Iterators
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit)) # apple
print(next(myit)) # banana
print(next(myit)) # cherry

mystr = "banana"
myit = iter(mystr)
print(next(myit)) # b
print(next(myit)) # a
print(next(myit)) # n
print(next(myit)) # a
print(next(myit)) # n
print(next(myit)) # a

mytuple = ("apple", "banana", "cherry")
for x in mytuple:
  print(x)

mystr = "banana"
for x in mystr:
  print(x) 

# Generators
def my_generator():
  yield 1
  yield 2
  yield 3
for value in my_generator():
  print(value) # 1 2 3


def count_up_to(n):
  count = 1
  while count <= n:
    yield count
    count += 1
for num in count_up_to(5):
  print(num)


def large_sequence(n):
  for i in range(n):
    yield i
# This doesn't create a million numbers in memory
gen = large_sequence(1000000)
print(next(gen)) # 0
print(next(gen)) # 1
print(next(gen)) # 2


def simple_gen():
  yield "Emil"
  yield "Tobias"
  yield "Linus"
gen = simple_gen()
print(next(gen)) # Emil
print(next(gen)) # Tobias
print(next(gen)) # Linus


def fibonacci():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b
# Get first 100 Fibonacci numbers
gen = fibonacci()
for _ in range(100):
  print(next(gen))

# Generator Methods
def echo_generator():
  while True:
    received = yield
    print("Received:", received)
gen = echo_generator()
next(gen) # Prime the generator
gen.send("Hello") # The send() method allows you to send a value to the generator
gen.send("World") 
# Received: Hello
# Received: World

def my_gen():
  try:
    yield 1
    yield 2
    yield 3
  finally:
    print("Generator closed")
gen = my_gen()
print(next(gen))
gen.close() # The close() method stops the generator
# 1
# Generator closed