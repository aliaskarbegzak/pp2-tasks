import re
# Check if the string starts with "The" and ends with "Spain":
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x: # The rain in Spain / True
  print("YES! We have a match!") 
else:
  print("No match")

txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start()) 
# The first white-space character is located in position: 3

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x) # None

