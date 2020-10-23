import sqlite3
import json
from flask import Flask
from flask import g

app = Flask(__name__)

DATABASE = './inventory.db'

def get_db():
    if hasattr(g, "db"):
        return g.db
    db = g.db = sqlite3.connect(DATABASE)
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



@app.route('/request/') #TODO: add functionality for "request" route
def request():
    return "request"

