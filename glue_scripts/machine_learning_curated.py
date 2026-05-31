import sys
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
DATABASE = "stedi"
OUTPUT_PATH = "s3://stedi-d609-096936281593-20260529/step_trainer/curated/"

sc = SparkContext()
glue_context = GlueContext(sc)
spark = glue_context.spark_session
job = Job(glue_context)
job.init(args["JOB_NAME"], args)

step_trainer_trusted_df = glue_context.create_dynamic_frame.from_catalog(
    database=DATABASE,
    table_name="step_trainer_trusted",
).toDF()

accelerometer_trusted_df = glue_context.create_dynamic_frame.from_catalog(
    database=DATABASE,
    table_name="accelerometer_trusted",
).toDF()

curated_df = (
    step_trainer_trusted_df.alias("s")
    .join(
        accelerometer_trusted_df.alias("a"),
        accelerometer_trusted_df["timestamp"] == step_trainer_trusted_df["sensorreadingtime"],
        "inner",
    )
    .select(
        "s.sensorreadingtime",
        "s.serialnumber",
        "s.distancefromobject",
        "a.user",
        "a.x",
        "a.y",
        "a.z",
    )
    .dropDuplicates()
)

curated_df.write.mode("overwrite").parquet(OUTPUT_PATH)

job.commit()
