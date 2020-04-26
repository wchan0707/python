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

	#オプションを設定する
	options = Options()
	options.set_headless(False)		#True: 画面表示なし

	#Chromeを起動
	driver = webdriver.Chrome(chrome_options=options)

	#URLを開く
	wait= 3
	driver.get(url)
	time.sleep(wait)
	print('Please wait', wait, 'sec...')
	data = driver.page_source.encode('utf-8')
	doc = soup(data, 'html.parser')

	#パラメータを収集する
	prmtnl= [
		 ['市場', 			'#main > div.stockMainTab.clearFix > div.stockMainTabParts.stockMainTabPartsCurrent > span']
		,['業種',			'#main > div.stocksDtlWp > div > div.forAddPortfolio > dl > dd.category.yjSb']
		,['銘柄コード',		'#main > div.stocksDtlWp > div > div.forAddPortfolio > dl > dt']
		,['銘柄名',			'#main > div.stocksDtlWp > div > div.forAddPortfolio > table > tbody > tr > th > h1']
		,['日時',			'#main > div.stocksDtlWp > div > div.forAddPortfolio > dl > dd.yjSb.real']
		,['株価',			'#main > div.stocksDtlWp > div > div.forAddPortfolio > table > tbody > tr > td:nth-child(3)']
		,['前日比',			'#main > div.stocksDtlWp > div > div.forAddPortfolio > table > tbody > tr > td.change > span.icoUpGreen.yjMSt']
		,['前日終値','#main > div.marB2.chartFinance.clearFix > div.innerDate > div:nth-child(1) > dl > dd > strong']
		,['始値','']
		,['高値','']
		,['出来高','']
		,['売買代金','']
		,['時価総額','']
		,['発行済株式数','']
		,['','']
		,['','']
		,['','']
		,['','']
		,['','']
	]

	for num, link in enumerate(prmtnl, start=1):
			params = doc.select(link[1])
			print(link[0], '[[[', params[0].text, ']]]')

	print()
	print()
	print()

	# Chromeを閉じる
	driver.close()

	#Csvファイルに保存する
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

