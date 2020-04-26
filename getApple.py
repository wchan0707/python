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

	# URLを設定する   yahoo!  finance アップル
	url = "https://stocks.finance.yahoo.co.jp/us/detail/AAPL"

	# ファイル名を設定する
	today = datetime.date.today()
	dbgfile = "Stock" + str(today.year) + ".debug.csv"
	csvfile = "Stock" + str(today.year) + ".csv"

	# オプションを設定する
	options = Options()
	options.set_headless(False)		#True: 画面表示なし

	# Chromeを起動
	driver = webdriver.Chrome(chrome_options=options)

	# URLを開く
	wait= 3
	driver.get(url)
	time.sleep(wait)
	print('Please wait', wait, 'sec...')
	data = driver.page_source.encode('utf-8')
	doc = soup(data, 'html.parser')

	# パラメータを収集する
	tbls= [
		 ['市場', 			'.stockMainTabName']
		,['業種',			'.category']
		,['銘柄コード',		'.stocksInfo > dt']
		,['銘柄名',			'h1']
		,['日付',			'.yjSb > span']
		,['日時',			'.real']
		,['株価',			'.stoksPrice:nth-child(3)']
		,['前日比',			'.icoUpGreen']
		,['前日終値',		'.innerDate > .lineFi:nth-child(1) strong']
		,['始値',			'.innerDate > .lineFi:nth-child(2) strong']
		,['高値',			'.innerDate > .lineFi:nth-child(3) strong']
		,['安値',			'.innerDate > .lineFi:nth-child(4) strong']
		,['出来高',			'.innerDate > .lineFi:nth-child(5) strong']
		,['売買代金',		'.innerDate > .lineFi:nth-child(6) strong']
		,['時価総額',		'.yjMS:nth-child(1) strong']
		,['発行済株式数',	'.yjMS:nth-child(2) > .tseDtlDelay strong']
		,['PER',			'.yjMS:nth-child(3) strong']
		,['PBR',			'.yjMS:nth-child(4) strong']
		,['EPS',			'.yjMS:nth-child(5) strong']
		,['BPS',			'.yjMS:nth-child(6) strong']
		,['52週高値',		'.lineFi:nth-child(7) strong']
		,['52週安値',		'.lineFi:nth-child(8) strong']
	]

	h = list()			# ヘッダー行
	d = list()			# データ行

	for num, tbl in enumerate(tbls, start=1):
		params = doc.select(tbl[1])
		if params:
			text= params[0].text
			if tbl[0]=='PER' or tbl[0]=='PBR'or tbl[0]=='EPS' or tbl[0]=='BPS':
				 text= text.replace('(連)', '')
			print(tbl[0], '[[[', text, ']]]')
			h.append(tbl[0])
			d.append(text)

	# Chromeを閉じる
	driver.close()

	# Csvファイルが存在するかチェックする
	exists= os.path.exists(csvfile)

	# Csvファイルに保存する
	f= open(csvfile, 'a', encoding='Shift_jis')
	writer = csv.writer(f, lineterminator='\n')
	if exists == False:
		writer.writerow(h)		# 新規作成時はヘッダ行を追加する
	writer.writerow(d)			# データ行追加
	f.close()
