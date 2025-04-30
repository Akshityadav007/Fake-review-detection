from pyspark.sql import SparkSession

class DataLoader:
    def __init__(self, path):
        try:
            spark = SparkSession.builder \
                                .appName("FakeReviewDetection") \
                                .master("local[*]") \
                                .config("spark.ui.showConsoleProgress", "false") \
                                .config("spark.hadoop.security.authentication", "simple") \
                                .getOrCreate()

            df = spark.read.csv(path, header=True, inferSchema=True)
            return df
        except Exception as e:
            print(f"Error loading data: {e}")
            return None
