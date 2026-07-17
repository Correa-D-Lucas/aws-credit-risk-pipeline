# spark_session.py
from pyspark.sql import SparkSession

def get_spark():
    """Initialize a spark session"""
    return (SparkSession.builder
        .appName("credit-risk-project")
        .getOrCreate()
    )