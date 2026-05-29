# One-Pass Screenshot Shot List

Take screenshots in this exact order to satisfy the rubric with minimal backtracking.

## 1) Landing Zone (Athena)

1. Query: SELECT COUNT(*) FROM stedi.customer_landing;
   - Capture result: 956
2. Query: SELECT COUNT(*) FROM stedi.customer_landing WHERE shareWithResearchAsOfDate IS NULL;
   - Capture result: 474 (proves blanks exist)
3. Query: SELECT COUNT(*) FROM stedi.accelerometer_landing;
   - Capture result: 81273
4. Query: SELECT COUNT(*) FROM stedi.step_trainer_landing;
   - Capture result: 28680

## 2) Trusted Zone (Athena)

5. Query: SELECT COUNT(*) FROM stedi.customer_trusted;
   - Capture result: 482
6. Query: SELECT COUNT(*) FROM stedi.customer_trusted WHERE shareWithResearchAsOfDate IS NULL;
   - Capture result: 0
7. Query: SELECT COUNT(*) FROM stedi.accelerometer_trusted;
   - Capture result: 40981
8. Query: SELECT COUNT(*) FROM stedi.step_trainer_trusted;
   - Capture result: 14460

## 3) Curated Zone (Athena)

9. Query: SELECT COUNT(*) FROM stedi.customer_curated;
   - Capture result: 482
10. Query: SELECT COUNT(*) FROM stedi.machine_learning_curated;
   - Capture result: 43681

## 4) Glue Evidence (Console)

11. customer_landing_to_trusted graph showing filter/drop of null shareWithResearchAsOfDate.
12. accelerometer_landing_to_trusted graph showing join on user = email and accelerometer-only output columns.
13. customer_trusted_to_curated graph showing join customer_trusted + accelerometer_trusted by email/user and customer-only output columns.
14. step_trainer_landing_to_trusted graph showing join on serialNumber.
15. machine_learning_curated graph showing join sensorReadingTime = timestamp.
16. Target setting screenshot: Data Catalog create table and update schema/add partitions enabled.
17. Glue runs list screenshot showing all five jobs in SUCCEEDED state.

## 5) Include in Submission Package

- sql/customer_landing.sql
- sql/accelerometer_landing.sql
- sql/step_trainer_landing.sql
- docs/submission-report-final.md
- docs/cli-execution-log.md
- Optional: sql/40_rubric_queries.sql
