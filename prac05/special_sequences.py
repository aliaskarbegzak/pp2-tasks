# Special Sequences
'''
Character	Example     Description
\A	        "\AThe"     Returns a match if the specified characters are at the beginning of the string		
\b	        r"\bain"    Returns a match where the specified characters are at the beginning or at the end of a word
            r"ain\b"    (the "r" in the beginning is making sure that the string is being treated as a "raw string")	
\B	        r"\Bain"    Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
            r"ain\B"    (the "r" in the beginning is making sure that the string is being treated as a "raw string")	
\d	        "\d"        Returns a match where the string contains digits (numbers from 0-9)		
\D	        "\D"        Returns a match where the string DOES NOT contain digits		
\s	        "\s"        Returns a match where the string contains a white space character		
\S	        "\S"        Returns a match where the string DOES NOT contain a white space character		
\w	        "\w"        Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)		
\W	        "\W"        Returns a match where the string DOES NOT contain any word characters		
\Z	        "Spain\Z"   Returns a match if the specified characters are at the end of the string	
'''
import re
# \A
txt = "The rain in Spain"
# Check if the string starts with "The":
print(re.findall("\AThe", txt)) # ['The']
print(re.findall("\Arian", txt)) # []

# \b
# Check if "ain" is present at the beginning of a WORD:
print(re.findall(r"\brai", txt)) # ['rai']
print(re.findall(r"\bain", txt)) # []
print(re.findall(r"\bThe", txt)) # ['The']
# Check if "ain" is present at the end of a WORD:
print(re.findall(r"ain\b", txt)) # ['ain', 'ain']
print(re.findall(r"rai\b", txt)) # []

# \B
# Check if "ain" is present, but NOT at the beginning of a word:
print(re.findall(r"\Bain", txt)) # ['ain', 'ain']
print(re.findall(r"\Brain", txt)) # []
# Check if "ain" is present, but NOT at the end of a word:
print(re.findall(r"\Brai", txt)) # ['rai']
print(re.findall(r"\Brain", txt)) # []

# \d
# Check if the string contains any digits (numbers from 0-9):
print(re.findall("\d", txt)) # []
txt = "The rain65 in7 6Spain"
print(re.findall("\d", txt)) # ['6','5','7','6']

# \D
# Return a match at every no-digit character:
x = re.findall("\D", txt) # ['T', 'h', 'e', ' ', 'r', 'a', 'i', 'n', ' ', 'i', 'n', ' ', 'S', 'p', 'a', 'i', 'n']

# \s
# Return a match at every white-space character:
print(re.findall("\s", txt)) # [' ',' ',' ']

# \S
# Return a match at every NON white-space character:
print(re.findall("\S", txt)) # ['T', 'h', 'e', 'r', 'a', 'i', 'n', 'i', 'n', 'S', 'p', 'a', 'i', 'n']
