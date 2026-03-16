#   File Write
""" 
"a" - Append - will append to the end of the file
"w" - Write - will overwrite any existing content
"""

with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!")
#open and read the file after the appending:
with open("demofile.txt") as f:
  print(f.read())
"""
Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck!Now the file has more content!
"""

with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")
#open and read the file after the overwriting:
with open("demofile.txt") as f:
  print(f.read()) # Woops! I have deleted the content!

#   File create
"""
"x" - Create - will create a file, returns an error if the file exists
"a" - Append - will create a file if the specified file does not exists
"w" - Write - will create a file if the specified file does not exists
"""

# This will create a new file:
f = open("myfile.txt", "x")
# If the file already exist, an error will be raised.

