from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/products')
def get_products():
    with open('products.json') as f:
        products = json.load(f)
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True)
