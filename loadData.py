from pyspark.sql import SparkSession

class DataLoader:
    def __init__(self, path):
        try:
            spark = SparkSession.builder.appName("FakeReviewDetection").getOrCreate()
            df = spark.read.csv(path)
            return df
        except Exception as e:
            print(f"Error loading data: {e}")
            return None