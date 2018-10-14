from flask import Flask, render_template, url_for, redirect
import reader
import random

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.htm')

@app.route('/recipedisplay')
def recipedisplay():
	return render_template('RecipeDisplay.htm',  recipe= reader.recipe, products = reader.las_details, product_name = reader.las_list)

@app.route('/shoppinglist')
def shoppinglist():
	prods = reader.product_details
	return render_template("ShoppingList.htm", products = prods )

@app.route('/surpriseme')
def surpriseme():
	num = reader.nb_recipes
	ran_num = random.randint(0, (num-1))
	return render_template('SurpriseMe_RecipeDisplay.htm',  recipe= reader.random_recipe(ran_num), products = reader.product_details, product_name = reader.product_list)

@app.route('/search')
def search():
	return render_template('RecipeSearch.htm',  recipe= reader.recipes, product_name = reader.product_list)

