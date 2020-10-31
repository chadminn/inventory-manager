import sqlite3
import json
from flask import Flask, jsonify, Response, request, g

app = Flask(__name__)

DATABASE = './inventory.db'


def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))

def get_db():
    if hasattr(g, "db"):
        return g.db
    db = g.db = sqlite3.connect(DATABASE)
    db.row_factory = make_dicts
    return db

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()



@app.route('/commit/')  #TODO: add functionality for "commit" route
def commit():
    return "commit"



@app.route('/remove/')  #TODO: add functionality for "remove" route
def remove():
    return "remove"



@app.route('/api/inventory', methods=['GET', 'POST'])    #GET request that returns database records that match name or id number. 
def inventory():
    if request.method == 'POST':
        id = request.form.get('id')
        matches = search(id)
        table = ""
        for item in matches:
            id = item['id']
            name = item['name']
            stock = item['stock']
            price = item['price']
            table += f"id: {id} name: {name} stock: {stock} price: {price}\n"
        return table

    return ''' <form method="POST">
                    Name/ID: <input type="text" name="id"><br>
                    <input type="submit" value="Submit"><br>
               </form>'''
   
def search(id):
    db = get_db()
    cur = db.cursor()
    cur.execute('select * from inv where id = ? or name = ? COLLATE NOCASE', (id, id))  #Case-insensitive search for either name or id.
    data = cur.fetchall()    #Fetch all the records retrieved from execute and place them in list of dicts (as specefied by make_dicts() fucntion.)
    cur.close()
    return data 

@app.route('/api/inventory/all', methods=['GET'])    #Same functionality as '/inventory' but instead it returns all records.
def inventory_all():
    db = get_db()
    cur = db.cursor()
    cur.execute('select * from inv')    #Select all available records from table.
    records = cur.fetchall()
    data = json.dumps(records)
    cur.close()
    
    return Response(data, mimetype = 'application/json')    

@app.route('/api/inventory/add', methods=['GET', 'POST']) #allow both GET and POST requests
def add():
    if request.method == 'POST':  #this block is only entered when the form is submitted
        name = request.form.get('name')
        stock = request.form.get('stock')
        price = request.form.get('price')
        insert(name, stock, price)
        return '''<h1>The name is: {}</h1>
                  <h1>The number in stock is: {}</h1>
                  <h1>The price is ${}'''.format(name, stock, price)

    return '''<form method="POST">
                  Name: <input type="text" name="name"><br>
                  Stock: <input type="text" name="stock"><br>
                  Price: <input type="text" name="price"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''

def insert(name, stock, price):
    try:
        db = get_db()
        cur = db.cursor()
        insert_cmd = """INSERT INTO inv(name, stock, price)
                          VALUES (?, ?, ?);"""

        data = (name, stock, price)
        cur.execute(insert_cmd, data)
        db.commit();
        return True
    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return False

