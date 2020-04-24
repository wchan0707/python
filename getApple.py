#coding: UTF-8
if __name__ == '__main__':
	import time
	from selenium import webdriver
	from selenium.webdriver.chrome.options import Options
	import requests
	from bs4 import BeautifulSoup as soup
	from selenium.webdriver.common.keys import Keys
	import sys
	import datetime
	import csv
	import os

	#URLを設定する   yahoo!  finance アップル
	url = "https://stocks.finance.yahoo.co.jp/us/detail/AAPL"

	#ファイル名を設定する
	today = datetime.date.today()
	dbgfile = "Apple" + str(today.year) + ".debug.csv"
	csvfile = "Apple" + str(today.year) + ".csv"

	options = Options()

	options.set_headless(False)		#True: 画面表示なし

	#Chromeを起動
	driver = webdriver.Chrome(chrome_options=options)

	#URLを開く
	driver.get(url)
	time.sleep(3)
	print('Please wait 3sec...')

	data = driver.page_source.encode('utf-8')

	doc = soup(data, 'html.parser')

	params = [i for a in doc.find_all('dl') for i in a.find_all('dt') if i]
	string2=list()

	for num, link in enumerate(params, start=1):
#		print(num, '[[[', link.text, ']]]')
		print(num, '[[[', link.text.split('\n')[0], ']]]')
#		print('[[[', link.string, ']]]')
		string = str(link.string)
		string = string.replace('\xa0', '')
		string = string.replace('\xa9', '')
		string2.append(string)

	print()
	print()
	print()

	params = [i for a in doc.find_all('dd') for i in a.find_all('strong') if i]

	string2=list()
		
	for num, link in enumerate(params, start=1):
#		print(num, '[[[', link.text, ']]]')
		print(num, '[[[', link.string, ']]]')
		string = str(link.string)
		string = string.replace('\xa0', '')
		string = string.replace('\xa9', '')
		string2.append(string)

	print()
	print()
	print()

	params = [i for i in doc.find_all("dt",{"class":"title"}) if i]
	string2=list()

	for num, link in enumerate(params, start=1):
#		print('[[[', link.text, ']]]')
		print(num, '[[[', link.text.split('\n')[0], ']]]')
#		print('[[[', string.split('>')[-1].split('<a')[0], ']]]')
#		print('[[[', link.string, ']]]')
		string = str(link.string)
		string = string.replace('\xa0', '')
		string = string.replace('\xa9', '')
		string2.append(string)

	driver.close()

#		if os.path.exists(csvfile):
#			f= open(csvfile, 'a', encoding='Shift_jis')
#			writer = csv.writer(f, lineterminator='\n')
#			writer.writerow(d)
#			f.close()
#		else:
#			f= open(csvfile, 'a', encoding='Shift_jis')
#			writer = csv.writer(f, lineterminator='\n')
#			writer.writerow(h)
#			writer.writerow(d)
#			f.close()

