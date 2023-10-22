from flask import request, jsonify
from database.directoryModel import Directory, db
from database.schemas import DirectorySchema

directory_schema = DirectorySchema()

def post_directory():
    try:
        name = request.json['name']
        emails = request.json['emails']

        new_directory = Directory(name=name, emails=emails)

        new_directory.save()

        data = directory_schema.dump(new_directory)

        return jsonify(data), 201
    except:
        return jsonify({'message': 'Bad Request'}), 400