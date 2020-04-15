#coding: UTF-8
#pythin2.7
#activate py27
#utf-8
#chcp 65001
#pip install selenium
#python3
#pyinstaller getUS.py --onefile
# --noconsoleはしない
#https://nikkeiyosoku.com/stock_us/ranking_dy/1/から米国株情報を取得

#データを取得する
def get_param1(url):
	import time
	from selenium import webdriver
	from selenium.webdriver.chrome.options import Options
	import requests
	from bs4 import BeautifulSoup as soup

	# ブラウザのオプションを格納する変数をもらってきます。
	options = Options()

	# Headlessモードを有効にする（コメントアウトするとブラウザが実際に立ち上がります）
	options.set_headless(True)

	# chromeを起動してurlを開く
	driver = webdriver.Chrome(chrome_options=options)
	driver.get(url)

	# N秒待つ
	time.sleep(1)
	print('Please wait Nsec...')

	# ページデータを取り出す
	data = driver.page_source.encode('utf-8')
	#print(data)

	# ページデータを解析する 日付
	#doc = soup(data, 'html.parser')
	#params1 = [i for a in doc.find_all('h4') for i in a.find_all('span')]

	# ページデータを解析する 株データ
	doc = soup(data, 'html.parser')
	params = [i for a in doc.find_all(['h4','tr','span']) for i in a.find_all(['th','td','span'])]

	return params


#メイン関数
if __name__ == '__main__':
	import sys
	import io

#1 資本財
#2 ヘルスケア
#3 情報技術
#4 電気通信
#5 一般消費財
#6 公益事業
#7 金融
#8 素材
#9 不動産
#10 生活必需品
#11 エネルギー
#12 その他
	# 変換不能コードを?に置換する
	sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding=sys.stdout.encoding, errors="replace")

	print("[start]")
	print("[1]")
	url = "https://nikkeiyosoku.com/stock_us/ranking_dy/1/"		#1 資本財
	for num, link in enumerate(get_param1(url), start=1):
		print(link.text)
	print("[end]")
	print("")

	print("[start]")
	print("[2]")
	url = "https://nikkeiyosoku.com/stock_us/ranking_dy/2/"		#2 ヘルスケア
	for num, link in enumerate(get_param1(url), start=1):
		print(link.text)
	print("[end]")
	print("")

	print("[start]")
	print("[3]")
	url = "https://nikkeiyosoku.com/stock_us/ranking_dy/3/"		#3 情報技術
	for num, link in enumerate(get_param1(url), start=1):
		print(link.text)
	print("[end]")
	print("")

	print("[start]")
	print("[4]")
	url = "https://nikkeiyosoku.com/stock_us/ranking_dy/4/"		#4 電気通信
	for num, link in enumerate(get_param1(url), start=1):
		print(link.text)
	print("[end]")
	print("")

	print("[start]")
	print("[5]")
	url = "https://nikkeiyosoku.com/stock_us/ranking_dy/5/"		#5 一般消費財
	for num, link in enumerate(get_param1(url), start=1):
		print(link.text)
	print("[end]")
	print("")

	print("[start]")
	print("[6]")
	url = "https://nikkeiyosoku.com/stock_us/ranking_dy/6/"		#6 公益事業
	for num, link in enumerate(get_param1(url), start=1):
		print(link.text)
	print("[end]")
	print("")

	print("[start]")
	print("[7]")
	url = "https://nikkeiyosoku.com/stock_us/ranking_dy/7/"		#7 金融
	for num, link in enumerate(get_param1(url), start=1):
		print(link.text)
	print("[end]")
	print("")

	print("[start]")
	print("[8]")
	url = "https://nikkeiyosoku.com/stock_us/ranking_dy/8/"		#8 素材
	for num, link in enumerate(get_param1(url), start=1):
		print(link.text)
	print("[end]")
	print("")

	print("[start]")
	print("[9]")
	url = "https://nikkeiyosoku.com/stock_us/ranking_dy/9/"		#9 不動産
	for num, link in enumerate(get_param1(url), start=1):
		print(link.text)
	print("[end]")
	print("")

	print("[start]")
	print("[10]")
	url = "https://nikkeiyosoku.com/stock_us/ranking_dy/10/"	#10 生活必需品
	for num, link in enumerate(get_param1(url), start=1):
		print(link.text)
	print("[end]")
	print("")

	print("[start]")
	print("[11]")
	url = "https://nikkeiyosoku.com/stock_us/ranking_dy/11/"	#11 エネルギー
	for num, link in enumerate(get_param1(url), start=1):
		print(link.text)
	print("[end]")
	print("")

	print("[start]")
	print("[12]")
	url = "https://nikkeiyosoku.com/stock_us/ranking_dy/12/"	#12 その他
	for num, link in enumerate(get_param1(url), start=1):
		print(link.text)
	print("[end]")
	print("")

