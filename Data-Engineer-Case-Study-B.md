Case Study: Data Engineer
---

The case study resembles areas of work for which a Senior Data Engineer in our team is responsible. There is no ground
truth for any question – our focus is more on your design philosophy, accuracy and coding style. A minimal solution that
can address the problem is always preferred to an over-engineered one. For any of the questions below, 
if any information is missing in your opinion, feel free to make assumptions.

When you finish, please upload your work to a private GitHub repository, and grant access to this email address:
manfred.lee@clp.com.hk.

## Requirements

The Digital Products team has a large number of energy sensors installed in multiple locations around Hong Kong. 
The sensor raw data is streamed into AWS MSK, a Kafka service managed by AWS. The data team is assigned to 
transform the streaming data in Kafka and store the transformed data in some object storage. We have decided 
to use Spark as the stream processing framework and MinIO as the storage.

## Deliverables

### 1. Setting up Spark and MinIO

Prepare necessary scripts in order to bootstrap a Spark cluster and MinIO in Kubernetes. It is sufficient to test
locally on Minikube. Public access is not required.

### 2. Processing the stream

We are required to transform the streaming data in Kafka, then sink the data into MinIO.

Each message under the Kafka topic has the following structure, where "measurements" is a batch 
of readings from multiple sensors across multiple points in time, "device_id" is a unique device 
identifier, "time" is the reading time in ISO format, and "cumulative_energy" is the accumulated 
energy consumption over time by that device. In the example below, device "123456" consumed 
122.45 - 120.12 = 2.33 units of energy during the period from 2022-07-11T02:15:00Z to 2022-07-11T02:20:00Z.

Example:
```json
{
  "measurements": [
    {
      "device_id": 123456,
      "device_name": "Test Device",
      "time": "2022-07-11T02:15:00Z",
      "cumulative_energy": 120.12
    },
    {
      "device_id": 123456,
      "device_name": "Test Device",
      "time": "2022-07-11T02:20:00Z",
      "cumulative_energy": 122.45
    }
  ]
}
```

Prepare codes using Spark Streaming that transform the streaming data, then sink the results into MinIO 
as parquets, with the following schema:

```
StructType(Array(
    StructField("device_id", IntegerType, false),
    StructField("device_name", StringType, false),
    StructField("time", TimestampType, false),
    StructField("duration", FloatType, true),
    StructField("delta_energy", FloatType, true)
))
```

where "delta_energy" is the **non-cumulative** energy consumption and duration is the time in minutes 
between two consecutive readings. Using the example above again, the resulting data point at "2022-07-11T02:20:00Z" 
is:
```
device_id = 123456 (in IntegerType)
device_name = "Test Device" (in StringType)
time = "2022-07-11T02:20:00Z" (in TimestampType)
delta_energy = 2.33 (in FloatType)
duration = 5.0 (in FloatType)
```

### 3. Analytics (No codes required)

The analytics team would like to query the data in MinIO directly using SQL. Suggest tools 
that may be useful here that are scalable and flexible.
