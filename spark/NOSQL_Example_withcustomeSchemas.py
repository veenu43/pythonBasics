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

    df = (spark.read.schema(custschema).option("header", "false").csv(inputFilePath))

    #Show only CustomerID, CustomerName and Age
    #df.select("Customerid", "CustName", "Age").show(200, False)

    #Scheam with 50 records  and column truncation set to false
    #df.show(50, False)

    #PrintSchema
    #df.printSchema()

    #Retrieving data from the Customers Dataset & displaying sorted on Customer Name
    #df.orderBy("CustName").show()
    # order by desccending
    #df.orderBy(desc("CustName")).show()

    # Filter
    #df.filter("Age > 30").show()
    #df.filter("Gender = 'F'").show()
    #df.filter("Gender = 'F' AND Age > 30").show()
    #df.filter("Gender = 'F' AND Age > 30 AND CustName LIKE 'C%'").show()
    #df.filter("Gender = 'F' AND Age > 30 AND CustName LIKE 'C%'").orderBy(desc("Age")).show()

    #Aggregation
    #print(df.filter("Age > 50").count())
    #print(df.agg(sum("Age")).first()[0])
    #rint(df.filter("Age > 50").agg(sum("Age")).first()[0])

    #Complex
    #df.groupBy("MemCat").sum("AmtSpent").show(200, False)
    #df.filter("Age > 50").groupBy("Gender").sum("AmtSpent").show(200, False)
    #df.groupBy("Gender", "Age").sum("AmtSpent").orderBy ("Gender", "Age").show(200, False)

    #RollUp
    #df.rollup("Gender", "Age").sum("AmtSpent").orderBy("Gender", "Age").show(200, False)

    #Cube
    df.cube("Gender", "Age").sum("AmtSpent").orderBy("Gender", "Age").show(200, False)

if __name__ == '__main__':
    main()