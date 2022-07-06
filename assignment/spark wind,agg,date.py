from pyspark.sql.functions import *
from pyspark.sql import SparkSession
from pyspark import *
sc=SparkContext.getOrCreate()
spark = SparkSession(sc)

# window function
# 1.ranking functions
# 2.analytic functions
# 3.aggregate functions

simpleData = (("James", "Sales", 3000), \
              ("Michael", "Sales", 4600), \
              ("Robert", "Sales", 4100), \
              ("Maria", "Finance", 3000), \
              ("James", "Sales", 3000), \
              ("Scott", "Finance", 3300), \
              ("Jen", "Finance", 3900), \
              ("Jeff", "Marketing", 3000), \
              ("Kumar", "Marketing", 2000), \
              ("Saif", "Sales", 4100) \
              )

columns = ["employee_name", "department", "salary"]
df = spark.createDataFrame(data=simpleData, schema=columns)
#df.show()









#windowSpec=Window.partitionBy("department").orderBy("salary" )
#df.withColumn("row_number",row_number().over(windowSpec)).show()



#2.3 dense_rank Window Function

from  pyspark.sql.functions import dense_rank
#df.withColumn("xxx.com",dense_rank().over(windowSpec)) \
  # .show()
from pyspark.sql.functions import dense_rank
#df.withColumn("dense_rank",dense_rank().over(windowSpec)).show()
#
#
# """rank"""
from pyspark.sql.functions import rank
# df.withColumn("rank",rank().over(windowSpec)).show()


""" percent_rank """
from pyspark.sql.functions import percent_rank
#df.withColumn("percent_rank",percent_rank().over(windowSpec)) \
    #.show()

"""ntile"""
from pyspark.sql.functions import ntile
#df.withColumn("ntile",ntile(4).over(windowSpec)) \
    # .show()
#. PySpark Window Analytic functions
#3.1 cume_dist Window Function

""" cume_dist """
from pyspark.sql.functions import cume_dist
#df.withColumn("cume_dist",cume_dist().over(windowSpec)).show()



"""lag"""
from pyspark.sql.functions import lag
#df.withColumn("lag",lag("salary",1).over(windowSpec)) \
 # .show()
#
#
#windowSpecAgg  = Window.partitionBy("department")
#from pyspark.sql.functions import col,avg,sum,min,max,row_number
#df.withColumn("row",row_number().over(windowSpec)) \
#   .withColumn("avg", avg(col("salary")).over(windowSpecAgg)) \
 #  .withColumn("sum", sum(col("salary")).over(windowSpecAgg)) \
##  .withColumn("max", max(col("salary")).over(windowSpecAgg)) \
#   .where(col("row")==1).select("department","avg","sum","min","max") \
#  .show()
"""lead"""
from pyspark.sql.functions import lead
#df.withColumn("lead",lead("salary",2).over(windowSpec)) \
    # .show()






simpleData1 = [(1,"tyx",200,"2021-01-01"),
            (2,"syx",200,"2021-01-04"),
            (3,"tyx",500,"2021-01-06"),
            (4,"ryx",200,"2021-01-06"),
            (5,"eyx",400,"2021-01-08"),
            (6,"wyx",200,"2021-01-09"),
            (7,"jyx",400,"2021-01-01"),
            (8,"lyx",200,"2021-01-01"),
            (9,"vyx",200,"2021-01-01")]



column=("Id","Name","salary","to_date,yyyy-mm-dd,alias to_date")
df1= spark.createDataFrame(data=simpleData1,schema=column)
#df1.show()
simpleData2 = [(1,200),
            (2,200),
            (3,500),
            (4,200),
            (5,400),
            (6,200),
            (7,400),
            (8,200),
            (9,200)]
columns=("id","salary")
df2= spark.createDataFrame(data=simpleData2,schema=columns)
df2.show()
#Q.1 retrive the max date and groupby name,id.
#df1.select('*').groupBy('id','name').agg(max('date')).alias("max_date").show()
#df1.select("*").groupBy("name").agg(max("salary")).show()

# from pyspark.sql.window import Window
# from pyspark.sql.functions import*
# from pyspark.sql.functions import row_number
# from pyspark.sql.functions import col
# from pyspark.sql.functions import max
# windowSpec  = Window.partitionBy("id").orderBy(col("salary").desc())
# df_salary_rank=df2.withColumn("salary_rank",dense_rank().over(windowSpec))
# df_salary_rank.show()
# n=int(input("Enter the value of n:"))
# print("n is: ",n)
# df_salary_rank.filter(f"salary_rank =={n}").show()




# df.select("Id","Name","salary").withColumn\
#     ("dense_rank",dense_rank().over(Window.partitionBy("salary"))).show()
# df.withColumn("lag_val",lag("salary").over(windowSpec)).show()
df.withColumn("max",max("salary").over(Window.partitionBy("Id","Name"))).show()
# df.withColumn("min",min("salary").over(Window.partitionBy("Id","Name"))).show()
#df.withColumn("avg",avg(col("salary")).over(Window.partitionBy("Id","Name"))).show()




df1.select("Id","Name","salary").groupBy("Id","Name").max("salary").show()

df1.select("date","Name","salary","Id").groupBy("Id","Name").max("date").show()

