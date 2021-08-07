from bs4 import BeautifulSoup
import requests
import time
import csv

# create BeautifulSoup object
page = requests.get("https://rlstats.net/leaderboards/skills")
soup = BeautifulSoup(page.content, "html.parser")

# parse html and find info
groups = list(zip(*[iter(soup.find_all("td"))] * 4))[:100]

# get current time
time = time.time()

# create tuples of each entry
data = [
    (
        entry[0].string,
        entry[1].a.string,
        entry[1].a.get("href"),
        entry[2].string,
        entry[3].string,
        time,
    )
    for entry in groups
]

# create unique filename based on the datetime
filename = str(time) + ".csv"

# write to csv
with open(filename, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)
