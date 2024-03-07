#!/usr/bin/env python3
import os

video_extensions = ["mkv", "avi", "mp4"]
files = os.listdir(os.getcwd())
files.sort()

no_file = 1
for extension in video_extensions:
    for file in files:
        if extension in file:
            no_file = 0

if no_file:
    print("No video files found")
    exit()

with open(".converted", "w") as f:
    for file in files:
        for extension in video_extensions:
            if extension in file:
                f.write(file)
                f.write("\n")

with open(".converted", "r") as f:
    for line in f:
        print(line,end="")