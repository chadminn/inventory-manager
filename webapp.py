from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def render():
    req = requests.get('http://127.0.0.1:5000/api/inventory/all')
    data = req.json()
    return render_template('index.html', value = data)

@app.route('/search')
def input():
    id = request.args['id']
    req = requests.get('http://127.0.0.1:5000/api/inventory?id=' + id)
    data = req.json()
    return render_template('index.html', value = data)

@app.route('/delete')
def delete():
    id = request.args['id']
    requests.delete('http://127.0.0.1:5000/api/inventory/delete?id=' + id)
    return render();

@app.route('/add', methods=['POST'])
def add():
    name = request.form.get('name')
    price = request.form.get('price')
    stock = request.form.get('stock')
    obj = {'name' : name, 'price' : price, 'stock' : stock}
    requests.post('http://127.0.0.1:5000/api/inventory/add', data = obj)
    return render()

