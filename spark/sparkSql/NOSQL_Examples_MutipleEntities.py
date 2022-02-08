from pyspark import SparkContext, SparkConf
from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *

def main():
    cnfg = SparkConf().setAppName("CustomerApplication").setMaster("local[2]")
    sc = SparkContext(conf=cnfg)
    spark = SparkSession(sc)
    customerFilePath = "D:\\Workspace\\pthonTest\\pthonTest\\spark\\BEAD_DATA-master\\BEAD_DATA-master\\Customer.csv"
    countryFilePath = "D:\\Workspace\\pthonTest\\pthonTest\\spark\\BEAD_DATA-master\\BEAD_DATA-master\\Country.csv"
    dfCustomer = ( spark.read
                   .option("header", "true")
                   .option("inferSchema", "true")
                   .csv(customerFilePath) )
    dfCountry = ( spark.read .option("header", "true")
                  .option("inferSchema", "true")
                  .csv(countryFilePath) )
    joinDF = dfCustomer.join(dfCountry, "CountryCode")
    ( joinDF.select("CustomerID", "CustomerName", "CountryCode", "CountryName", "Currency", "TimeZone")
      .show(300, False))

if __name__ == '__main__':
    main()