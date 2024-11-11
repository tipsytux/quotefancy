import shutil
import os

import requests
from bs4 import BeautifulSoup

# USAGE: Add all the galleries that you want to be scraped in the list below
roots = ["https://quotefancy.com/motivational-quotes",
         "https://quotefancy.com/inspirational-entrepreneurship-quotes",
		 "https://quotefancy.com/positive-quotes",
		 "https://quotefancy.com/elon-musk-quotes",
         "https://quotefancy.com/startup-quotes"]

# The root directory
root_dir = "quotefancy"
baselink = "https://quotefancy.com/media/wallpaper/3840x2160/"
if not os.path.exists(root_dir):
	os.mkdir(root_dir)

for root in roots:
	current = root.split("/")[-1]
	response = requests.get(root)
	if response.status_code==200:
		soup = BeautifulSoup(response.text)
		hyperlinks = soup.find_all("a")
		img_links = []
		for link in hyperlinks:
			img = link.find("img")
			if img and img.get("data-original"):
				img_links.append(img['data-original'])
		if img_links:
			count = 0
			for linky in img_links:
				name = linky.split("/")[-1]
				newLink = baselink+ name
				res = requests.get(newLink, stream=True)
				path = os.path.join(root_dir, name)
				with open(path, 'wb') as out_file:
					shutil.copyfileobj(res.raw, out_file)
					count += 1
					print(f'Processing: {current}, Count: {count}',end="\r",flush=True)
				del res
			print()
