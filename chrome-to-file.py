#!/usr/bin/env python3
import subprocess
import sys
import os

LIST_URLS_COMMAND = ["chrome-cli", "list", "links"]

urls = []
input_url = ""

substring = input("Enter substring to search for: ")
if substring == "":
    exit(0)
pipe = subprocess.Popen(LIST_URLS_COMMAND, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
all_urls = pipe.communicate()[0].decode("utf-8").splitlines()
urls = [url.split(" ")[1] for url in all_urls if substring in url]

print("----------------------------------------\n")
for url,profile_id in zip(urls, range(len(urls))):
    print(url)
print()
exit(0)