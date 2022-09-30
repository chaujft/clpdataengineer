import datetime as dt

from marshmallow import Schema, fields

class SensorData(object):
    def __init__(self, sensor_id, timestamp, sensor_type, reading):
        self.sensor_id = sensor_id
        self.timestamp = timestamp
        self.sensor_type = sensor_type
        self.reading = reading
    
    def __repr__(self):
        return 

class SensorDataSchema(Schema):
    sensor_id = fields.str()
    timestamp = fields.Date()
    sensor_type = fields.str()
    reading = fields.int()