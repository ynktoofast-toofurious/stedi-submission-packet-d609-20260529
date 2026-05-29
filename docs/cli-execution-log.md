# CLI Execution Log (voclabs)

## Environment
- Account: 096936281593
- Region: us-east-1
- Profile: voclabs
- Bucket: stedi-d609-096936281593-20260529
- Database: stedi
- Glue role created: arn:aws:iam::096936281593:role/stediGlueRole

## Glue Job Runs
- stedi_customer_landing_to_trusted: jr_1af673e3f8d649e96a09a4cbb6d1f1906cf00a799f87ace2067bb22e7e31d6dc (SUCCEEDED)
- stedi_accelerometer_landing_to_trusted: jr_f5b671b92e745d4b13dc0015fe575fe540ccfc4340454809fab77060e98e5b12 (SUCCEEDED)
- stedi_customer_trusted_to_curated: jr_eff647bf3712d00d8b01acfccd90aa8bc6e78b74b081e140262cbf1bbd9899d0 (SUCCEEDED)
- stedi_customer_trusted_to_curated (rerun, rubric logic): jr_3022843c614c39fa6e94736198f3b052e67ab39f73dcce6adc046561a545852c (SUCCEEDED)
- stedi_step_trainer_landing_to_trusted: jr_ed8724658fcc368c875a9df0c65473600d64ad59b259799d66d3daefd220553e (SUCCEEDED)
- stedi_machine_learning_curated: jr_d2f0b771a3a7ff294e7fc687241561ecfcf4fee5971a1e078666a624fbcf35a1 (SUCCEEDED)
- stedi_machine_learning_curated (rerun, rubric logic): jr_48738b7730eba2b5e99950ae05a70b0cdf11af50187a21dc6283fa3dfb6cb2d9 (SUCCEEDED)

## Final Validation Counts
- customer_trusted: 482
- accelerometer_trusted: 40981
- customer_curated: 482
- step_trainer_trusted: 14460
- machine_learning_curated: 43681

## Consent Quality Checks
- customer_landing blank shareWithResearchAsOfDate: 474
- customer_trusted blank shareWithResearchAsOfDate: 0
