#!/usr/bin/python3
import os
import re
#list all files in the current directory that contain SxEX in the name where x is season number and E is an episode number

files = []
for filename in os.listdir("."):
    if re.search(r'S\d+E\d+', filename):
        files.append(filename)

renamed = []
#delete everything after episode number but keep the extension
for filename in files:
    newname = re.sub(r'(S\d+E\d+).*', r'\1', filename)
    extension = filename.split('.')[-1]
    os.rename(filename, newname+"."+extension)
    renamed.append(newname+"."+extension)

renamed.sort()

print("Renamed files:\n")
for filename in renamed:
    print(filename)
