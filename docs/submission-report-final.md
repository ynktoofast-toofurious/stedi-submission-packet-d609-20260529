# STEDI Human Balance Analytics - Final Submission Report

## Student Information

- Name: YANNICK NKONGOLO
- Date: 2026-05-29
- AWS Region: us-east-1
- AWS Account: 096936281593 (voclabs)

## Objective

Build and validate a complete STEDI data pipeline across landing, trusted, and curated zones using AWS Glue and Athena.

## Landing Zone

Implemented Glue ingestion from S3-backed landing datasets for customer, accelerometer, and step trainer. Landing DDL was provided with typed columns in:

- sql/customer_landing.sql
- sql/accelerometer_landing.sql
- sql/step_trainer_landing.sql

Athena validation results:

- customer_landing = 956
- customer_landing rows with blank shareWithResearchAsOfDate = 474
- accelerometer_landing = 81273
- step_trainer_landing = 28680

## Trusted Zone

Implemented trusted transformations with privacy filtering and joins:

- customer_landing_to_trusted filters out rows where shareWithResearchAsOfDate is null.
- accelerometer_landing_to_trusted joins accelerometer_landing to customer_trusted on user = email and outputs only accelerometer fields.
- step_trainer_landing_to_trusted joins step_trainer_landing to customer_curated on serialNumber.

Athena validation results:

- customer_trusted = 482
- customer_trusted with blank shareWithResearchAsOfDate = 0
- accelerometer_trusted = 40981
- step_trainer_trusted = 14460

## Curated Zone

Implemented curated transformations:

- customer_trusted_to_curated joins customer_trusted and accelerometer_trusted on email/user and outputs customer columns.
- machine_learning_curated joins step_trainer_trusted and accelerometer_trusted on sensorReadingTime = timestamp.

Athena validation results:

- customer_curated = 482
- machine_learning_curated = 43681

## Glue Job Run Evidence (SUCCEEDED)

- stedi_customer_landing_to_trusted: jr_1af673e3f8d649e96a09a4cbb6d1f1906cf00a799f87ace2067bb22e7e31d6dc
- stedi_accelerometer_landing_to_trusted: jr_f5b671b92e745d4b13dc0015fe575fe540ccfc4340454809fab77060e98e5b12
- stedi_customer_trusted_to_curated: jr_3022843c614c39fa6e94736198f3b052e67ab39f73dcce6adc046561a545852c
- stedi_step_trainer_landing_to_trusted: jr_ed8724658fcc368c875a9df0c65473600d64ad59b259799d66d3daefd220553e
- stedi_machine_learning_curated: jr_48738b7730eba2b5e99950ae05a70b0cdf11af50187a21dc6283fa3dfb6cb2d9

## Notes

- Data Catalog sources were used for stable joins and schema consistency.
- Final outputs were validated in Athena after successful reruns of curated jobs.
- Detailed command and run history is documented in docs/cli-execution-log.md.

## Conclusion

The STEDI pipeline was implemented and validated successfully against the required landing/trusted/curated rubric checks, including privacy filtering and final machine-learning curated output generation.
