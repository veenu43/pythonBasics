from pyspark import SparkContext, SparkConf
from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *

def main():
    # Configure Spark
    conf = SparkConf().setAppName("Create RDD")
    conf = conf.setMaster("local[*]").set("spark.driver.bindAddress","localhost").set("spark.ui.port","4050")
    spark = SparkContext(conf=conf)
    spark.setLogLevel("INFO")

    baseRdd1 = spark.parallelize(["hello", "hi", "suria", "big", "data", "hub", "hub", "hi"])
    print(f"baseRdd1 : '{baseRdd1.collect()}'")

    baseRdd2 = spark.parallelize(["hey", "daniel","mohammad", "prateek"])
    print(f"baseRdd2 : '{baseRdd2.collect()}'")


    baseRdd3 = spark.parallelize([1, 2, 3, 4], 2)
    print(f"baseRdd3 : '{baseRdd3.collect()}'")

    sampledRdd = baseRdd1.sample("false", 0.5)
    print(f"sampledRdd : '{sampledRdd.collect()}'")


    unionRdd = baseRdd1.union(baseRdd2).repartition(1)
    print(f"unionRdd : '{unionRdd.collect()}'")

    intersectionRdd = baseRdd1.intersection(baseRdd2)
    # distinctRdd = baseRdd1.distinct.repartition(1)

    subtractRdd = baseRdd1.subtract(baseRdd2)
    cartesianRdd = sampledRdd.cartesian(baseRdd2)
    reducedValue = baseRdd3.reduce(lambda a, b: a + b)
    collectedRdd = baseRdd1.collect
    print(collectedRdd)
    count = baseRdd1.count
    first = baseRdd1.first
    print("Count is...\l",count);
    print("First Element is...")
    print(first)
    takeValues = baseRdd1.take(3)
    takeSample = baseRdd1.takeSample("false", 2)
    takeOrdered = baseRdd1.takeOrdered(2)
    print("Take Three Values..")
    print(takeValues)
    print("Take Sample Values..")
    print(takeSample)
    input("Press enter to terminate")

if __name__ == '__main__':
    main()