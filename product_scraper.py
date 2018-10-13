import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from datetime import datetime
import csv
from urllib.request import Request

#page = 'https://www.fairprice.com.sg/product/kellys-bockwurst-sausage-200g-11608417'
#page= 'https://www.fairprice.com.sg/FPProductDisplay?storeId=10151&productId=3074457345617129659&urlRequestType=Base&langId=-1&catalogId=10201'
page = 'https://www.fairprice.com.sg/product/seng-choon-large-eggs-10s-630g-13104178'

def scrape(quote_page):
	req = Request(quote_page, headers={'User-Agent': 'Mozilla/5.0'})
	page = urllib.request.urlopen(req).read()
	soup = BeautifulSoup(page, 'html.parser')
	name_box = soup.find("h1", {"class": "pdt_Pname"}).getText().strip()
	quantity = soup.find("span", {"class": "pdt_weightMg"}).getText().strip()
	price = soup.find("span", {"class": "pdt_C_price"}).getText().strip()
	print(name_box, quantity, price)
	product = {	"name": name_box,
				"quantity": quantity,
				"price": price
				}
	with open('products.csv', 'a') as csv_file:
	 w = csv.writer(csv_file)
	 #w.writerow(["name", "quantity", "price"])
	 w.writerow([name_box,quantity, price])

# 	with open('products.csv', 'a') as csv_file:
# 	 w = csv.DictWriter(csv_file, product.keys())
# 	 w.writeheader()
# 	 w.writerow(product)

scrape(page)