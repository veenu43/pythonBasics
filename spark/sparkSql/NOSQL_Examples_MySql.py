from pyspark import SparkContext, SparkConf
from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *


# Question :Part A
# Data retrieval using Spark SQL
# 1. Retrieve all data from the Movies table.
# 2. Retrieve all Movies and display the data in ascending order of Movie Title.
# 3. Retrieve all R rated movies. You should display only the Video Code, Movie Title, and Movie Type.
# 4. Retrieve all Science Fiction movies produced by Warner.


# Question: Part B
# Aggregation and Statistical Queries
# 5. Determine the average rental price of all movies. Explore the variance, standard deviation and skewness of this population.
# 6. Find the total stock of movies grouped by Movie Type and Rating (two fields).
# Use the RollUp function and build the cube function to determine the dimensional totals for the above grouping.



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

    #1 : Retrieve all data from the Movies table.
    #df.show(50, False)
    #df.printSchema()

    #2: Retrieve all Movies and display the data in ascending order of Movie Title.
    #df.orderBy(asc("MovieTitle")).show(200,False)

    #3: Retrieve all R rated movies. You should display only the Video Code, Movie Title, and Movie Type.
    #df.filter(" Rating = 'R'").select("VideoCode","MovieTitle","MovieType").show(200,False)

    #4: Retrieve all Science Fiction movies produced by Warner.
    #df.filter("MovieType = 'Sci-fi' AND ProducerID = 'Warner'").show(200,False)

    #5: Determine the average rental price of all movies. Explore the variance, standard deviation and skewness of this population.
    '''
    average = df.agg(avg("RentalPrice")).first()[0]
    print("average: ",average)

    stdDev = df.agg(stddev_pop("RentalPrice")).first()[0]
    print("standdardDeviation: ",stdDev)

    skewnessPop = df.agg(skewness("RentalPrice")).first()[0]
    print("Skewness: ",skewnessPop)
    '''
    # 6: Find the total stock of movies grouped by Movie Type and Rating (two fields).
    # Use the RollUp function and build the cube function to determine the dimensional totals for the above grouping
    df.groupby("MovieType","Rating").count().show()
    df.rollup("MovieType","Rating").count().show()
    df.cube("MovieType","Rating").count().show()



if __name__ == '__main__':
    main()