import csv
import random

in1 = "egg"
def num_recipes():
	counter = 0
	with open("recipes.csv") as f:
	    reader = csv.DictReader(f)
	    for row in reader:
	    	 counter += 1
	return counter
def list_parser(ing_list):
	final_list= []
	individual = ''
	punct = '[]\''
	for i in ing_list:
		if ((i == '[') or (i ==']')):
			pass
		if (i == ","):
			for pun in punct:
				individual = individual.replace(pun, "")
			final_list.append(individual)
			individual = ''
		else:
			individual += str(i)
	return final_list
	
def search_by_ingredient(ingredient):
	rec_list = []
	with open("recipes.csv") as f:
	    reader = csv.DictReader(f)
	    for row in reader:
	    	if ingredient in row['ingredients']:
	    		row['ingredients'] = list_parser(row['ingredients'])
	    		row['steps'] = list_parser(row['steps']) 	    		
	    		rec_list.append(row)
	return rec_list

def search_by_name(name):
	with open("recipes.csv") as f:
	    reader = csv.DictReader(f)
	    for row in reader:
	    	if name in row['ingredients']: 
	    		print(row['name'] )

def random_recipe(num):
	rec_list = []
	with open("recipes.csv") as f:
	    reader = csv.DictReader(f)
	    for row in reader:
	    	row['ingredients'] = list_parser(row['ingredients'])
	    	row['steps'] = list_parser(row['steps'])
	    	rec_list.append(row)
	return rec_list[num]


def retrieve_product():
	p_details = []
	p_list = []
	with open("products.csv") as fh:
	    reader = csv.DictReader(fh)	    
	    for row in reader:
	    	p_list.append(row['name'])
	    	p_details.append(row)
	return p_list, p_details

nb_recipes = num_recipes()
recipes = search_by_ingredient(in1)
recipe = recipes[0]
product_list, product_details = retrieve_product()
