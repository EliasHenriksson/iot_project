from marshmallow import Schema, fields
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

ma = Marshmallow()
db = SQLAlchemy()

class Observation(db.Model):
    __tablename__ = 'observations'
    observationId = db.Column(db.Integer, primary_key=True)
    thingId = db.Column(db.String(150), nullable=False)
    name = db.Column(db.String(150), nullable=False)
    timestamp = db.Column(db.Integer, nullable=False)
    data = db.Column(db.String(150), nullable=False)

    def __init__(self, thingId, name, timestamp, data):
        self.thingId = thingId
        self.timestamp = timestamp
        self.name = name
        self.data = data

class ObservationSchema(ma.Schema):
    thingId = fields.String(required=True)
    name = fields.String(required=True)
    timestamp = fields.Integer(required=True)
    data = fields.Dict(required=True)