from pyspark import SparkContext, SparkConf
from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *


#Question Retrieve all movies produced by Walt Disney Studios. You should display the Producer Name, Location, Movie Title and Movie Type.
# (Note: The first two fields are from Producer.JSON and the other two fields are from Movies.CSV.
# The join field is ProcuderCode field. If you have issues, you may change ProducerID column in the CSV to same as in JSON, viz. ProducerCode)


def main():
    cnfg = SparkConf().setAppName("CustomerApplication").setMaster("local[2]")
    sc = SparkContext(conf=cnfg)
    spark = SparkSession(sc)
    inputFilePathProducer = "D:\\Workspace\\pthonTest\\pthonTest\\spark\\BEAD_DATA-master\\BEAD_DATA-master\\Producers.json"
    dfProducer = (spark.read.option("header", "true").option("inferSchema", "true").json(inputFilePathProducer))

    inputFilePathMovies = "D:\\Workspace\\pthonTest\\pthonTest\\spark\\BEAD_DATA-master\\BEAD_DATA-master\\\MoviesV2.csv"
    dfMovies = (spark.read.option("header", "true").option("inferSchema", "true").csv(inputFilePathMovies))

    joinDF = dfProducer.join(dfMovies,"ProducerCode")
    joinDF.select("ProducerName","Location","MovieTitle","MovieType").show(50,False)

if __name__ == '__main__':
    main()