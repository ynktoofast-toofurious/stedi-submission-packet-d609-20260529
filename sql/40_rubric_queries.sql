-- Landing checks
SELECT COUNT(*) AS customer_landing_count FROM stedi.customer_landing;
SELECT COUNT(*) AS customer_blank_research_consent_count
FROM stedi.customer_landing
WHERE shareWithResearchAsOfDate IS NULL;
SELECT COUNT(*) AS accelerometer_landing_count FROM stedi.accelerometer_landing;
SELECT COUNT(*) AS step_trainer_landing_count FROM stedi.step_trainer_landing;

-- Trusted checks
SELECT COUNT(*) AS customer_trusted_count FROM stedi.customer_trusted;
SELECT COUNT(*) AS customer_trusted_blank_research_consent_count
FROM stedi.customer_trusted
WHERE shareWithResearchAsOfDate IS NULL;
SELECT COUNT(*) AS accelerometer_trusted_count FROM stedi.accelerometer_trusted;
SELECT COUNT(*) AS step_trainer_trusted_count FROM stedi.step_trainer_trusted;

-- Curated checks
SELECT COUNT(*) AS customer_curated_count FROM stedi.customer_curated;
SELECT COUNT(*) AS machine_learning_curated_count FROM stedi.machine_learning_curated;

-- Optional quality checks
SELECT email, COUNT(*) AS cnt
FROM stedi.customer_curated
GROUP BY email
HAVING COUNT(*) > 1;

SELECT serialNumber, sensorReadingTime, COUNT(*) AS cnt
FROM stedi.step_trainer_trusted
GROUP BY serialNumber, sensorReadingTime
HAVING COUNT(*) > 1;
