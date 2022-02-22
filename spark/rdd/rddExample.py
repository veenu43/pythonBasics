from pyspark import SparkContext, SparkConf
from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *

def main():
    # Configure Spark
    conf = SparkConf().setAppName("Create RDD")
    conf = conf.setMaster("local[*]")
    spark = SparkContext(conf=conf)
    spark.setLogLevel("ERROR")
    # in Python from a local collection
    myCollection = "Spark RDD is for any text, structured or unstructured - Big Data Processing".split(" ")

    # parallelize will help to convert a dataset or collection to RDD
    words = spark.parallelize(myCollection, 2)
    upeerWords = words.map(lambda x: x.upper()).take(14);
    print(words)
    print(type(words))
    print(words.collect())
    print(myCollection)
    print(upeerWords)

    # in Python from a File or a directory

    # liNE COUNT
    myFileLineCount = spark.textFile("in/dummy.txt").count()
    print(myFileLineCount)

    # WORD COUNT
    #flatMap will result in a single list of data based on the function or lambda expression
    newdd  = spark.textFile("in/dummy.txt").flatMap(
        lambda line: line.split(" "))
    print (newdd.toDebugString)
    print(newdd)
    print(type(newdd))
    myFileWordCount = spark.textFile("in/dummy.txt").flatMap(
        lambda line: line.split(" ")).count()


    print(myFileWordCount)

    # NO OF FILES COUNT
    myFileCount = spark.wholeTextFiles("in/dummy.txt").count()
    print(myFileCount)


if __name__ == '__main__':
    main()