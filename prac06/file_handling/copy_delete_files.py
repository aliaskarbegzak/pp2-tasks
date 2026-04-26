#   File delete
# Remove the file "demofile.txt"
import os
os.remove("demofile.txt")

# Check if File exist:
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

#   Delete folder
os.rmdir("myfolder")

#   File copy
import shutil
shutil.copy("demofile.txt", "demofile_copy.txt")
# Check if File exists before copying:
if os.path.exists("demofile.txt"):
  shutil.copy("demofile.txt", "demofile_copy.txt")
else:
  print("The source file does not exist")

#   Copy folder
# Copies the entire directory tree from "myfolder" to "myfolder_copy"
shutil.copytree("myfolder", "myfolder_copy")