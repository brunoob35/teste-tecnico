from flask import jsonify

from handlers import points_handler
from models.devices_model import Device
from models.points_model import Point
from pprint import pprint

def get_devices(db):
    results = db.devices.find()
    devices = [{'_id': str(device['_id']),
                'name': device['name'],
                'serialNumber': device['serial_number']}
               for device in results]
    return jsonify(devices)

def get_devices_w_points(db):
    devices_cursor = db.devices.find()
    devices_list = []

    for device in devices_cursor:
        device_data = {
            '_id': str(device['_id']),
            'name': device['name'],
            'serialNumber': device['serial_number'],
            'points': []
        }
        device = Device(**device_data)
        devices_list.append(device)

    for device in devices_list:

        point = points_handler.get_point_by_serial(db, device.serialNumber)
        desserializedPoint = point.get_json()
        device.points.append(desserializedPoint)

    devices_json = [device.__dict__ for device in devices_list]

    return jsonify(devices_json)


def insert_devices(db, req):
    db.devices.insert_one(req)
    return jsonify((req['name'] + ' adicionado com sucesso'))

def get_device_by_id(db, id):
    strId = str(id)
    print(strId)
    results = db.devices.find({'_id': strId})
    devices = [{'_id': str(device['_id']),
                'name': device['name'],
                'serialNumber': device['serial_number']}
               for device in results]
    return jsonify(devices)

def get_device_by_serial(db, serial):
    results = db.devices.find({'serial_number': serial})
    devices = [{'_id': str(device['_id']),
                'name': device['name'],
                'serialNumber': device['serial_number']}
               for device in results]
    return jsonify(devices)

def edit_device_by_serial(db, serial, req):
    new_values = {
        "name": req['name'],
        "serial_number": req['serial_number']
    }

    result = db.devices.update_one({'serial_number': serial}, {"$set": new_values})

    if result.modified_count == 1:
        return ("device updated")
    else:
        return ("fail to updat")

def delete_device_by_serial(db, serial):
    device = db.points.find({'serial_number': serial})

    if device:
        db.devices.delete_many({'serial_number': serial})
        db.points.delete_one({'serial_number': serial})
        return jsonify({'message': 'Device and associated points deleted successfully'})
    else:
        return jsonify({'message': 'Device not found'})