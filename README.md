# SecurityAnalysis

*** Step by step instructions for running these programs and generating your own data ***

**********
Important: 

In our paper, we explored our 4 step system. We have cleaned up our programs, and all data is now generated in 3 steps. 
”centralize.py” and ”ﬁnal.csv” have been removed from our solution.

If URL.csv and hashes.csv aren't automatically created, then you may need create them. They are empty csv files.

**********

1. Make sure you have Python up to date. Use Python Pip to install Requests and Selenium.

2. Run getHashes.py (this will populate hashes.csv, and it will print generated hashes to the console).
	*** Gather all desired hashes before proceeding to the next step to prevent duplicating hashes

3. Run crawl.py (this will populate URL.csv, and will print the Bit.ly analytics to the console).
	*** This does NOT remove hashes from hashes.csv. If you intend on pausing and resuming, then 
	you must remove the hashes that have already been crawled from hashes.csv.

4. Run scan.py (this will populate vuln.csv, which is the final data file).
	*** Like crawl.py, this does NOT remove websites from URL.csv. Follow the same protocol if needed.
	***	vuln.csv should have a header built in. If you accidently delete it, then here is a copy:

hash, securityScore, bitlySecurityTag, numCLicks, creationTime, isActive, ipAddress, google, norton, mcafee, sucuri, eset, phishTank, yandex, opera, spamHaus, longURL

Feel free to speed up these scans with Virtual machines. Note that Bit,ly limits HTTP requests to roughly 1 thousand per hour.
