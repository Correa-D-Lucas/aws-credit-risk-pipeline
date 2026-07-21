# raw_to_bronze.py
from pyspark.sql import functions as F
from pathlib import Path


def raw_to_bronze(spark, source_path, destination_folder):
    """read csv files from raw and move it to bronze layer"""

    files = Path(source_path).glob("*.csv")

    if not files:
        raise FileNotFoundError(f"No CSV files found in {source_path}")


    for file in files:

        dataset_name = file.stem
        print(f"Processing {dataset_name}...")

        df = (
            
            spark.read
                .options(header=True, inferSchema=True)
                .csv(str(file))
                .withColumn("ingestion_timestamp", F.current_timestamp())
                .withColumn("source_file", F.lit(file.name))
        )



        df.write.parquet(f"{destination_folder}/{dataset_name}", mode="overwrite")