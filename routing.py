import sqlite3
import json
from flask import Flask, jsonify, Response
from flask import g

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



@app.route('/inventory/<id>', methods=['GET'])    #GET request that returns database records that match name or id number. 
def inventory(id):
    db = get_db()
    cur = db.cursor()
    cur.execute('select * from inv where id = ? or name = ? COLLATE NOCASE', (id, id))  #Case-insensitive search for either name or id.
    records = cur.fetchall()    #Fetch all the records retrieved from execute and place them in list of dicts (as specefied by make_dicts() fucntion.)
    data = json.dumps(records)  #Create json string with the list of records.
    cur.close()
    return Response(data, mimetype = 'application/json')    #Format response using JSON MIME type so that the requesting application recognizes it.


@app.route('/inventory/all', methods=['GET']) #Same functionality as '/requests/<id>' but instead it returns all records.
def inventory_all():
    db = get_db()
    cur = db.cursor()
    cur.execute('select * from inv')    #Select all available records from table.
    records = cur.fetchall()
    data = json.dumps(records)
    cur.close()
    return Response(data, mimetype = 'application/json')    
