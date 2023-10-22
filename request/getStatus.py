from flask import request, jsonify
from database.directoryModel import Directory, db
from database.schemas import DirectorySchema

directory_schema = DirectorySchema()

def get_directories_status():
    try:
        return jsonify({'response': 'pong'}), 200
    except:
        return jsonify({'message': 'Not Found'}), 404