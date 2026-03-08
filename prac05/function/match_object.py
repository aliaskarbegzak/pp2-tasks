import re
# The search() function returns a Match object:
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) # <_sre.SRE_Match object; span=(5, 7), match='ai'>


# Search for an upper case "S" character in the beginning of a word, and print its position:
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span()) # (12,17)

# The string property returns the search string:
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string) # The rain in Spain

# Search for an upper case "S" character in the beginning of a word, and print the word:
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group()) # Spain
