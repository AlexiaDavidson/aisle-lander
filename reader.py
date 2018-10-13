import csv
import random

in1 = "egg"
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

def random_recipe():
	rec_list = []
	with open("recipes.csv") as f:
	    reader = csv.DictReader(f)
	    for row in reader:
	    	row['ingredients'] = list_parser(row['ingredients'])
	    	row['steps'] = list_parser(row['steps'])
	    	rec_list.append(row)
	ran_num = random.randint(0, (len(rec_list)-1))
	return rec_list[ran_num]


def retrieve_product():
	p_details = []
	p_list = []
	with open("products.csv") as fh:
	    reader = csv.DictReader(fh)	    
	    for row in reader:
	    	p_list.append(row['name'])
	    	p_details.append(row)
	return p_list, p_details

recipes = search_by_ingredient(in1)
recipe = recipes[0]
product_list, product_details = retrieve_product()
# product_details = products[0]
# product_list = products[1]
# for i in product_list:
# 	print(i)
rand_rec = random_recipe()
#print(rand_rec["name"])
print(recipe['steps'][0])

#product = {'name':row['name'],'price':row['price'],'quantity':row['quantity']}
#p_details.append(product)