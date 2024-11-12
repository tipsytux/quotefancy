import shutil
import os

import requests
from bs4 import BeautifulSoup

baseUrl = "https://quotefancy.com/"
downloadUrl = "https://quotefancy.com/media/wallpaper/3840x2160/"
def downloadImage(imageUrls, root, pageNumber):
	count = 0
	for linky in imageUrls:
		name = linky.split("/")[-1]
		newLink = downloadUrl+ name
		res = requests.get(newLink, stream=True)
		path = os.path.join(root_dir, name)
		with open(path, 'wb') as out_file:
			shutil.copyfileobj(res.raw, out_file)
			count += 1
			print(f'Processing: {root}, Page: {pageNumber}, Count: {count}',end="\r",flush=True)
		del res
	print()

def filterLinks(hyperlinks):
	img_links = []
	for link in hyperlinks:
		img = link.find("img")
		if img and img.get("data-original"):
			img_links.append(img['data-original'])
	return img_links

def generateRoots(root):
	generatedUrls = []
	for page in range(1,10,1):
		url = baseUrl+root+"/page/"+str(page)
		generatedUrls.append(url)
	return generatedUrls

# USAGE: Add all the galleries that you want to be scraped in the list below
roots = ["motivational-quotes",
         "inspirational-entrepreneurship-quotes",
         "startup-quotes"]

# The root directory
root_dir = "quotefancy"

if not os.path.exists(root_dir):
	os.mkdir(root_dir)

for root in roots:
	pages = generateRoots(root)
	status = True
	for page in pages:
		response = requests.get(page)
		pageNumber = page.split("/")[-1]
		if response.status_code==200:
			soup = BeautifulSoup(response.text,features="html.parser")
			hyperlinks = soup.find_all("a")
			img_links = filterLinks(hyperlinks)
			if img_links:
				downloadImage(img_links,root, pageNumber)
		else:
			break
