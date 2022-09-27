from tkinter import Tk
from tkinter.filedialog import askdirectory

import os
import hashlib

# file dialog box
Tk().withdraw()
path = askdirectory(title="Select a folder")

# list out files in main folder 
# walk through each subdirectory and prints out files
walker = os.walk(path)
uniqueFiles = dict()

for folder, sub_folders, files in walker:
  for file in files:
    filepath = os.path.join(folder, file)
    filehash = hashlib.md5(open(filepath, "rb").read()).hexdigest()
    
    if filehash in uniqueFiles:
      os.remove(filepath)
      print(f"{filepath} has been deleted")
    else:
      uniqueFiles[filehash] = path



  









