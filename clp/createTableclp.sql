CREATE TABLE clp (
    sensor_id INT NOT NULL PRIMARY KEY,
    time_stamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    sensor_type varchar(255),
    reading INT
);

INSERT INTO clp(sensor_id, time_stamp, sensor_type, reading)VALUES(1,'2021-04-30T00:50:30Z','temperature',2000);
INSERT INTO clp(sensor_id, time_stamp, sensor_type, reading)VALUES(2,'2021-04-30T00:50:30Z','humidity',60);
INSERT INTO clp(sensor_id, time_stamp, sensor_type, reading)VALUES(3,'2021-04-30T00:50:40Z','temperature',2500);
INSERT INTO clp(sensor_id, time_stamp, sensor_type, reading)VALUES(4,'2021-04-30T00:50:40Z','humidity',75);