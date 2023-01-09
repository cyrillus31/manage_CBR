import os
"""
This file allow to batch change the extensions of the files
"""
extension = input("To what extension do you want change? For example enter '.cbr' ")
for path, folders, files in os.walk (os.getcwd()):
    myfiles = files
    break

for file in myfiles:
    if ".py" not in file:
        os.rename (file, file.split(".")[0]+ extension)
    else:
        pass