Case Study: Data Engineer
---

The case study resembles areas of work for which a Data Engineer in our team is responsible. 
There is no ground truth for any question – our focus is more on your design philosophy, accuracy and coding style. A minimal solution that can address the problem is always preferred to an over-engineered one.

When you finish, please upload your solution to a private GitHub repository, 
and grant access to this email address: manfred.lee@clp.com.hk.

## Requirements
The Digital Products team has a large number of sensors installed in multiple locations. 
From time to time, the data from all sensors will be batched as a CSV file and sent to an endpoint 
for further processing.  As a data engineer, you are asked to design and implement a pipeline 
to ingest and transform the batched sensor data. While there can be many variants, 
as a minimal proof-of-concept, the technical team has agreed to use a PostgreSQL database 
and Python-based RESTful APIs for this project. For simplicity, you can use localhost for 
this work.

## Deliverables
### 1. Setting up the database
Prepare necessary files and scripts in order to spin up a local PostgreSQL database in a Docker container. We should have the flexibility to change important settings such as the default database port.

### 2. Ingestion
Create an API endpoint (user authentication is not required) to accept a CSV file with sensor data and insert the data into a table inside the database. We should use appropriate HTTP request methods and return meaningful HTTP status codes.
An extract of the CSV file is as follow:

```csv
sensor_id,timestamp,sensor_type,reading
1,2021-04-30T00:50:30Z,temperature,2000
2,2021-04-30T00:50:30Z,humidity,60
3,2021-04-30T00:50:40Z,temperature,2500
4,2021-04-30T00:50:40Z,humidity,75
```
 
### 3. Business Requirements
The data are known to have the following characteristics:
- The raw temperature has been multiplied by 100 (i.e. 2000 means 20.00 degrees Celsius). We would like to show the temperature in normal scale instead. 
- In a rare case, we may get relative humidity value that is negative or greater than 100. We would like to ignore those erroneous records.

Another team has provided us specific requirements of what they want from the data:
- The half-hourly average “dew point” for each sensor. “Dew point” is defined in this relationship: RH = 100 – 5(T – DP), where RH is relative humidity in percentage, T is temperature in degrees Celsius and DP is dew point.

Prepare an executable script in Spark to handle the requirement and export the results in csv. 
You may use the Spark’s Python, Scala or Java API depending on your preference.

