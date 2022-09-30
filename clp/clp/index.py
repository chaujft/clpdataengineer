#clp.py

from flask import Flask, jsonify, request
import csv
from clp.model.schema import SensorData, SensorDataSchema

app = Flask(__name__)

sensor_data = []

@app.route('/', methods=['POST'])
def add_reading():
    f = request.files['data_file']
    if not f:
        return "csv not received", 400

    stream = f.stream.read().decode("utf-8")
    csv_input = csv.reader(stream)  
    sensor_data.append(csv_input)
    return "csv received successfully", 200

if __name__ == "__main__":
    app.run()




#api = Api(app)



### app parsers
###sensor_args = reqparse.RequestParser()
###sensor_args.add_argument(sensor_id, type=int, help="Sensor ID; Integer value")
#sensor_args.add_argument(timestamp, type= ???, help="timestamp; datetime value")
###sensor_args.add_argument(sensor_type, type=str, help="Sensor type; string value")
###sensor_args.add_argument(reading, type=int, help="reading; Integer value")

###class Channel(Resource):
    #def post(self, sensor):
