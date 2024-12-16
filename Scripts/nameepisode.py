#!/usr/bin/python3
import os
import re

#list all files in the current directory that contain SxEX in the name where x is season number and E is an episode number
name_of_episodes = input("Enter the name of the episodes: ")

files = []
for filename in os.listdir("."):
    if re.search(r'S\d+E\d+', filename):
        files.append(filename)


renamed = []
#get original name but starting with Season number and Episode number and concatenate after the name of the episodes
for filename in files:
    #name after SxEx 
    name = re.sub(r".*(S\d{1,2}E\d{1,2}.*)", r"\1", filename).strip()
    os.rename(filename, f"{name_of_episodes} - {name}")
    renamed.append(f"{name_of_episodes} - {name}")
renamed.sort()

print("Renamed files:\n")
for filename in renamed:
    print(filename)