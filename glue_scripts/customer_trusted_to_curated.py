import sys
from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
DATABASE = "stedi"
TARGET_TABLE = "customer_curated"
OUTPUT_PATH = "s3://stedi-d609-096936281593-20260529/customer/curated/"

sc = SparkContext()
glue_context = GlueContext(sc)
spark = glue_context.spark_session
job = Job(glue_context)
job.init(args["JOB_NAME"], args)

customer_trusted_df = glue_context.create_dynamic_frame.from_catalog(
    database=DATABASE,
    table_name="customer_trusted",
).toDF()

accelerometer_trusted_df = glue_context.create_dynamic_frame.from_catalog(
    database=DATABASE,
    table_name="accelerometer_trusted",
).toDF()

curated_df = (
    customer_trusted_df.alias("c")
    .join(accelerometer_trusted_df.alias("a"), customer_trusted_df["email"] == accelerometer_trusted_df["user"], "inner")
    .select(
        "c.customername",
        "c.email",
        "c.phone",
        "c.birthday",
        "c.serialnumber",
        "c.registrationdate",
        "c.lastupdatedate",
        "c.sharewithresearchasofdate",
        "c.sharewithpublicasofdate",
        "c.sharewithfriendsasofdate",
    )
    .dropDuplicates()
)

curated_dyf = DynamicFrame.fromDF(curated_df, glue_context, "curated_dyf")
sink = glue_context.getSink(
    path=OUTPUT_PATH,
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=[],
    enableUpdateCatalog=True,
    transformation_ctx="curated_sink",
)
sink.setCatalogInfo(catalogDatabase=DATABASE, catalogTableName=TARGET_TABLE)
sink.setFormat("glueparquet")
sink.writeFrame(curated_dyf)

job.commit()
