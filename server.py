from flask import Flask, render_template
import reader

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('RecipeDisplay.htm',  recipe= reader.rand_rec, products = reader.product_details, product_name = reader.product_list)

@app.route('/shoppinglist')
def shoppinglist():
	prods = reader.product_details
	return render_template("ShoppingList.htm", products = prods )
