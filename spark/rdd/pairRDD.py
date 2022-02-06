from ctypes import Array

from pyspark import *

def main():
    # Configure Spark
    conf = SparkConf().setAppName("Create RDD")
    conf = conf.setMaster("local[*]")
    spark = SparkContext(conf=conf)
    spark.setLogLevel("INFO")
    groupRDD= spark.parallelize([("k",5),("s",3),("s",4),("p",7)]).groupByKey()
    #groupRDD = spark.parallelize(Array(("k", 5), ("s", 3), ("s", 4), ("p", 7))).groupByKey()
    #groupRDD.cache()
    print("collect: ",groupRDD.mapValues(len).collect())
    print("sorted Collect: ",sorted(groupRDD.mapValues(len).collect()))
    #groupRDD.unpersist()

    groupReducedRDD = spark.parallelize([("k", 5), ("s", 3), ("s", 4), ("p", 7)]).reduceByKey(lambda x,y : x+y)
    #print("groupReducedRDD: ", groupReducedRDD.mapValues(len).collect())
    for element in groupReducedRDD.collect():
        print(element)

    sortedRDD = spark.parallelize([("k", 5), ("s", 3), ("s", 4), ("p", 7)]).sortByKey()
    #print("sortedRDD: ", sortedRDD.mapValues().collect())
    for element in sortedRDD.collect():
        print(element)

if __name__ == '__main__':
    main()