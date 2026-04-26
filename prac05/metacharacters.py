# Metacharacters
"""
Character	Description	                                    Example	
 []     	A set of characters     	                    "[a-m]"	
 \	        Signals a special sequence 	                    "\d"	
 .	        Any character                   	            "he..o"	
 ^	        Starts with	                                    "^hello"	
 $	        Ends with	                                    "planet$"	
 *	        Zero or more occurrences	                    "he.*o"	
 +	        One or more occurrences	                        "he.+o"	
 ?	        Zero or one occurrences	                        "he.?o"	
 {}     	Exactly the specified number of occurrences     "he.{2}o"	
 | 	        Either or	                                    "falls|stays"	
 ()	        Capture and group	 	                         
"""
# []
import re
txt = "The rain in Spain"
# Find all lower case characters alphabetically between "a" and "m":
x = re.findall("[a-m]", txt)
print(x) # ['h', 'e', 'a', 'i', 'i', 'a', 'i']

# \ 
txt = "That will be 59 dollars"
# Find all digit characters:
x = re.findall("\d", txt)
print(x) # ['5', '9']

# .
txt = "hello planet"
# Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
x = re.findall("he..o", txt)
print(x) # ['hello']

# ^
txt = "hello planet"
# Check if the string starts with 'hello':
x = re.findall("^hello", txt)
if x: # ['hello'] / True
  print("Yes, the string starts with 'hello'")
else:
  print("No match")

# $
txt = "hello planet"
# Check if the string ends with 'planet':
x = re.findall("planet$", txt)
if x: # ['planet'] / True
  print("Yes, the string ends with 'planet'")
else:
  print("No match")

# *
txt = "hello planet"
# Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":
x = re.findall("he.*o", txt)
print(x) # ['hello']

# +
txt = "hello planet"
# Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":
x = re.findall("he.+o", txt)
print(x) # ['hello']

# ?
txt = "hello planet"
# Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":
x = re.findall("he.?o", txt)
print(x) # []
#This time we got no match, because there were not zero, not one, but two characters between "he" and the "o"

# {}
txt = "hello planet"
# Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":
x = re.findall("he.{2}o", txt)
print(x) # ['hello']

# | 
txt = "The rain in Spain falls mainly in the plain!"
# Check if the string contains either "falls" or "stays":
x = re.findall("falls|stays", txt)
print(x) # ['falls']
if x: # True
  print("Yes, there is at least one match!")
else:
  print("No match")

# ()
txt = "The rain in Spain"
x = re.search(r".+(\bSpain).+", txt)
print(x.group(1)) # Spain

