"""Unlike our before program which uses a lot of intermediate variables which is ok to check our work but clutters the flow of code, we can avoid the intermediate variables by "chaining" the results of one methods to the next [remember, each transformation to the dataframe gives out an object], making our program compact and readable."""

from pyspark.sql import SparkSession
import pyspark.sql.functions as F
spark = SparkSession.builder.appName(
    "Analyzing the frequency of word count in a text file by chaning the methods"
).getOrCreate()

results = (
    spark.read.text("./gutenberg.txt")
    .select(F.split(F.col("value"), " ").alias("line"))
    .select(F.explode(F.col("line")).alias("word"))
    .select(F.lower(F.col("word")).alias("word"))
    .select(F.regexp_extract(F.col("word"),"[a-z']*", 0).alias("word"))
    .where(F.col("word") != "")
    .groupBy("word")
    .count()
)

print("Showing Results...")
results.show(20, truncate=False)

