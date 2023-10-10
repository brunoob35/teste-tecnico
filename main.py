from flask import Flask, jsonify, request
from pymongo import MongoClient

from handlers import devices_handler, points_handler

app = Flask(__name__)

# DB connection
mongo_uri = "mongodb://localhost:27017"
client = MongoClient(mongo_uri)
db = client['devices-storage']


##Devices Routes:
# Fetch all
@app.route('/devices', methods=['GET'])
def get_devices_w_points():
    resp = devices_handler.get_devices_w_points(db)
    return resp

# Create
@app.route('/devices', methods=['POST'])
def insert_device():
    req = request.get_json()
    resp = devices_handler.insert_devices(db, req)
    return resp

# Fetch by Id
@app.route('/deviceId/<id>', methods=['GET'])
def get_device_by_id(id):
    resp = devices_handler.get_device_by_id(db, id)
    return resp

# Fetch by Serial
@app.route('/device/<int:serial>', methods=['GET'])
def get_device_by_serial(serial):
    resp = devices_handler.get_device_by_serial(db, serial)
    return resp


# Edit by serial
@app.route('/devices/<int:serial>', methods=['PUT'])
def edit_device_by_serial(serial):
    req = request.get_json()
    resp = devices_handler.edit_device_by_serial(db, serial, req)
    return resp


# Delete
@app.route('/devices/<int:serial>', methods=['DELETE'])
def delete_device_by_serial(serial):
    resp = devices_handler.delete_device_by_serial(db, serial)
    return resp

##Points Routes:
# Create
@app.route('/points', methods=['POST'])
def insert_point():
    req = request.get_json()
    resp = points_handler.insert_point(db, req)
    return resp

# Fetch by Serial
@app.route('/points/<int:serial>', methods=['GET'])
def get_point_by_serial(serial):
    resp = points_handler.get_point_by_serial(db, serial)
    return resp

# Edit by serial
@app.route('/points/<int:serial>', methods=['PUT'])
def update_point_by_serial(serial):
    req = request.get_json()
    resp = points_handler.update_point_by_serial(db, serial, req)
    return resp

# Delete
@app.route('/points/<int:serial>', methods=['DELETE'])
def delete_point_by_serial(serial):
    resp = points_handler.delete_point_by_serial(db, serial)
    return resp

app.run(port=5000, host='localhost', debug=True)