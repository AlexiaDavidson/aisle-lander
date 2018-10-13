import csv

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
	    		recipe = {'name':row['name'],
	    				   'ingredients': list_parser(row['ingredients']),
	    				   'steps': row['steps'],
	    				   'total_time': row['total_time'],
	    				   'servings': row['servings']
	    				   }
	    		rec_list.append(recipe)
	return rec_list

def search_by_name(name):
	with open("recipes.csv") as f:
	    reader = csv.DictReader(f)
	    for row in reader:
	    	if name in row['ingredients']: 
	    		print(row['name'] )

def retrieve_product(prod):
	rec_list = []
	with open("products.csv") as fh:
	    reader = csv.DictReader(fh)
	    for row in reader:	 
	    	print(row["quantity"])   	
	    	if prod in row['name']: 
	    		print(row['quantity'])
	    		rec_list.append(row)
	return rec_list
recipes = search_by_ingredient(in1)
recipe = recipes[0]
#products = retrieve_product()
#product_details = products[0]
product_list = retrieve_product("Beef")
# for i in product_list:
# 	print(i)

print(recipe['ingredients'][0])

#product = {'name':row['name'],'price':row['price'],'quantity':row['quantity']}
#p_details.append(product)