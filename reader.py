import csv

in1 = "egg"
def list_parser(ing_list):
	final_list= []
	individual = ''
	for i in ing_list:
		if ((i == '[') or (i ==']')):
			pass
		if (i == ","):
			individual = individual.replace("[", "")
			individual = individual.replace("]", "")
			final_list.append(individual)
			individual = ''
		else:
			individual += str(i)
	return final_list
	
def search_by_ingredient(ingredient):
	rec_list = []
	with open("index.csv") as f:
	    reader = csv.DictReader(f)
	    for row in reader:
	    	if ingredient in row['ingredients']: 
	    		recipe = {'name':row['name'],
	    				   'ingredients': list_parser(row['ingredients']),
	    				   'steps': row['steps']}
	    		rec_list.append(recipe)
	return rec_list

def search_by_name(name):
	with open("index.csv") as f:
	    reader = csv.DictReader(f)
	    for row in reader:
	    	if name in row['ingredients']: 
	    		print(row['name'] )

recipes = search_by_ingredient(in1)
recipe = recipes[1]

for i in recipes:
	print(i['name'])

print(recipe['ingredients'][0])