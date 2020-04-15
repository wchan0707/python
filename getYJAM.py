#coding: UTF-8
#pythin2.7
#activate py27
#utf-8
#chcp 65001
#
#python3
#

def get_param1(url):
	import requests
	from bs4 import BeautifulSoup as soup
	result = requests.get(url)
	page = result.text
	doc = soup(page, 'html.parser')
	params = [i for a in doc.find_all('tr') for i in a.find_all('th')]
	return params

def get_param2(url):
	import requests
	from bs4 import BeautifulSoup as soup
	result = requests.get(url)
	page = result.text
	doc = soup(page, 'html.parser')
	params = [i for a in doc.find_all('td') for i in a.find_all('span')]
	return params

if __name__ == '__main__':
	import sys
	import datetime
	import csv

	url = "http://t2.jiji.com/linkbox?area=null&FWCS=bear&pageID=LB2031_FUND_SUMMARY&userID=iyo-bk&fcode=9731116C"

	today = datetime.date.today()
	csvfile = "yjam" + str(today.year) + ".csv"

	param = get_param1(url)
	string2 = list()

	for num, link in enumerate(param, start=1):
		print(link.string)
		string = str(link.string)
		string = string.replace('\xa0', '')
		string = string.replace('\xa9', '')
		string2.append(string)

	with open(csvfile, 'a', encoding='Shift_jis') as f:	
		writer = csv.writer(f, lineterminator='\n')
		writer.writerow(string2)
		f.close()

	param = get_param2(url)
	string2 = list()

	for num, link in enumerate(param, start=1):
		print(link.string)
		string = str(link.string)
		string = string.replace('\xa0', '')
		string = string.replace('\xa9', '')
		string2.append(string)

	with open(csvfile, 'a', encoding='Shift_jis') as f:	
		writer = csv.writer(f, lineterminator='\n')
		writer.writerow(string2)
		f.close()
