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

	# URLを設定する   田中貴金属工業　貴金属価格情報
	url = "https://gold.tanaka.co.jp/commodity/souba/"

	# ファイル名を設定する
	today = datetime.date.today()
	dbgfile = "Gold" + str(today.year) + ".debug.csv"
	csvfile = "Gold" + str(today.year) + ".csv"

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

	pdcts= ['.gold', '.pt', '.silver']
	
	# 収集するパラメータを設定する
	for pdct in enumerate(pdcts, start=1):
		print('<<<', str(pdct[1]), '>>>')
		tbls= [
			 ['日時',				'h3:nth-child(4) > span']
			,['銘柄名',				pdct[1] + ' > .metal_name']
			,['税込小売価格',		pdct[1] + ' > .retail_tax:nth-child(2)']
			,['小売価格前日比',		pdct[1] + ' > .retail_ratio']
			,['税込買取価格',		pdct[1] + ' > .purchase_tax']
			,['買取価格前日比',		pdct[1] + ' > .purchase_ratio']
		]

		h = list()			# ヘッダー行
		d = list()			# データ行

		# パラメータを収集する
		for num, tbl in enumerate(tbls, start=1):
			params = doc.select(tbl[1])
			if params:
				text= params[0].text
				text= text.replace('\xa0', '')
				text= text.replace('\xa9', '')
				text= text.replace('\n', '')
				text= text.strip(' ')
				print(tbl[0], '[[[', text, ']]]')
				h.append(tbl[0])
				d.append(text)

		# Csvファイルが存在するかチェックする
		exists= os.path.exists(csvfile)

		# Csvファイルに保存する
		f= open(csvfile, 'a', encoding='Shift_jis')
		writer = csv.writer(f, lineterminator='\n')
		if exists == False:
			writer.writerow(h)		# 新規作成時はヘッダ行を追加する
		writer.writerow(d)			# データ行追加
		f.close()

# Chromeを閉じる
driver.close()

