import os
import re
import zipfile

"""
This script creates cbr files out of every folder
"""

mycwd = os.getcwd()
print("here's my working directory: " + mycwd)
pattern = r"\d+"
count = 0
for path, folders, files in os.walk(mycwd):
    myfolders = folders
    break
print (myfolders)

for myfolder in myfolders:
    os.chdir(mycwd)
    with zipfile.ZipFile(myfolder+".cbr", "x") as my_zip:
        for path, folders, files in os.walk(mycwd+"\\"+myfolder):
            os.chdir(mycwd+"\\"+myfolder)
            for file in files:
                my_zip.write(file)
