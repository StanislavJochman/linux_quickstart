#!/usr/bin/env python3
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import argparse


parser = argparse.ArgumentParser(description='Add titles to files')
parser.add_argument('--website', help='Website with titles', required=False)
parser.add_argument('--skip', help='Skip files', required=False)
args = parser.parse_args()
skip = args.skip
website = args.website

text = []


files = os.listdir(os.getcwd())
languages = "UNKNOWN"

extensions = ["mkv","avi","mp4","ts"]
renamefiles = []
for string in range(len(files)):
    for extension in range(len(extensions)):
        if extensions[extension] in files[string]:
            jmp = 1
            renamefiles.append(files[string])
            break
if website == None:
    website = input("Website: ")
    print("")
options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)

browser.get(website)
episode = browser.find_elements(By.XPATH,'//*[@id="page-wrapper"]/div/div[1]/div/section/div[2]/div')
episodes = [x.text for x in episode]
episodes = episodes[0].split('\n',100)
for episode in episodes:
    if("(" in episode):
        episodes.remove(episode)

episode_names = []

for episode in episodes:
    episode = episode.replace("?","")
    episode = episode.replace(":"," - ")
    episode_names.append(episode)

renamefiles.sort()
if len(renamefiles) != len(episode_names):
    browser.close()
    print("Error: Number of files does not match number of episodes")
    exit(1)
if skip == None:
    for x in range(len(renamefiles)):
        try:
            newname = renamefiles[x][:-4] + " - " + episode_names[x] + renamefiles[x][-4:]
            os.rename(renamefiles[x], newname)
        except:
            pass
browser.close()
with open(".csfd","w") as f:
    f.write(f'URL="{website}"\n')
    f.write(f'EPISODES="{len(episode_names)}"\n')
    f.write(f'LANGUAGES="{languages}"\n')
print("------------------------------------------")
print("Total episodes: " + str(len(episode_names)))
print("------------------------------------------")
print("Files renamed:\n")
os.system("ls")
exit()
