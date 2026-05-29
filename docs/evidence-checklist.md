# Submission Evidence Checklist (Rubric-Aligned)

Use this checklist exactly against the rubric language.

## Landing Zone

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

## Trusted Zone

- Screenshot: Glue target setting that enables Data Catalog create/update schema behavior.
- Athena screenshot: customer_trusted count = 482.
- Athena screenshot: customer_trusted blank shareWithResearchAsOfDate count = 0.
- Athena screenshot: accelerometer_trusted count = 40981.
- Athena screenshot: step_trainer_trusted count = 14460.
- Screenshot/evidence: customer_landing_to_trusted filter logic on shareWithResearchAsOfDate.
- Screenshot/evidence: accelerometer_landing_to_trusted join on customer email and output only accelerometer columns.

## Curated Zone

- Screenshot/evidence: customer_trusted_to_curated joins customer_trusted + accelerometer_trusted by email and outputs customer columns only.
- Screenshot/evidence: step_trainer_landing_to_trusted joins step_trainer_landing + customer_curated by serialNumber.
- Screenshot/evidence: machine_learning_curated joins step_trainer_trusted + accelerometer_trusted by sensorReadingTime = timestamp.
- Athena screenshot: customer_curated count = 482.
- Athena screenshot: machine_learning_curated count = 43681.

## Final Attachments

- Glue run-success screenshots for all 5 jobs.
- Athena query screenshots for all required counts/quality checks.
- Submission narrative generated from docs/submission-report-template.md and docs/cli-execution-log.md.
