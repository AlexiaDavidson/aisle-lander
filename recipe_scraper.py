import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from datetime import datetime
import csv

quote_page = 'https://www.allrecipes.com/recipe/25037/best-big-fat-chewy-chocolate-chip-cookie/?internalSource=hub%20recipe&referringId=362&referringContentType=Recipe%20Hub'
#quote_page = "https://www.allrecipes.com/recipe/233661/chef-johns-lasagna/?internalSource=hub%20recipe&referringContentType=Search"
page = urllib.request.urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')
name_box = soup.find("h1", {"class": "recipe-summary__h1"})
name = name_box.text.strip() # strip() is used to remove starting and trailing
print (name)
recipe = {"name": name,
		"ingredients": [],
		"steps": []
		#"total_time": total_time
				}
ingredients = soup.findAll("li", {"class": "checkList__line"})
steps = soup.findAll("span", {"class": "recipe-directions__list--item"})
for ingredient in ingredients:
	str_ing = ingredient.find("span", {"class": "recipe-ingred_txt"}).get_text()
	if str_ing and str_ing != "Add all ingredients to list":
		str_ing = str_ing.replace(",", "-")
		recipe['ingredients'].append(str_ing)
for step in steps:
	str_step = step.get_text()
	if str_step:
		recipe['steps'].append(str_step)

with open('index.csv', 'a') as csv_file:
 w = csv.DictWriter(csv_file, recipe.keys())
 w.writeheader()
 w.writerow(recipe)



