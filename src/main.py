from pyspark.sql import SparkSession


spark = (
    SparkSession.builder.appName("First Spark")
    .config("spark.driver.host", "127.0.0.1")
    .config("spark.driver.bindAddress", "127.0.0.1")
    .getOrCreate()
)
df = spark.read.csv("data/cnn_dailymail/train.csv", header=True, inferSchema=True)
df.show(5)
spark.stop()
