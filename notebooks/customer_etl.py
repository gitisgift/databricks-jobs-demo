# Databricks notebook source
# MAGIC %md
# MAGIC ### Customer ETL Notebook

# COMMAND ----------

dbutils.widgets.text("catalog", "")
dbutils.widgets.text("source", "")
dbutils.widgets.text("limit", "10")

catalog = dbutils.widgets.get("catalog")
source = dbutils.widgets.get("source")
limit = int(dbutils.widgets.get("limit"))

# COMMAND ----------

spark.sql(f"USE CATALOG {catalog}")
spark.sql("CREATE SCHEMA IF NOT EXISTS demo")

df = spark.range(0, limit)
df = df.withColumnRenamed("id", "value")
df = df.withColumn("source", spark.createDataFrame([(source,)], ["s"]).first()[0])

df.write.mode("overwrite").saveAsTable("demo.customer_etl")

# COMMAND ----------

display(spark.table("demo.customer_etl"))
