import sys
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
DATABASE = "stedi"
OUTPUT_PATH = "s3://stedi-d609-096936281593-20260529/step_trainer/trusted/"

sc = SparkContext()
glue_context = GlueContext(sc)
spark = glue_context.spark_session
job = Job(glue_context)
job.init(args["JOB_NAME"], args)

step_trainer_df = glue_context.create_dynamic_frame.from_catalog(
    database=DATABASE,
    table_name="step_trainer_landing",
).toDF()

customer_curated_df = glue_context.create_dynamic_frame.from_catalog(
    database=DATABASE,
    table_name="customer_curated",
).toDF()

trusted_df = (
    step_trainer_df.alias("s")
    .join(customer_curated_df.alias("c"), step_trainer_df["serialnumber"] == customer_curated_df["serialnumber"], "inner")
    .select("s.sensorreadingtime", "s.serialnumber", "s.distancefromobject")
    .dropDuplicates()
)

trusted_df.write.mode("overwrite").parquet(OUTPUT_PATH)

job.commit()
