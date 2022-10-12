from flask import Flask, jsonify, request, render_template, request, redirect
import psycopg2
import os
from sqlite3 import Cursor, Timestamp
import pandas as pd

app = Flask(__name__)

#### Configuration for PostgresSQL database connection
clpconfig = psycopg2.connect(
    host="localhost",
    database="clp_casestudyA",
    user="clp",
    password="clp",
    port="5432"
)
inbounddata = clpconfig.cursor()

#### File Upload and allowed extensions
uploadfile = './uploaded'
allowed_extensions = {'csv'}
app.config['uploadedfile'] = uploadfile

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in allowed_extensions

#### Inbound sensor record to Postgres database table
sql = """INSERT INTO clp
        VALUES(%s, %s, %s, %s);
"""

#### Functions to add the data into the table using 4 parameters
def addData(id, t, st, r):
    inbounddata.execute(sql, (id, t, st, r))
    clpconfig.commit()

#### Read the CSV file and change the column type of reading
def getcsv(filepath):
    df = pd.read_csv(filepath, header=0)
    df['reading'] = df['reading'].astype(float)
    
    for i, row in df.iterrows():
        addData(row['sensor_id','timestamp','sensor_type','reading'])

#### API inbound

@app.route("/")
def uploadlocation():
    return render_template('upload.html')
    
@app.route('/', methods=['POST'])
def add_reading():
    f = request.files['data_file']
    if not f:
        return "file not received", 400
    elif not allowed_file(f):
        return "not csv file", 400
    filedestination = os.path.join(app.config['uploadedfile'], f.filename)
    f.save(filedestination)
    getcsv(filedestination)
    return redirect(url_for('upload'))

if __name__ == "__main__":
    app.run()