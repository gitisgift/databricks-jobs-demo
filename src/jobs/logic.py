#from pyspark.sql import SparkSession


# def run_job(catalog: str, source: str, limit: int):
#     spark = SparkSession.getActiveSession()
#     if spark is None:
#         raise RuntimeError("Spark session not available")

#     spark.sql(f"USE CATALOG {catalog}")
#     spark.sql("CREATE SCHEMA IF NOT EXISTS demo")

#     df = spark.range(0, limit).withColumnRenamed("id", "value")
#     df = df.withColumn("source", spark.createDataFrame([(source,)], ["s"]).first()[0])

#     df.write.mode("overwrite").saveAsTable("demo.external_trigger_table")


def generate_rows(limit: int, source: str):
    """
    Pure logic function.
    No Spark. Easy to test.
    """
    if limit < 0:
        raise ValueError("limit must be non-negative")

    return [(i, source) for i in range(limit)]