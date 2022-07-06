from pyspark.sql import SparkSession
from pyspark.sql.types import *


if __name__ == '__main__':
    spark = SparkSession.builder \
        .appName("PYSPARK 2404") \
        .master("local[*]")\
        .config("spark.driver.bindAddress", "localhost") \
        .config("spark.ui.port", "4050") \
        .getOrCreate()

    dataschema1 = StructType([StructField(name="id", dataType=IntegerType()),
                              StructField(name="fname", dataType=StringType()),
                              StructField(name="lname", dataType=StringType()),
                              StructField("age", IntegerType()),
                              StructField("gender", StringType()),
                              StructField("deptno", IntegerType()),
                              StructField("salary", LongType())
                              ])

    csvwithschemadf = spark.read.csv(
        path=r"C:\Users\RITU\PycharmProjects\pythonProject\KB.txt", schema=dataschema1,
        header=True)
    # csvwithschemadf.printSchema()
    # csvwithschemadf.show()

    # write dataframe in csv file
    csvwithschemadf.write.csv(r"C:\Users\RITU\PycharmProjects\pythonProject\venv\share", sep="\\t")

    # # write dataframe in JSON file
    csvwithschemadf.write.json(r"C:\Users\RITU\PycharmProjects\pythonProject\venv\share", mode="overwrite")
