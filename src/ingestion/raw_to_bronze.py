# raw_to_bronze.py
from pyspark.sql import functions as F

def raw_to_bronze(spark, source_path, destination_path):
    """read csv files from raw and move it to bronze layer"""
    df = (
        
        spark.read
            .options(header=True, inferSchema=True)
            .csv(source_path)
            .withColumn("ingestion_timestamp", F.current_timestamp())
            .withColumn("source_file", F.input_file_name())
    )
    df = df.coalesce(2)
    df.write.parquet(destination_path, mode="overwrite")