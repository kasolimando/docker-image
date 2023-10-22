from flask import request, jsonify
from database.directoryModel import Directory, db
from database.schemas import DirectorySchema

directory_schema = DirectorySchema()

def get_specific_directories(id):
    try:

        directory = Directory.get_by_id(id)

        data = directory_schema.dump(directory)

        if not data:
            return jsonify({'message': 'Not Found'}), 404

        return jsonify(data), 200
    except:
        return jsonify({'message': 'Not Found'}), 404