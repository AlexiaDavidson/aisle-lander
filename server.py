from flask import Flask, render_template
import reader

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
	return render_template('RecipeDisplay1.htm',  recipe= reader.recipe)
