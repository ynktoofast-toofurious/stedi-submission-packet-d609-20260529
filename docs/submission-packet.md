# STEDI Submission Packet

## 1) Final Report

### Student Information

- Name: YANNICK NKONGOLO
- Date: 2026-05-29
- AWS Region: us-east-1
- AWS Account: 096936281593 (voclabs)

### Objective

Build and validate a complete STEDI data pipeline across landing, trusted, and curated zones using AWS Glue and Athena.

### Landing Zone

Implemented Glue ingestion from S3-backed landing datasets for customer, accelerometer, and step trainer. Landing DDL was provided with typed columns in:

- sql/customer_landing.sql
- sql/accelerometer_landing.sql
- sql/step_trainer_landing.sql

Athena validation results:

- customer_landing = 956
- customer_landing rows with blank shareWithResearchAsOfDate = 474
- accelerometer_landing = 81273
- step_trainer_landing = 28680

### Trusted Zone

Implemented trusted transformations with privacy filtering and joins:

- customer_landing_to_trusted filters out rows where shareWithResearchAsOfDate is null.
- accelerometer_landing_to_trusted joins accelerometer_landing to customer_trusted on user = email and outputs only accelerometer fields.
- step_trainer_landing_to_trusted joins step_trainer_landing to customer_curated on serialNumber.

Athena validation results:

- customer_trusted = 482
- customer_trusted with blank shareWithResearchAsOfDate = 0
- accelerometer_trusted = 40981
- step_trainer_trusted = 14460

### Curated Zone

Implemented curated transformations:

- customer_trusted_to_curated joins customer_trusted and accelerometer_trusted on email/user and outputs customer columns.
- machine_learning_curated joins step_trainer_trusted and accelerometer_trusted on sensorReadingTime = timestamp.

Athena validation results:

- customer_curated = 482
- machine_learning_curated = 43681

### Glue Job Run Evidence (SUCCEEDED)

- stedi_customer_landing_to_trusted: jr_1af673e3f8d649e96a09a4cbb6d1f1906cf00a799f87ace2067bb22e7e31d6dc
- stedi_accelerometer_landing_to_trusted: jr_f5b671b92e745d4b13dc0015fe575fe540ccfc4340454809fab77060e98e5b12
- stedi_customer_trusted_to_curated: jr_3022843c614c39fa6e94736198f3b052e67ab39f73dcce6adc046561a545852c
- stedi_step_trainer_landing_to_trusted: jr_ed8724658fcc368c875a9df0c65473600d64ad59b259799d66d3daefd220553e
- stedi_machine_learning_curated: jr_48738b7730eba2b5e99950ae05a70b0cdf11af50187a21dc6283fa3dfb6cb2d9

### Notes

- Data Catalog sources were used for stable joins and schema consistency.
- Final outputs were validated in Athena after successful reruns of curated jobs.
- Detailed command and run history is documented in docs/cli-execution-log.md.

### Conclusion

The STEDI pipeline was implemented and validated successfully against the required landing/trusted/curated rubric checks, including privacy filtering and final machine-learning curated output generation.

## 2) Rubric Evidence Checklist

### Landing Zone

- Screenshot: Glue job/source node for customer landing input (S3 or Data Catalog-backed S3).
- Screenshot: Glue job/source node for accelerometer landing input.
- Screenshot: Glue job/source node for step trainer landing input.
- Include SQL files in submission:
  - sql/customer_landing.sql
  - sql/accelerometer_landing.sql
  - sql/step_trainer_landing.sql
- Athena screenshot: customer_landing count = 956.
- Athena screenshot: customer_landing has blank shareWithResearchAsOfDate values.
- Athena screenshot: accelerometer_landing count = 81273.
- Athena screenshot: step_trainer_landing count = 28680.

### Trusted Zone

- Screenshot: Glue target setting that enables Data Catalog create/update schema behavior.
- Athena screenshot: customer_trusted count = 482.
- Athena screenshot: customer_trusted blank shareWithResearchAsOfDate count = 0.
- Athena screenshot: accelerometer_trusted count = 40981.
- Athena screenshot: step_trainer_trusted count = 14460.
- Screenshot/evidence: customer_landing_to_trusted filter logic on shareWithResearchAsOfDate.
- Screenshot/evidence: accelerometer_landing_to_trusted join on customer email and output only accelerometer columns.

### Curated Zone

- Screenshot/evidence: customer_trusted_to_curated joins customer_trusted + accelerometer_trusted by email and outputs customer columns only.
- Screenshot/evidence: step_trainer_landing_to_trusted joins step_trainer_landing + customer_curated by serialNumber.
- Screenshot/evidence: machine_learning_curated joins step_trainer_trusted + accelerometer_trusted by sensorReadingTime = timestamp.
- Athena screenshot: customer_curated count = 482.
- Athena screenshot: machine_learning_curated count = 43681.

### Final Attachments

- Glue run-success screenshots for all 5 jobs.
- Athena query screenshots for all required counts/quality checks.
- Submission narrative generated from docs/submission-report-template.md and docs/cli-execution-log.md.

## 3) One-Pass Screenshot Shot List

1. Athena: SELECT COUNT(*) FROM stedi.customer_landing; result 956
2. Athena: SELECT COUNT(*) FROM stedi.customer_landing WHERE shareWithResearchAsOfDate IS NULL; result 474
3. Athena: SELECT COUNT(*) FROM stedi.accelerometer_landing; result 81273
4. Athena: SELECT COUNT(*) FROM stedi.step_trainer_landing; result 28680
5. Athena: SELECT COUNT(*) FROM stedi.customer_trusted; result 482
6. Athena: SELECT COUNT(*) FROM stedi.customer_trusted WHERE shareWithResearchAsOfDate IS NULL; result 0
7. Athena: SELECT COUNT(*) FROM stedi.accelerometer_trusted; result 40981
8. Athena: SELECT COUNT(*) FROM stedi.step_trainer_trusted; result 14460
9. Athena: SELECT COUNT(*) FROM stedi.customer_curated; result 482
10. Athena: SELECT COUNT(*) FROM stedi.machine_learning_curated; result 43681
11. Glue graph: customer_landing_to_trusted (filter/drop null consent)
12. Glue graph: accelerometer_landing_to_trusted (join user = email, accelerometer-only output)
13. Glue graph: customer_trusted_to_curated (join customer_trusted + accelerometer_trusted)
14. Glue graph: step_trainer_landing_to_trusted (join by serialNumber)
15. Glue graph: machine_learning_curated (join by sensorReadingTime = timestamp)
16. Glue target setting: Data Catalog create/update schema and partitions enabled
17. Glue runs list: all five jobs in SUCCEEDED state

## 4) Submission File Bundle

- sql/customer_landing.sql
- sql/accelerometer_landing.sql
- sql/step_trainer_landing.sql
- sql/40_rubric_queries.sql
- docs/submission-packet.md
- docs/cli-execution-log.md
