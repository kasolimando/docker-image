from flask import request, jsonify
from database.directoryModel import Directory, db
from database.schemas import DirectorySchema

directory_schema = DirectorySchema()

def delete_directories(id):
    try:
        directory = Directory.get_by_id(id)

        if not directory:
            return jsonify({'error': 'Directory not found.'}), 404
        
        directory.delete()

        return jsonify(), 204

    except:
        return jsonify({'error': 'Directory not found.'}), 404