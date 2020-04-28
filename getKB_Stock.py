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

	# URLを設定する   株探　ソフトバンク
	url = "https://kabutan.jp/stock/?code=9434"

	# ファイル名を設定する
	today = datetime.date.today()
	dbgfile = "KB_Stock" + str(today.year) + ".debug.csv"
	csvfile = "KB_Stock" + str(today.year) + ".csv"

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
		 ['市場', 		'.market']
		,['日付',		'h2 > time']
		,['銘柄名',		'.si_i1_1 > h2']
		,['株価',		'.kabuka']
		,['前日比',		'dd:nth-child(2) > .down']
		,['始値',		'#kobetsu_left > table:nth-child(3) tr:nth-child(1) > td:nth-child(2)']
		,['高値',		'#kobetsu_left > table:nth-child(3) tr:nth-child(2) > td:nth-child(2)']
		,['安値',		'table:nth-child(3) tr:nth-child(3) > td:nth-child(2)']
		,['終値',		'table:nth-child(3) tr:nth-child(4) > td:nth-child(2)']
		,['業種', 		'#stockinfo_i2 a']
		,['PER', 		'table:nth-child(1) > tbody:nth-child(2) td:nth-child(1)']
		,['PBR', 		'table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2)']
		,['利回り', 	'table:nth-child(1) > tbody:nth-child(2) td:nth-child(3)']
		,['信用倍率', 	'table:nth-child(1) > tbody:nth-child(2) td:nth-child(4)']
		,['出来高', 	'table:nth-child(4) tr:nth-child(1) > td']
		,['売買代金', 	'table:nth-child(4) tr:nth-child(2) > td']
		,['VWAP', 		'table:nth-child(4) tr:nth-child(3) > td']
		,['約定回数', 	'table:nth-child(4) tr:nth-child(4) > td']
		,['売買最低代金', 'table:nth-child(4) tr:nth-child(5) > td']
		,['単元株数', 	'tr:nth-child(6) > td:nth-child(2)']
		,['時価総額', 	'tr:nth-child(7) > td']
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
