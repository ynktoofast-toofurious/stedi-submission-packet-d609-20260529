CREATE EXTERNAL TABLE IF NOT EXISTS stedi.accelerometer_landing (
    user string,
    timestamp bigint,
    x double,
    y double,
    z double
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
WITH SERDEPROPERTIES (
  'ignore.malformed.json'='true'
)
LOCATION 's3://stedi-d609-096936281593-20260529/accelerometer/landing/'
TBLPROPERTIES ('has_encrypted_data'='false');
