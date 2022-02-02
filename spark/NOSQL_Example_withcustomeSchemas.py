from pyspark import SparkContext, SparkConf
from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *

def main():
    cnfg = SparkConf().setAppName("CustomerApplication").setMaster("local[2]")
    sc = SparkContext(conf=cnfg)
    spark = SparkSession(sc)
    inputFilePath = "D:\\Workspace\\pthonTest\\pthonTest\\spark\\BEAD_DATA-master\\BEAD_DATA-master\\\CustomerNoHdr.csv"
    custschema = StructType(
        [StructField("Customerid", IntegerType(), True), StructField("CustName", StringType(), True),
         StructField("MemCat", StringType(), True), StructField("Age", IntegerType(), True),
         StructField("Gender", StringType(), True), StructField("AmtSpent", DoubleType(), True),
         StructField("Address", StringType(), True), StructField("City", StringType(), True),
         StructField("CountryID", StringType(), True), StructField("Title", StringType(), True),
         StructField("PhoneNo", StringType(), True)])

    df = (spark.read.schema(custschema).option("header", "true").csv(inputFilePath))

    #Show only CustomerID, CustomerName and Age
    #df.select("Customerid", "CustName", "Age").show(200, False)

    #Scheam with 50 records  and column truncation set to false
    #df.show(50, False)

    #PrintSchema
    #df.printSchema()

    #Retrieving data from the Customers Dataset & displaying sorted on Customer Name
    df.orderBy("CustName").show()

if __name__ == '__main__':
    main()