from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType, TimestampType, StringType
from pyspark.sql.functions import col, when, window, avg

#### Initiate a Spark session
spark = SparkSession \
    .builder \
    .appName("clp sensor data") \
    .getOrCreate()

#### Read test csv file from folder
filepath = './test.csv'
df = spark.read.format("csv").option("header", True).load(filepath)

#### Change columns to appropriate data types and keep sensor id as string
df = df.withColumn("timestamp", df['timestamp'].cast(TimestampType()))
df = df.withColumn("reading", df['reading'].cast(IntegerType()))

#### Normalize temperature and remove abnomalies
df = df.withColumn('new_reading', when(df.sensor_type == 'temperature', df.reading/100).otherwise(df.reading)).drop(df.reading) 
#df = df.withColumn('new_reading', df['new_reading'].case(IntegerType()))
df = df.where(~((df.sensor_type == 'humidity') & ((df.new_reading < 0) | (df.new_reading > 100))))

#### Group humidity and temperature into new table
df2 = df.groupBy('sensor_id', 'timestamp').pivot('sensor_type').sum('new_reading').orderBy('sensor_id', 'timestamp')

#### Create a new column for "Dew point" in 30 minute intervals
df2 = df2.withColumn('dew_point', (100 - (5*df2.temperature - df2.humidity/100)))
df2 = df2.groupBy('sensor_id', window('timestamp', '30 minutes').alias('time_interval')).agg(avg('dew_point').alias('avg_dew_point')).orderBy('sensor_id', 'time_interval')
df2 = df2.withColumn('time_interval', col('time_interval').cast(StringType()))

# Export the data to a new CSV file
df2.write.option("header",True).csv("./clp_pyspark_out/")