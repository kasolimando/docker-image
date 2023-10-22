from flask import request, jsonify
from database.directoryModel import Directory, db
from database.schemas import DirectorySchema

directory_schema = DirectorySchema()

def put_directories(id):
    try:
        directory = Directory.get_by_id(id)

        if not directory:
            return jsonify({'error': 'Directory not found.'}), 404
        
        json_data = request.get_json()
        
        directory.name = json_data.get('name', directory.name)
        directory.emails = json_data.get('emails', directory.emails)
        
        db.session.commit()
        
        data = directory_schema.dump(directory)
        return jsonify(data), 200

    except:
        return jsonify({'error': 'Directory not found.'}), 404