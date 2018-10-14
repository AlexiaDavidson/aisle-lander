import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from datetime import datetime
import csv
from urllib.request import Request

#Scrapes product information from fairprice supermarket's website
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

f = open('products_links.txt', 'r')
url_list = [] 
for line in f:
    url_list.append(line.strip())

for i in range(len(url_list)):
	scrape(url_list[i])
