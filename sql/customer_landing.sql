CREATE EXTERNAL TABLE IF NOT EXISTS stedi.customer_landing (
    customerName string,
    email string,
    phone string,
    birthDay bigint,
    serialNumber string,
    registrationDate bigint,
    lastUpdateDate bigint,
    shareWithResearchAsOfDate bigint,
    shareWithPublicAsOfDate bigint,
    shareWithFriendsAsOfDate bigint
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
WITH SERDEPROPERTIES (
  'ignore.malformed.json'='true'
)
LOCATION 's3://stedi-d609-096936281593-20260529/customer/landing/'
TBLPROPERTIES ('has_encrypted_data'='false');
