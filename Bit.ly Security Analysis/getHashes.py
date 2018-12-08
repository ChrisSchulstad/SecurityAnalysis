import requests
import bs4
import lxml
import random
import string
import csv

def random_generator(size=4, chars=string.ascii_letters + string.digits):
	return ''.join(random.choice(chars) for x in range(size))

while(True):

	hash4 = random_generator(4)
	hash5 = random_generator(5)
	hash6 = random_generator(6)

	post4 = True
	post5 = True
	post6 = True
	f = open('hashes6.csv', 'r')
	reader = csv.reader(f)
	for row in reader:		
		if (row[0] == hash4):
			post4 = False
		if (row[0] == hash5):
			post5 = False
		if (row[0] == hash6):
			post6 = False
	f.close()

	f = open('hashes.csv', 'a', newline='')
	writer = csv.writer(f)
	if (post4 == True):
		writer.writerow([hash4])
		print (hash4)
	else:
		print ('not writing: ' + hash4)
	if (post5 == True):
		writer.writerow([hash5])
		print (hash5)
	else:
		print ('not writing: ' + hash5)
	if (post6 == True):
		writer.writerow([hash6])
		print (hash6)
	else:
		print ('not writing: ' + hash6)
	f.close()