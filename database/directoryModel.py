from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Directory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),  nullable=False)
    emails = db.Column(db.ARRAY(db.String(360)), nullable=False)
    
    def __init__(self, name, emails):
        self.name = name
        self.emails = emails

    @classmethod
    def get_all(cls):
        return cls.query.all()
    
    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()