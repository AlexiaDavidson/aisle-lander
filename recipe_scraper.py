import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from datetime import datetime
import csv

def scrape(quote_page):
	page = urllib.request.urlopen(quote_page)
	soup = BeautifulSoup(page, 'html.parser')
	name_box = soup.find("h1", {"class": "recipe-summary__h1"})
	name = name_box.text.strip() # strip() is used to remove starting and trailing
	servings_html = soup.find("meta", {'id': 'metaRecipeServings'})
	servings = servings_html['content']
	total_time = soup.find('span', {'class': 'ready-in-time'}).get_text()
	print (name)

	ingredients = soup.findAll("li", {"class": "checkList__line"})
	ingredients_list = []
	steps = soup.findAll("span", {"class": "recipe-directions__list--item"})
	steps_list = []

	for ingredient in ingredients:
		str_ing = ingredient.find("span", {"class": "recipe-ingred_txt"}).get_text().strip()
		if str_ing and str_ing != "Add all ingredients to list":
			str_ing = str_ing.replace(",", "-")
			ingredients_list.append(str_ing)
	for step in steps:
		str_step = step.get_text().strip()
		if str_step:
			steps_list.append(str_step)

	with open('recipes.csv', 'a') as csv_file:
	 w = csv.writer(csv_file)
	 #w.writerow(["name", "ingredients", "steps", "total_time", "servings"])
	 w.writerow([name,ingredients_list, steps_list, total_time, servings])
	# with open('recipes.csv', 'a') as csv_file:
	#  w = csv.DictWriter(csv_file, recipe.keys())
	#  w.writeheader()
	#  w.writerow(recipe)
f = open('recipe_links.txt', 'r')
url_list = [] 
for line in f:
    url_list.append(line.strip())

for i in range(len(url_list)):
	scrape(url_list[i])




