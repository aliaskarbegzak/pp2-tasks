import re
# Return a list containing every occurrence of "ai":
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x) # ['ai','ai']

txt = "The rain in Spain"
# Check if "Portugal" is in the string:
x = re.findall("Portugal", txt)
print(x) # []

