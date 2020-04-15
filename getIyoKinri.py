#coding: UTF-8
#pythin2.7
#activate py27
#utf-8
#chcp 65001
#
#python3
#
#pyinstaller getIyoKinri.py --onefile
def get_param1(url):
	import time
	from selenium import webdriver
	from selenium.webdriver.chrome.options import Options
	import requests
	from bs4 import BeautifulSoup as soup

	options = Options()

	options.set_headless(True)

	driver = webdriver.Chrome(chrome_options=options)
	driver.get(url)

	time.sleep(3)
	print('Please wait 3sec...')

	data = driver.page_source.encode('utf-8')
	#print(data)

	doc = soup(data, 'html.parser')
	params = [i for a in doc.find_all('tr') for i in a.find_all('td')]
	return params

if __name__ == '__main__':
	import sys
	import datetime
	import csv

	url = "https://www.iyobank.co.jp/kinri-gaikokukawasesoba-market/kojinloankinri.html"

	today = datetime.date.today()
	csvfile = "iyokinri" + str(today.year) + ".csv"

	param = get_param1(url)
	
	string2 = list()

	for num, link in enumerate(param, start=1):
		print(link.string)
		string = str(link.string)
		string = string.replace('\xa0', '')
		string = string.replace('\xa9', '')
		string = string.replace('\uff5e', '')
		string2.append(string)

	with open(csvfile, 'a', encoding='Shift_jis') as f:	
		writer = csv.writer(f, lineterminator='\n')
		writer.writerow(string2)
		f.close()
