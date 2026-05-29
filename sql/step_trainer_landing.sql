CREATE EXTERNAL TABLE IF NOT EXISTS stedi.step_trainer_landing (
    sensorReadingTime bigint,
    serialNumber string,
    distanceFromObject int
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
WITH SERDEPROPERTIES (
  'ignore.malformed.json'='true'
)
LOCATION 's3://stedi-d609-096936281593-20260529/step_trainer/landing/'
TBLPROPERTIES ('has_encrypted_data'='false');
