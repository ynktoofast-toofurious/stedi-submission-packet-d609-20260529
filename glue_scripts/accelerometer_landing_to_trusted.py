import sys
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
DATABASE = "stedi"
OUTPUT_PATH = "s3://stedi-d609-096936281593-20260529/accelerometer/trusted/"

sc = SparkContext()
glue_context = GlueContext(sc)
spark = glue_context.spark_session
job = Job(glue_context)
job.init(args["JOB_NAME"], args)

accelerometer_df = glue_context.create_dynamic_frame.from_catalog(
    database=DATABASE,
    table_name="accelerometer_landing",
).toDF()

customer_trusted_df = glue_context.create_dynamic_frame.from_catalog(
    database=DATABASE,
    table_name="customer_trusted",
).toDF()

trusted_df = (
    accelerometer_df.alias("a")
    .join(customer_trusted_df.alias("c"), accelerometer_df["user"] == customer_trusted_df["email"], "inner")
    .select("a.user", "a.timestamp", "a.x", "a.y", "a.z")
    .dropDuplicates()
)

trusted_df.write.mode("overwrite").parquet(OUTPUT_PATH)

job.commit()
