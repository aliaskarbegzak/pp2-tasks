import re
# Split the string at every white-space character:
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x) # ['The', 'rain', 'in', 'Spain']

# Split the string at the first white-space character:
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x) # ['The', 'rain in Spain']

