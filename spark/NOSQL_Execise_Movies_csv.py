from pyspark import SparkContext, SparkConf
from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *

# 9. Read the Movies.CSV into a Dataframe and write it as a JSON format file. Open Json file to observe the conversion schema.

def main():
    cnfg = SparkConf().setAppName("CustomerApplication").setMaster("local[2]")
    sc = SparkContext(conf=cnfg)
    spark = SparkSession(sc)
    inputFilePath = "D:\\Workspace\\pthonTest\\pthonTest\\spark\\BEAD_DATA-master\\BEAD_DATA-master\\Movies.csv"
    df = (spark.read.option("header", "true").option("inferSchema", "true").csv(inputFilePath))
    df.show(50, False)
    df.printSchema()
    df.write.json("D:\\DataSets\\write\\json\\movies")

if __name__ == '__main__':
    main()