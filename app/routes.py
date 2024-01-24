from app import app
from flask import request, abort, Response
from app.db_utils import db_create, db_read, db_purge
import datetime
import json

@app.route('/test')
def test():
    return "yuh"

@app.route('/c', methods=['POST'])
def c():
    if request.method == 'POST':
        if request.form['password'] != '':
            abort(403)
        db_create(price=float(request.form['price']))
        db_purge()
        return Response(status=201, response={'price': price, 'timestamp': datetime.datetime.now(datetime.UTC).strftime('%Y-%m-%d %H:%M:%S')}, mimetype='application/json')

@app.route('/r')
def r():
    try:
        limit = int(request.args.get('limit'))
        data_list = db_read(limit=limit)
        return Response(status=200, response=json.dumps(data_list), mimetype='application/json')
    except:
        return Response(status=400, response=json.dumps({'error': 'Insufficient arguments.'}), mimetype='application/json')
