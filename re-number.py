import os
import re

"""
This script renames all files in folders and adds the name of the folder in front
"""


mycwd = os.getcwd()
print("here's my working directory: " + mycwd)
pattern = r"\d+"
count = 0
for path, folders, files in os.walk(mycwd):
    myfolders = folders
    break


for path, folders, files in os.walk(mycwd):
    if len(folders)==0:
        for file in files:
            number = myfolders[count] + " #" + re.search(pattern, file).group().zfill(3) + ".jpg"
            print (number)
            os.rename(path+"\\"+file, path+"\\"+number)
        count += 1


print (myfolders)