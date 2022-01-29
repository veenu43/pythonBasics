from pyspark import *

conf = SparkConf().setAppName("Your First Spark App").setMaster("local[*]")

spark = SparkContext(conf=conf)

spark.setLogLevel("INFO")

numberoflines = spark.textFile("dummy.txt").count()

print("The total number of lines is "+ str(numberoflines))