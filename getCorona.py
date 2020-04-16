#coding: UTF-8
#pythin2.7
#activate py27
#utf-8
#chcp 65001
#
#python3
#pyinstaller exetest.py --onefile

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

	doc = soup(data, 'html.parser')
	params = [i for a in doc.find_all('div') for i in a.find_all('p') if i]
#params = [i for a in doc.find_all('div') for i in a.find_all('p')]
#scripts=[i for i in soup.find("div",{"class":"scrolling-script-container"}) if i]
	return params

if __name__ == '__main__':
	import sys
	import datetime
	import csv
	import os

	url = "https://www.asahi.com/special/corona/"

	today = datetime.date.today()
	dbgfile = "corona" + str(today.year) + ".debug.csv"
	csvfile = "corona" + str(today.year) + ".csv"

	param = get_param1(url)

	string2=list()
	
	for num, link in enumerate(param, start=1):
		#print(link.string)
		string = str(link.string)
		string = string.replace('\xa0', '')
		string = string.replace('\xa9', '')
		string2.append(string)

	f= open(dbgfile, 'a', encoding='Shift_jis')
	writer = csv.writer(f, lineterminator='\n')
	writer.writerow(string2)
	f.close()

	a= ['東京都','大阪府','神奈川県','千葉県','埼玉県','兵庫県','福岡県','愛知県','北海道','京都府','石川県','岐阜県','茨城県','福井県','群馬県',
 		'沖縄県','高知県','広島県','宮城県','富山県','静岡県','奈良県','大分県','新潟県','滋賀県','福島県','愛媛県','栃木県','山形県','山梨県','長野県',
 		'和歌山県','熊本県','山口県','青森県','三重県','宮崎県','岡山県','香川県','秋田県','長崎県','佐賀県','島根県','鹿児島県','徳島県','鳥取県','岩手県']

	h= list(range(1,49))
	d= list(range(1,49))

	for num, link in enumerate(string2, start=1):
		if num==1:
			#print(num, link)
			h[0]="日付"
			d[0]=link
		elif link in a:
			#print(num, link, string2[num], a.index(link))
			idx=a.index(link)
			h[idx+1]= link
			d[idx+1]= string2[num].replace('人', '')
		elif num > 200:
			break
	
	for num, link in enumerate(h, start=1):
		print(h[num-1], d[num-1])

	if os.path.exists(csvfile):
		f= open(csvfile, 'a', encoding='Shift_jis')
		writer = csv.writer(f, lineterminator='\n')
		writer.writerow(d)
		f.close()
	else:
		f= open(csvfile, 'a', encoding='Shift_jis')
		writer = csv.writer(f, lineterminator='\n')
		writer.writerow(h)
		writer.writerow(d)
		f.close()
