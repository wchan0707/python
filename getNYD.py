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

	# URLを設定する   yahoo!  finance 日経平均株価
	url = "https://finance.yahoo.co.jp/quote/%5EDJI"

	# ファイル名を設定する
	today = datetime.date.today()
	dbgfile = "NYD" + str(today.year) + ".debug.csv"
	csvfile = "NYD" + str(today.year) + ".csv"

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
		 ['市場', 			'.Nv8MV3cw']
		,['銘柄名',			'.Pz3gXPTn']
		,['株価',			'.wlbmIy9W > .\_3BGK5SVf']
		,['前日比',			'.St6PBOuj .\_3BGK5SVf']
		,['前日終値',		'.\_1fLThPxD:nth-child(1) .\_3BGK5SVf']
		,['始値',			'.\_1fLThPxD:nth-child(2) .\_3BGK5SVf']
		,['高値',			'.\_1fLThPxD:nth-child(3) .\_3BGK5SVf']
		,['安値',			'.\_1fLThPxD:nth-child(4) .\_3BGK5SVf']
		,['出来高',			'.\_1fLThPxD:nth-child(5) .\_3BGK5SVf']
		,['52週高値',		'.\_1fLThPxD:nth-child(6) .\_3BGK5SVf']
		,['52週安値',		'.\_1fLThPxD:nth-child(7) .\_3BGK5SVf']
	]

	h = list()			# ヘッダー行
	d = list()			# データ行

	for num, tbl in enumerate(tbls, start=1):
		params = doc.select(tbl[1])
		if params:
			text= params[0].text
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
