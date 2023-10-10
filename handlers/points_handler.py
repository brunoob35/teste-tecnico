from flask import jsonify

def get_points(db):
    results = db.points.find()
    points = [{'_id': str(point['_id']),
                'name': point['name'],
                'serialNumber': point['serial_number'],
                'dataType': point['data_type'],
                'value': point['value']}
               for point in results]
    return jsonify(points)

def insert_point(db, req):
    db.points.insert_one(req)
    return jsonify((req['name'] + ' adicionado com sucesso'))

def get_point_by_id(db, id):
    strId = str(id)
    print(strId)
    results = db.points.find({'_id': strId})
    points = [{'_id': str(point['_id']),
                'name': point['name'],
                'serialNumber': point['serial_number'],
                'dataType': point['data_type'],
                'value': point['value']}
               for point in results]
    return jsonify(points)

def get_point_by_serial(db, serial):
    results = db.points.find({'serial_number': serial})
    points = [{'_id': str(point['_id']),
                'name': point['name'],
                'serialNumber': point['serial_number'],
                'dataType': point['data_type'],
                'value': point['value']}
               for point in results]
    return jsonify(points)

def update_point_by_serial(db, serial, req):
    new_values = {
        "name": req['name'],
        "serial_number": req['serial_number']
    }

    result = db.points.update_one({'serial_number': serial}, {"$set": new_values})

    if result.modified_count == 1:
        return ("point updated")
    else:
        return ("fail to updat")

def delete_point_by_serial(db, serial):
    point = db.points.find({'serial_number': serial})

    if point:
        db.points.delete_one({'serial_number': serial})
        return jsonify({'message': 'Point deleted successfully'})
    else:
        return jsonify({'message': 'Point not found'})
