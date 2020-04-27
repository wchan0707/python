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

	# URLを設定する   みんかぶ　日経平均株価
	url = "https://minkabu.jp/stock/100000018"

	# ファイル名を設定する
	today = datetime.date.today()
	dbgfile = "MN_Nikkei" + str(today.year) + ".debug.csv"
	csvfile = "MN_Nikkei" + str(today.year) + ".csv"

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
		 ['市場', 		'.ly_col > .stock_label']
		,['日時',		'.ico_calendar']
		,['銘柄名',		'.md_stockBoard_stockName']
		,['株価',		'.stock_price']
		,['前日比',		'.stock_price_diff > .up']
		,['始値',		'.ly_col:nth-child(1) > .md_list > .ly_vamd:nth-child(1) > .ly_colsize_9_fix']
		,['高値',		'.ly_col:nth-child(1) > .md_list > .ly_vamd:nth-child(2) > .ly_colsize_9_fix']
		,['安値',		'.ly_col:nth-child(1) > .md_list > .ly_vamd:nth-child(3) > .ly_colsize_9_fix']
	]

	h = list()			# ヘッダー行
	d = list()			# データ行

	for num, tbl in enumerate(tbls, start=1):
		params = doc.select(tbl[1])
		if params:
			text= params[0].text
			text= text.replace('\xa0', '')
			text= text.replace('\xa9', '')
			text= text.replace('\n', '')
			text= text.strip(' ')
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
