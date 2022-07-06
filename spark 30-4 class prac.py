from pyspark.sql import SparkSession
from pyspark.sql.types import*
from pyspark import *
from pyspark import *
sc=SparkContext.getOrCreate()
spark = SparkSession(sc)

dataschema1 = StructType([StructField("id", dataType=IntegerType()),
                              StructField("fname", dataType=StringType()),
                              StructField("lname", dataType=StringType()),
                              StructField("age", IntegerType()),
                              StructField("gender", StringType()),
                              StructField("deptno", IntegerType()),
                              StructField("salary", LongType())
                              ])



# Create RDD from external Data source by 3 types
df = spark.read.csv(
        r"C:\Users\RITU\PycharmProjects\pythonProject\KB.txt", schema=dataschema1)
def fullformfunc(element):
    output=""
    if str(element).upper()=="M":
        output="Male"
    elif str(element).upper()=="F":
        output="Female"
    else:
        output="none"
    return output
fullformudf= udf(lambda x:fullformudf(x))
df.select("gender", fullformudf(col("gender")).show()

