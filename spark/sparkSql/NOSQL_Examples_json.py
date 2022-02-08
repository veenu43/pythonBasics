from pyspark import SparkContext, SparkConf
from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *


# Question Part c
# JSON files
# 7. Read data from the JSON file Producers.JSON and display all records.
# 8. Modify the above query to display those producers who are located in UK.



def main():
    cnfg = SparkConf().setAppName("CustomerApplication").setMaster("local[2]")
    sc = SparkContext(conf=cnfg)
    spark = SparkSession(sc)
    inputFilePath = "D:\\Workspace\\pthonTest\\pthonTest\\spark\\BEAD_DATA-master\\BEAD_DATA-master\\Producers.json"
    df = (spark.read.option("header", "true").option("inferSchema", "true").json(inputFilePath))

    # 7. Read data from the JSON file Producers.JSON and display all records.
    df.show(200, False)
    #df.printSchema()

    # 8. Modify the above query to display those producers who are located in UK.
    df.filter("Location = 'UK'").show()

   # df.write.csv("D:\\Workspace\\pthonTest\\pthonTest\\spark\\BEAD_DATA-master\\log\\json")


if __name__ == '__main__':
    main()