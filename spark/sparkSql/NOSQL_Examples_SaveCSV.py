from pyspark import SparkContext, SparkConf
from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *

def main():
    cnfg = SparkConf().setAppName("CustomerApplication").setMaster("local[2]")
    sc = SparkContext(conf=cnfg)
    spark = SparkSession(sc)
    #inputFilePath = "D:\\Workspace\\pthonTest\\pthonTest\\spark\\BEAD_DATA-master\\BEAD_DATA-master\\\Customer.csv"

    inputFilePath = "D:\\DataSets\\archive\\Coursera.csv"
    df = (spark.read.option("header", "true").option("inferSchema", "true").csv(inputFilePath))
    #df.show(50, False)
    #df.printSchema()
    df.write.json("D:\\DataSets\\archive\\json")

    inputFilePath2 = "D:\\DataSets\\archive\\json\\*.json"
    df = (spark.read.option("header", "true").option("inferSchema", "true").json(inputFilePath2))
    df.write.csv("D:\\DataSets\\archive\\csv")

if __name__ == '__main__':
    main()