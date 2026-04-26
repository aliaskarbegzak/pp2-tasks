# Flags
"""
Flag        	Shorthand	    Description	
re.ASCII    	re.A	        Returns only ASCII matches	
re.DEBUG        		        Returns debug information	
re.DOTALL   	re.S    	    Makes the . character match all characters (including newline character)	
re.IGNORECASE	re.I    	    Case-insensitive matching	
re.MULTILINE	re.M     	    Returns only matches at the beginning of each line	
re.NOFLAG           		    Specifies that no flag is set for this pattern	
re.UNICODE  	re.U	        Returns Unicode matches. This is default from Python 3. For Python 2: use this flag to return only Unicode matches	
re.VERBOSE  	re.X    	    Allows whitespaces and comments inside patterns. Makes the pattern more readable
"""
# re.A / re.ASCII 
import re
txt = "Åland"
# Find all ASCII matches:
print(re.findall("\w", txt, re.ASCII)) # ['l', 'a', 'n', 'd']
# Without the flag, the example would return all character:
print(re.findall("\w", txt)) # ['Å', 'l', 'a', 'n', 'd']
# Same result using the shorthand re.A flag:
print(re.findall("\w", txt, re.A)) # ['l', 'a', 'n', 'd']

# re.DEBUG
txt = "The rain in Spain"
# Use a case-insensitive search when finding a match for Spain in the text:
print(re.findall("spain", txt, re.DEBUG))
"""
LITERAL 115
LITERAL 112
LITERAL 97
LITERAL 105
LITERAL 110

 0. INFO 16 0b11 5 5 (to 17)
      prefix_skip 5
      prefix [0x73, 0x70, 0x61, 0x69, 0x6e] ('spain')
      overlap [0, 0, 0, 0, 0]
17: LITERAL 0x73 ('s')
19. LITERAL 0x70 ('p')
21. LITERAL 0x61 ('a')
23. LITERAL 0x69 ('i')
25. LITERAL 0x6e ('n')
27. SUCCESS
"""
# re.DOTALL / re.S
txt = """Hi
my
name
is
Sally"""
# Search for a sequence that starts with "me", followed by one character, even a newline character, and continues with "is":
print(re.findall("me.is", txt, re.DOTALL)) # ['me\nis']
# This example would return no match without the re.DOTALL flag:
print(re.findall("me.is", txt)) # []
# Same result with the shorthand re.S flag:
print(re.findall("me.is", txt, re.S)) # ['me\nis']

# re.IGNORECASE / re.I
txt = "The rain in Spain"
# Use a case-insensitive search when finding a match for Spain in the text:
print(re.findall("spain", txt, re.IGNORECASE)) # ['Spain']
# Same result using the shorthand re.I flag:
print(re.findall("spain", txt, re.I)) ['Spain']

# re.MULTILINE / re.M
txt = """There
aint much
rain in 
Spain"""
# Search for the sequence "ain", at the beginning of a line:
print(re.findall("^ain", txt, re.MULTILINE)) # ['ain']
# This example would return no matches without the re.MULTILINE flag, because the ^ character without re.MULTILINE only get a match at the very beginning of the text:
print(re.findall("^ain", txt)) # []
# Same result with the shorthand re.M flag:
print(re.findall("^ain", txt, re.M)) # ['ain']

# re.UNICODE / re.U
txt = "Åland"
# Find all UNICODE matches:
print(re.findall("\w", txt, re.UNICODE)) # ['Å', 'l', 'a', 'n', 'd']
# Same result using the shorthand re.U flag:
print(re.findall("\w", txt, re.U)) # ['Å', 'l', 'a', 'n', 'd']

# re.VERBOSE / re.X
text = "The rain in Spain falls mainly on the plain"
# Find and return words that contains the phrase "ain":
pattern = """
[A-Za-z]* #starts with any letter
ain+      #contains 'ain'
[a-z]*    #followed by any small letter
"""
print(re.findall(pattern, text, re.VERBOSE)) # ['rain', 'Spain', 'mainly', 'plain']
# The example would return nothing without the re.VERBOSE flag
print(re.findall(pattern, text)) # []
# Same result with the shorthand re.X flag:
print(re.findall(pattern, text, re.X)) # ['rain', 'Spain', 'mainly', 'plain']

