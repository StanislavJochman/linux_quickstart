#!/usr/bin/env python3
import subprocess
import sys
import os

CHROME_COMMAND = "/Applications/Chromium.app/Contents/MacOS/Chromium"
PROFILE_COMMAND =  "--profile-directory=\"Person {profile}\""
LIST_URLS_COMMAND = ["chrome-cli", "list", "links"]

urls = []
input_url = ""
if len(sys.argv) > 1:
    if sys.argv[1] == "url":
        while input_url != "q" and input_url != "Q":
            input_url = input("Enter URL (q to quit): ")
            if input_url != "q":
                urls.append(input_url)
else:
    substring = input("Enter substring to search for: ")
    pipe = subprocess.Popen(LIST_URLS_COMMAND, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    all_urls = pipe.communicate()[0].decode("utf-8").splitlines()
    urls = [url.split(" ")[1] for url in all_urls if substring in url]

for url,profile_id in zip(urls, range(len(urls))):
    print([CHROME_COMMAND, PROFILE_COMMAND.format(profile=profile_id), url])
    #subprocess.call([CHROME_COMMAND, PROFILE_COMMAND.format(profile=profile_id), url],shell=True)
    subprocess.Popen([CHROME_COMMAND + " " + PROFILE_COMMAND.format(profile=profile_id) + " " + url],shell=True)
exit(0)