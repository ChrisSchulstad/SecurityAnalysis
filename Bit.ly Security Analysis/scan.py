import requests
from bs4 import BeautifulSoup
import lxml
import random
import string
import csv
import time
from selenium import webdriver


oSite = "https://sitecheck.sucuri.net/results/"

f = open('URL.csv', 'r')
reader = csv.reader(f)

for row in reader:	

	newrow = [0, "{{ratingBarPosition}}"]

	while (newrow[1] == "{{ratingBarPosition}}"):

		ff = open('vuln.csv', 'a', newline='')
		writer = csv.writer(ff)

		browser = webdriver.Chrome()

		shorten = row[0]

		site = oSite + str((row[7])[7:])

		browser.get(site)
		time.sleep(6)
		innerHTML = browser.execute_script("return document.body.innerHTML")
		time.sleep(6)
		soup = BeautifulSoup(innerHTML)
	
		temp = soup.encode('utf-8')
		temp = temp[5500:]
		temp = temp[:-10000]
		new = str(temp)
		new = new.replace(' ', '')
		new = new.replace(':', '\n')
		new = new.replace(';', '\n')
		print("\n")
	
		time.sleep(1)

		severity = 0
		temp = ""
		lock = 0
		for char in new:
			if (char == '\n'):
				temp = ""
			elif (char == '%' and lock == 0):
				severity = temp
				lock = 1
				new = ""
			else:
				temp += char
	
		temp = soup.encode('utf-8')
		new = str(temp)
		new = new.replace(' ', '')
		new = new.replace('.', '\n')
		new = new.replace('<', '\n')
		fof = 1 # 0 if the website is down (404)
		temp = ""
		for char in new:
			if (char == '\n'):
				if (temp == "404NOTFOUND"):
					fof = 0
					new = ""
				temp = ""
			else:
				temp += char


		temp = soup.encode('utf-8')
		temp = temp[5000:]
		temp = temp[:-5000]
		new = str(temp)
		new = new.replace('\n', '')
		new = new.replace('<', '\n')
		new = new.replace('>', '\n')
		new = new.replace(':', '\n')

		google = int(0)
		norton = int(0)
		mcafee = int(0)
		sucuri = int(0)
		eset = int(0)
		phishtank = int(0)
		yandex = int(0)
		opera = int(0)
		spamhaus = int(0)
		temp = ""
		for char in new:
			if (char == '\n'):
				if (temp == "Domain blacklisted by Google Safe Browsing"):
					google = 1
				elif (temp == "Domain blacklisted by Norton Safe Web"):
					norton = 1
				elif (temp == "Domain blacklisted by McAfee"):
					mcafee = 1
				elif (temp == "Domain blacklisted by Sucuri Labs"):
					sucuri = 1
				elif (temp == "Domain blacklisted by ESET"):
					eset = 1
				elif (temp == "Domain blacklisted by PhishTank"):
					phishtank = 1
				elif (temp == "Domain blacklisted by Yandex"):
					yandex = 1
				elif (temp == "Domain blacklisted by Opera"):
					opera = 1
				elif (temp == "Domain blacklisted by Spamhaus"):
					spamhaus = 1
				temp = ""
			else:
				temp += char
	

		temp = soup.encode('utf-8')
		temp = temp[4500:]
		temp = temp[:-10000]
		new = str(temp)
		new = new.replace('\n', '')
		new = new.replace('<', '\n')
		new = new.replace('>', '\n')
		ip = ""
		temp = ""
		record = 0
		lock = 0
		for char in new:
			if (char == '\n'):
				if (temp == "IP address:"):
					record = 1
				elif (record == 1 and temp == "span"):
					record = 2
				elif (record == 2 and lock == 0):
					ip = temp
					record = 3
					lock = 1
					new = ""
				temp = ""
			else:
				temp += char

		time.sleep(1)

		#hash, securityScore, bitlySecurityTag, numCLicks, creationTime, isActive, ipAddress, google, norton, mcafee, sucuri, eset, phishTank, yandex, opera, spamHaus, longURL
		newrow = [shorten[2:][:-2], severity, row[1], row[6], row[2], fof, ip, google, norton, mcafee, sucuri, eset, phishtank, yandex, opera, spamhaus, (row[7])[7:]]	

	writer.writerow(newrow)
	print(newrow)

	time.sleep(1)
	ff.close()

	browser.quit()
	