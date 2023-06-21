# read a json file into a dictionary
import os
import json

cwd = os.getcwd()
files = os.listdir(cwd)
print("Files in %r: %s" % (cwd, files))

with open("python_cookbook/data.json","r") as f:
     data = json.load(f)
     
print(data)