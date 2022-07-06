#There are three ways to create an RDD in Spark.

#1.Parallelizing already existing collection in driver program.


from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
sc = SparkContext('local')
spark = SparkSession(sc)

spark = SparkSession.builder \
       .master("local[1]") \
       .appName("SparkRDD") \
       .config("spark.driver.bindAddress","localhost")\
       .config("spark.ui.port","4050")\
       .getOrCreate()
words = sc.parallelize (
   ["scala",

   "java",
   "hadoop",
   "spark",
   "akka",
   "spark vs hadoop",
   "pyspark",
   "pyspark and spark"]
)
counts = words.count()
print ("Number of elements in RDD -> %i" % (counts))


# sum of salary per department by Data frame

from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.sql.readwriter
sc = SparkContext("local","app")
spark = SparkSession(sc)
simpleData = [(1,"Yesh","Patil",29,"M",11,20000),
              (2,"Ram","Wagh",30,"M",12,3000000),
              (3,"Sita","Patil",29,"F",11,50000),
              (4,"Kiran","XYZ",33,"F",11,40052),
              (5,"Savita","Waghmare",35,"F",12,800000)
  ]

schema = ["eid","first_name","last_nmae","age","sex","d_id","salary"]
df = spark.createDataFrame(data=simpleData, schema = schema)
df.printSchema()
df.show(truncate=False)
df.groupBy("d_id").sum("salary").show(truncate=False)
df.groupBy("d_id").avg("salary").show(truncate=False)
df.groupBy("d_id").max("salary").show(truncate=False)
df.groupBy("d_id").max("salary").show(truncate=False)



#creat dataframe by file
#2.Referencing a dataset in an external storage system (e.g. HDFS, Hbase, shared file system).
from pyspark.sql import SparkSession
from pyspark.sql.types import *


if __name__ == '__main__':
    spark = SparkSession.builder \
        .appName("PYSPARK 2404") \
        .master("local[*]")\
        .config("spark.driver.bindAddress", "localhost") \
        .config("spark.ui.port", "4050") \
        .getOrCreate()

    dataschema1 = StructType([StructField("id", dataType=IntegerType()),
                              StructField("fname", dataType=StringType()),
                              StructField("lname", dataType=StringType()),
                              StructField("age", IntegerType()),
                              StructField("gender", StringType()),
                              StructField("deptno", IntegerType()),
                              StructField("salary", LongType())
                              ])

    csvwithschemadf = spark.read.csv(
        path=r"C:\Users\RITU\PycharmProjects\pythonProject\KB.txt", schema=dataschema1,
        header=True)
    csvwithschemadf.printSchema()
    csvwithschemadf.show()

# no need of  spark = SparkSession.builder

from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
sc = SparkContext('local')
spark = SparkSession(sc)

from pyspark.sql.types import *
if __name__ == '__main__':
 dataschema1 = StructType([StructField("id", dataType=IntegerType()),
                          StructField("fname", dataType=StringType()),
                          StructField("lname", dataType=StringType()),
                          StructField("age", StringType()),
                          StructField("gender", StringType()),

                          ])

 csvwithschemadf = spark.read.csv(
    path=r"C:\Users\RITU\OneDrive\Desktop\New Text Document.txt", schema=dataschema1,
    header=True)
 csvwithschemadf.printSchema()
 csvwithschemadf.show()
