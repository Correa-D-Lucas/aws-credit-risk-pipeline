from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("CreditRiskIngest") \
    .getOrCreate()

df = spark.read.parquet("data_sample/credit_data.parquet")
df.show()

df.write.mode("overwrite").parquet("data/bronze/credit_data")
print("parquet written successfully.")