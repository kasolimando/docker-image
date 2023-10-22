from flask import request, jsonify
from database.directoryModel import Directory, db
from database.schemas import DirectorySchema
from flask_paginate import Pagination

directory_schema = DirectorySchema()

def get_directories():
    try:

        page = request.args.get('page', default=1, type=int)
        per_page = 5

        directories = Directory.query.paginate(page=page, per_page=per_page)
        total_count = directories.total
        next_page = directories.next_num if directories.has_next else None
        prev_page = directories.prev_num if directories.has_prev else None

        results = []
        for directory in directories.items:
            data = directory_schema.dump(directory)
            results.append(data)

        pagination = Pagination(page=page, total=total_count, per_page=per_page, next_num=next_page, prev_num=prev_page)

        return jsonify({
            'count': total_count,
            'next': f"{request.base_url}?page={next_page}" if next_page else None,
            'previous': f"{request.base_url}?page={prev_page}" if prev_page else None,
            'results': results
        }), 200
    except:
        return jsonify({'message': 'Not Found'}), 404