from bs4 import BeautifulSoup
import requests


def get_statisticks():
	description = []
	url = "https://opensea.io/collection/pandasboxclub"
	page = requests.get(url)
	soup = BeautifulSoup(page.text, "html.parser")
	allNews = soup.findAll('h3', {"class" : "Blockreact__Block-sc-1xf18x6-0 Textreact__Text-sc-1w94ul3-0 bqHBns kscHgv"})
	print(allNews)
	#for i in allNews:
		#description.append(i.get_text())
	#return description

print(get_statisticks())



