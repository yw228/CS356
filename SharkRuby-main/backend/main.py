import os
from flask import Flask, render_template, request, send_from_directory
from flask_cors import CORS, cross_origin
from flask_compress import Compress

from backend.api import get_costco_from_id, get_costcos_from_gps, get_costcos_from_query, get_costcos_from_ids

app = Flask(__name__, static_folder='gas-ui/dist/')
Compress(app)
CORS(app, origins='')

@app.get('/api/costco')
@cross_origin(origins=['http://localhost:3000', 'http://localhost:5000'])
def costco_api():
    warehouse_id = request.args.get('id', None)
    if warehouse_id:
        return get_costco_from_id(warehouse_id)
    warehouse_ids = request.args.get('ids', None)
    if warehouse_ids:
        return {'locations': get_costcos_from_ids(warehouse_ids.split(','))}
    query = request.args.get('q', None)
    if query:
        return {'locations': get_costcos_from_query(query)}
    lat = request.args.get('lat')
    long = request.args.get('long')
    return {'locations': get_costcos_from_gps(lat, long)}

@app.get('/.well-known/assetlinks.json')
def asset_links():
    return app.send_static_file('assetlinks.json')

@app.get('/privacy')
def privacy():
    return app.send_static_file('privacy.html')

@app.get('/assets/<path:path>')
def assets(path):
    return send_from_directory(os.path.join(app.static_folder, 'assets'), path)

@app.get('/', defaults={'path': ''})
@app.get('/<path:path>')
def index(path):
    try:
        return send_from_directory(app.static_folder, path)
    except Exception:
        return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run()