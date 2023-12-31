from flask import Flask
from database.directoryModel import Directory, db
from database.schemas import DirectorySchema
from request.post import post_directory
from request.getStatus import get_directories_status
from request.getSpecific import get_specific_directories
from request.put import put_directories
from request.patch import patch_directories
from request.delete import delete_directories
from request.getAll import get_directories
import os #ESTA LINEA FUE AGREGADA

app = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:kr140701@docker-image-pgsql.pj-krodriguez-20.svc/pratica2'

flask_database_name = os.environ.get('FLASK_DATABASE_NAME')
flask_database_user = os.environ.get('FLASK_DATABASE_USER')
flask_database_password = os.environ.get('FLASK_DATABASE_PASSWORD')
flask_database_host = os.environ.get('FLASK_DATABASE_HOST')
flask_allowed_hosts = os.environ.get('FLASK_ALLOWED_HOSTS')

app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{flask_database_user}:{flask_database_password}@{flask_database_host}/{flask_database_name}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

directory_schema = DirectorySchema()

@app.route('/')

@app.route('/directories/', methods=['POST'])
def post_directory_route():
    return post_directory()

@app.route('/status/', methods=['GET'])
def get_directory_route():
    return get_directories_status()

@app.route('/directories/', methods=['GET'])
def get_all_directory_route():
    return get_directories()

@app.route('/directories/<int:id>', methods=['GET'])
def get_specific_directory_route(id):
    return get_specific_directories(id)

@app.route('/directories/<int:id>', methods=['PUT'])
def put_directory_route(id):
    return put_directories(id)

@app.route('/directories/<int:id>', methods=['PATCH'])
def patch_directory_route(id):
    return patch_directories(id)

@app.route('/directories/<int:id>', methods=['DELETE'])
def delete_directory_route(id):
    return delete_directories(id)
    

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=8000)
