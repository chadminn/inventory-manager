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



@app.route('/put/')  #TODO: add functionality for "put" route
def commit():
    return "put"



@app.route('/api/inventory/delete', methods=['DELETE']) 
def remove():
    if 'id' in request.args:
        id = request.args['id']
    else:
        return "Error: no id # or name was provided.\n", 400
        
    try:
        db = get_db()
        cur = db.cursor()
        cur.execute('DELETE FROM inv WHERE id = ? OR name = ? COLLATE NOCASE', (id, id))
        db.commit()
        if db.total_changes == 0:
            return "Row not found for: " + id + '\n', 404
        cur.close()
        return "Succesfuly deleted row with: " + id + '\n'

    except Exception as e:
        return "Problem deleting db resource: " + str(e), 404
         



@app.route('/api/inventory', methods=['GET'])    #GET request that returns database records that match name or id number. 
def inventory():
    if 'id' in request.args:
        id = request.args['id']
    else:
        return "Error: no id # or product name was provided."

    db = get_db()
    cur = db.cursor()
    cur.execute('select * from inv where id = ? or name = ? COLLATE NOCASE', (id, id))  #Case-insensitive search for either name or id.
    records = cur.fetchall()    #Fetch all the records retrieved from execute and place them in list of dicts (as specefied by make_dicts() fucntion.)
    data = json.dumps(records)  #Create json string with the list of records.
    cur.close()
   
    return Response(data, mimetype = 'application/json')    #Format response using JSON MIME type so that the requesting application recognizes it.


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

if __name__ == '__main__':
    app.run(debug=False)
