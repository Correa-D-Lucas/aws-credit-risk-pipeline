# main.py

from utils.spark_session import get_spark
from ingestion.raw_to_bronze import raw_to_bronze


def main():
    """Orchestration"""
    spark = get_spark()

    try:
        raw_to_bronze(
            spark=spark, 
            source_path="data/raw", 
            destination_folder="data/bronze")
        
        print("File was successfully created in bronze layer.")

    except Exception as e:
        print(f"Ingestion to bronze failed: {e}")
        raise

    finally:
        spark.stop()




if __name__=="__main__":
    main()