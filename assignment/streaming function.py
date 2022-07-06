from pyspark.sql import SparkSession
from pyspark import *
sc=SparkContext.getOrCreate()
spark = SparkSession(sc)
simpleData1 = [(5,"tyx",200,"2021-01-01"),
            (2,"syx",200,"2021-01-04"),
            (5,"tyx",500,"2021-01-06"),
            (5,"tyx",200,"2021-01-06"),
            (5,"tyx",400,"2021-01-08"),
            (2,"syx",200,"2021-01-09"),
            (2,"syx",400,"2021-01-01")]


column=("Id","Name","salary","date")
df1= spark.createDataFrame(data=simpleData1,schema=column)
#df1.show()
from pyspark.sql.functions import *
from pyspark.sql.functions import max
from pyspark.sql.window import *
# df1.select("date","Id", to_date(col("date"), "yyy-MM-dd").alias("to_date")).show()
#df1.select("Id","Name","date").groupBy("Id","Name").agg(max("date").alias("max_date")).show()
# #df1.select("salary","Name").groupBy("Name").agg(max("salary")).show()
windowSpec = Window.partitionBy("id").orderBy(col("date").desc())
#df1.withColumn("row_number",row_number().over(windowSpec)).where(col("row_number")==1).show()
df1.select("*").groupby("id","name").agg(max("date")).show()
df1.withColumn("new_date",lead("date").over(windowSpec)).where(col("new_date")=="2999-12-31").