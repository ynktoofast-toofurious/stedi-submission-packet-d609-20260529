import sys
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from pyspark.sql import functions as F

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
DATABASE = "stedi"
OUTPUT_PATH = "s3://stedi-d609-096936281593-20260529/customer/trusted/"

sc = SparkContext()
glue_context = GlueContext(sc)
spark = glue_context.spark_session
job = Job(glue_context)
job.init(args["JOB_NAME"], args)

source_df = glue_context.create_dynamic_frame.from_catalog(
    database=DATABASE,
    table_name="customer_landing",
).toDF()

trusted_df = (
    source_df.filter(F.col("sharewithresearchasofdate").isNotNull())
    .select(
        "customername",
        "email",
        "phone",
        "birthday",
        "serialnumber",
        "registrationdate",
        "lastupdatedate",
        "sharewithresearchasofdate",
        "sharewithpublicasofdate",
        "sharewithfriendsasofdate",
    )
)

trusted_df.write.mode("overwrite").parquet(OUTPUT_PATH)

job.commit()
