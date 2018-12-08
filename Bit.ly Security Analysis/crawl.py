import requests
from bs4 import BeautifulSoup
import lxml
import random
import string
import csv
import time

writeF = open('URL.csv', 'a', newline='')
writer = csv.writer(writeF)

f = open('hashes.csv', 'r')
reader = csv.reader(f)
for row in reader:		
	site = 'https://bitly.com/' + str(row) + '+'
	res = requests.get(site)
	if (res.status_code != 200): #404
		writeList = [row, '', 0, '', '', '', '', '']
	else:
		soup = BeautifulSoup(res.text, 'lxml')
		
		test = str(soup.select('script')[6]) # Removes irrelivant data at the beginning)

	
		# Puts the response into myList for string parsing
		myList = []
		current = ""
		for char in test:
			if (char == '\n'):
					myList.append(current)
					current = ""
			else:
				current += char
		myList.pop(0)
		myList.pop(0)
		myList.pop(0)

		# Iterates through the first section of data (headline)
		temp = myList.pop(0)
		temp = temp.replace(" ", "\n")	
		currentList = []
		current = ""
		for char in temp:
			if (char == '\n'):
					currentList.append(current)
					current = ""
			else:
				current += char
		currentList.append(current)

		start = currentList[11]
		start = start[:-1]

		url = currentList[22]
		url = url[1:]
		url = url[:-2]

		person = currentList[18]
		person = person[1:]
		person = person[:-3]

		image = currentList[16]
		image = image[1:]
		image = image[:-2]

		# Iterates through second section of data (analytics)
		temp = myList.pop(0)
		temp = temp.replace(" ", "\n")	
		currentList = []
		current = ""
		for char in temp:
			if (char == '\n'):
					currentList.append(current)
					current = ""
			else:
				current += char
		currentList.append(current)

		user_clicks = currentList[1]
		user_clicks = user_clicks[:-1]

		global_clicks = currentList[9]
		global_clicks = global_clicks[:-2]

		isMalicious = myList.pop(0)
		isMalicious = isMalicious[:-1]

		writeList = [str(row), isMalicious, start, person, image, user_clicks, global_clicks, url]
		
		if (len(writeList[7]) >= 8):
			if (writeList[7][:4] == "http"):
				print(writeList)
				writer.writerow(writeList)

		time.sleep(8)

f.close()
writeF.close()