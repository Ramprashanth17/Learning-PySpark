
"""
from pyspark.sql import SparkSession
from pyspark.sql.functions import (
col,
explode,
lower,
regexp_extract,
split,
)
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import (
col,
explode,
lower,
regexp_extract,
split,
)
import pyspark.sql.functions as F

spark = SparkSession.builder.appName(
    "Analyzing the vocabulary of Pride and Prejudice book."
).getOrCreate()

book = spark.read.text("./gutenberg.txt")

lines = book.select(F.split(book.value, " ").alias("line"))

words = lines.select(F.explode(F.col("line")).alias("word"))

words_lower = words.select(F.lower(F.col("word")).alias("word"))

words_clean = words_lower.select(
    regexp_extract(F.col("word"), "[a-z]*", 0).alias("word"))

words_nonull = words_clean.filter(F.col("word") != "")

results = words_nonull.groupBy(F.col("word")).count()

results.orderBy("count", ascending= False).show(10)

results.coalesce(1).write.csv("./words_frequence_single_parition.csv")

