from flask import Flask, render_template, request, redirect, url_for
import requests
import json

app = Flask(__name__)

@app.route('/') #Renders the index.html page with all the contents of the database included.
def render():
    req = requests.get('http://127.0.0.1:5000/api/inventory/all')
    data = req.json()
    return render_template('index.html', value = data)

@app.route('/search')   #Sends a GET request to the API to find a specific ID and returns the results in a table.
def input():
    id = request.args['id']
    req = requests.get('http://127.0.0.1:5000/api/inventory?id=' + id)
    data = req.json()
    return render_template('index.html', value = data)

@app.route('/delete')   #Sends a DELETE request to the API for a particular id.
def delete():
    id = request.args['id']
    requests.delete('http://127.0.0.1:5000/api/inventory/delete?id=' + id)
    return redirect(url_for('render'));

@app.route('/add', methods=['POST'])    #Sends an add request to the API with form information from the web UI.
def add():
    name = request.form.get('name')
    price = request.form.get('price')
    stock = request.form.get('stock')
    if (price.replace('.','',1).isdigit() and stock.isdigit()):   #Check to see if the input values are correct.
        obj = {'name' : name, 'price' : price, 'stock' : stock}
        requests.post('http://127.0.0.1:5000/api/inventory/add', data = obj)
        return redirect(url_for('render'))
    else:   
        req = requests.get('http://127.0.0.1:5000/api/inventory/all')
        data = req.json()
        return render_template('input_error.html', value = data)    #Renders a template that informs user that input is invalid.


if __name__=='__main__':
    app.run(debug=False,port=int('5001'))
    
