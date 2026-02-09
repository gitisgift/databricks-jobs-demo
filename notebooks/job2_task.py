
# Job 2: Notebook + SQL
dbutils.widgets.text("sql_file", "")
sql_file = dbutils.widgets.get("sql_file")

with open(sql_file) as f:
    spark.sql(f.read())
