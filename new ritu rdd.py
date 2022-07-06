      ###how to create rdd###

from pyspark.sql import SparkSession
from pyspark.sql.types import*
from pyspark import *
sc=SparkContext.getOrCreate()
spark = SparkSession(sc)
rdd1 = spark.sparkContext.parallelize([1,2,3,4,5,6,7,8])
#print(rdd1.collect())

# rdd_set = sc.parallelize([[2,3,4,6,82,34,42],
#                      [23,12,14,16,24,21],
#                      [8,6,4,83,12,14,16],
#                      [12,45,48,46,12,14,26]])
# print(rdd_set.first())
# print(rdd_set.take(2))
# print(rdd_set.count())
# print(rdd1.collect())
# rdd2 = spark.sparkContext.textFile("stu.text")
# print(rdd2.collect())
# df=rdd2.toDF()
# df=printSchema(df)
# rdd3=rdd2.flatMap(lambda x:x.split(","))
# print(rdd3)
# rdd5 = spark.sparkContext.wholeTextFiles("KB.txt")
#print(rdd3.collect())
#rdd3.collect()
rdd4= sc.textFile("KB.txt")
#print(rdd4.collect())



Deta_s =StructType([StructField('id',dataType=IntegerType()),
                    StructField('fname',dataType=StringType()),
                    StructField('lname', dataType=StringType()),
                    StructField('age', dataType=StringType()),
                    StructField('gender', dataType=StringType()),
                    StructField('deptno', dataType=IntegerType()),
                    StructField('salary', dataType=StringType())])
df =spark.read.csv(r"C:\Users\RITU\PycharmProjects\pythonProject\KB.txt",schema=Deta_s)
df.show()
#df.write.option("header",True).csv(r"C:\Users\RITU\PycharmProjects\pythonProject\ritu")
#df.write.csv(r"C:\Users\RITU\PycharmProjects\pythonProject\ritu4")
##assignment question
rdd6=spark.sparkContext.parallelize([("a",1),("b",2),("c",3),("d",4)])
rdd7=spark.sparkContext.parallelize([("a",5),("b",2),("c",3),("d",4)])
#a=rdd7.collect()
#print(rdd6.collect())
rec=rdd6.filter(lambda x:x  in a)
#print(rec.collect())

a=rdd6.union(rdd7).distinct()
#print(a.collect())

re1c=rdd6.map(lambda x:x [1]*25)
#print(rec.collect())
res=rdd6.map(lambda x:x [1]%2==0)
#print(res.collect())

lines=sc.textFile("KB.txt")
#print(lines)
words=lines.flatMap(lambda x:x.split(","))
print(words.collect())
#print(words.take(10))
wordsAsTuple =words.map(lambda x:(x.lower(),1))
#print(wordsAsTuple.collect())
wordsAsTuple =words.reduceByKey(lambda x,y:x+y)
#print(wordsAsTuple.collect())
       ##groupByKey##
#df.show()
# aggrigate function
#df.agg({"salary": "max"}).show()
#df.agg({"salary": "min"}).show()
#Sort and orderby
#df.sort(df.age.desc()).show()

#df3.show()
#df4=df3.take(2)
#print(df4)


#df.agg({"salary":"max"}).show()

rdd4= sc.textFile("KB.txt")
print(rdd4.collect())

rdd8=rdd4.map(lambda x:x.split(","))
#print(rdd8.collect())
rdd9=rdd8.map(lambda x:((x[-1:]),1)).sortByKey()
#print(rdd9.collect())
rdd8=rdd4.map(lambda x:x.split(","))\
    .map(lambda x:(x,1)).sortByKey()
#print(rdd8.collect())

a=min((rdd4.map(lambda x:x.split(","))
       .map(lambda x:int(x[6]))).distinct()
      .takeOrdered(2,key=lambda x:-x))
#print(a)
empdetail=(rdd4.map(lambda x:x.split(","))
           .filter(lambda x:int(x[6])==a))
#print(empdetail.collect())







