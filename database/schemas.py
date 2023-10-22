from marshmallow import Schema, fields

class DirectorySchema(Schema):
    id = fields.Integer()
    name = fields.String()
    emails = fields.List(fields.String())