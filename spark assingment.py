from pyspark.sql import SparkSession
from pyspark.sql.types import*
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
df = spark.read.csv(r"C:\Users\RITU\PycharmProjects\pythonProject\KB.txt", schema=dataschema1)
#df.show()
from pyspark.sql.functions import when
df2 = df.withColumn("deptno", when(df.deptno == 11,"HR")
                                 .when(df.deptno == 12,"Infra")
                                 .when(df.deptno == 13,"Production")
                                  .when(df.deptno == 14,"IT")
                                 .otherwise(df.deptno))
#df2.show()

df3 = df2.withColumn("age", when(df.age == 29,"40")
                                   .when(df.age == 30,"40")
                                   .when(df.age == 35,"40")
                                   .when(df.age == 33,"50")
                                   .otherwise(df.age))
#df3.show()

# Q-2 select average salary9 from department
#df.groupBy("deptno").sum("salary").show(truncate=False)
#df.groupBy("deptno").avg("salary").show(truncate=False)
#df.groupBy("deptno").max("salary").show(truncate=False)

#Q-3 provide employee details who has second highest salary
#df.groupBy("deptno").max("salary").alias("max_s").show(truncate=False) # By group by function

# #a=min((df.map(lambda x:x.split(","))
#         .map(lambda x:int(x[6]))).distinct()
#        .takeOrdered(2,key=lambda x:-x))
# #print(a)
# empdetail=(df.map(lambda x:x.split(","))
#             .filter(lambda x:int(x[6])==a))
# #print(empdetail.collect())

from pyspark.sql.window import Window
from pyspark.sql.functions import col,dense_rank,desc

windowSpec  = Window.partitionBy("id").orderBy(col("salary").desc())
df_salary_rank=df.withColumn("salary_rank",dense_rank().over(windowSpec))
df_salary_rank.show()
n=int(input("Enter the value of n:"))
print("n is: ",n)
df_salary_rank.filter(f"salary_rank =={n}").show()
df.createTempView("ritu")

#spark.sql("select * from (select id, lname, gender, deptno, salary, dense_rank() over(order by salary desc) as r from  ritu) where r ==2").show()

'''
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number
from pyspark.sql.functions import col
windowSpec = Window.partitionBy("deptno").orderBy(col("salary"))
df.withColumn("row_number",row_number().over(windowSpec)).where(col("row_number")==1).show()
'''



#Q-4. retrieve employee_details with unique records from employee_detail.txt and employee_details1.txt and store them in different file.
#df1=df.distinct()
#df1.write.option("header", True).csv(r"C:\Users\RITU\PycharmProjects\pythonProject\write")
#df1.show()

# Q-5. Create a dataframe from existing rdd/existing collection using various ways

from pyspark.sql import SparkSession
from pyspark.sql.types import*
from pyspark import *
sc=SparkContext.getOrCreate()
spark = SparkSession(sc)
columns = ["language","users_count,int"]
data = [("Java", "20000"), ("Python", "100000"), ("Scala", "3000")]
rdd = spark.sparkContext.parallelize(data)
#print(rdd.collect())


#2-toDF()

# or

dfFromRDD1 = rdd.toDF(columns)
dfFromRDD1.printSchema()
# or
dfFromRDD2 = spark.createDataFrame(rdd).toDF(*columns)
#or
dfFromData2 = spark.createDataFrame(data).toDF(*columns)
#dfFromData2.show()
#or

#3- CSV file

df2 = spark.read.csv("/src/resources/file.csv")

s1 =min((df.map(lambda x:x.split(",")).map(lambda x:x[6]))).distinct().takeOrdered(2, key=lambda x:-x)
s1= (df.map(lambda x:x.split(",")).filter(lambda x:int(x[6])== df2))
#print(s1.collect)





