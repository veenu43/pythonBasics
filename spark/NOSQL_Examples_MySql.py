from pyspark import SparkContext, SparkConf
from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *

def main():
    cnfg = SparkConf().setAppName("CustomerApplication").setMaster("local[2]")
    cnfg.set("spark.jars", "C:\\Users\\veenu\\.m2\\repository\\mysql\\mysql-connector-java\\8.0.23\\mysql-connector-java-8.0.23.jar")
    sc = SparkContext(conf=cnfg)
    spark = SparkSession(sc)
    df = (spark.read.format("jdbc")
          .options(url="jdbc:mysql://localhost:3306/videoshop",
                    driver="com.mysql.jdbc.Driver",
                    dbtable="Movies",
                    user="root",
                    password="root").load())
    df.show(50, False)
    df.printSchema()


if __name__ == '__main__':
    main()