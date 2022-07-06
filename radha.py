from pyspark.sql import SparkSession
from pyspark.sql.types import*
from pyspark import *
sc=SparkContext.getOrCreate()
spark = SparkSession(sc)

rdd2 = spark.sparkContext.textFile("stu.text")
#print(rdd2.collect())
rdd3=rdd2.map(lambda x:x.split(","))
print(rdd3.collect())