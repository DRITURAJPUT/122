from pyspark.sql import SparkSession
from pyspark import *
sc=SparkContext.getOrCreate()
spark = SparkSession(sc)
from pyspark.sql.functions import*
# schema="id int,f_name string,l_name string,age int,gender string,dept_no int,salary int,j_date string"
# df = spark.read.csv(path=r"C:\Users\RITU\PycharmProjects\pythonProject\assignment\data",schema=schema)
# df.show()


#df.select(current_date().alias("current_date")).show(1)


#date_format()
#df.select(col("j_date"), date_format(col("j_date"), "MM-dd-yyyy").alias("date_format") ).show()


"""to_date"""
#df.select(col("j_date"), to_date(col("j_date"), "yyy-MM-dd").alias("to_date")).show()



#date_diff()

#df.select(col("j_date"),datediff(current_date(),col("j_date")).alias("datediff")).show()



  #trunc()
#df.select(col("j_date"), trunc(col("j_date"),"Month").alias("Month_Trunc"),
      #trunc(col("j_date"),"Year").alias("Month_Year"),trunc(col("j_date"),
               #"Month").alias("Month_Trunc")).show()

###dayofweek(), dayofmonth(), dayofyear()


#     dayofweek(col("j_date")).alias("dayofweek"),
#     dayofmonth(col("j_date")).alias("dayofmonth"),
#     dayofyear(col("j_date")).alias("dayofyear"),
#  ).show()

###current_timestamp()

data=[["1","02-01-2020 11 01 19 06"],["2","03-01-2019 12 01 19 406"],["3","03-01-2021 12 01 19 406"]]
df2=spark.createDataFrame(data,["id","j_date"])
df2.show(truncate=False)



#add_months() , date_add(), date_sub()
# df.select(col("j_date"),
#     add_months(col("j_date"),3).alias("add_months"),
#     add_months(col("j_date"),-3).alias("sub_months"),
#     date_add(col("j_date"),4).alias("date_add"),
#     date_sub(col("j_date"),4).alias("date_sub")
#   ).show()



##year(), month(), month(),next_day(), weekofyear()
# df.select(col("j_date"),
#      year(col("j_date")).alias("year"),
#      month(col("j_date")).alias("month"),
#      next_day(col("j_date"),"Sunday").alias("next_day"),
#      weekofyear(col("j_date")).alias("weekofyear")#   ).show()


###dayofweek(), dayofmonth(), dayofyear()
# df.select(col("j_date"),
#      dayofweek(col("j_date")).alias("dayofweek"),
#      dayofmonth(col("j_date")).alias("dayofmonth"),
#      dayofyear(col("j_date")).alias("dayofyear"),
#   ).show()



#to_timestamp()

# df.select(col("j_date"),
#     to_timestamp(col("j_date"), "MM-dd-yyyy HH mm ss SSS").alias("to_timestamp")
#   ).show(truncate=False)


##hour(), Minute() and second()

# ta=[["1","2020-02-01 11:01:19.06"],["2","2019-03-01 12:01:19.406"],["3","2021-03-01 12:01:19.406"]]
# df=spark.createDataFrame(col("j_date"))
#
# df.select(col("input"),
#     hour(col("input")).alias("hour"),
#     minute(col("input")).alias("minute"),
#     second(col("input")).alias("second")
#   ).show(truncate=False)




















