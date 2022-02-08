'''
This example shows how to persist an RDD. As a known fact, RDDs are lazily evaluated and sometimes it is necessary to reuse the RDD multiple times.
In such cases, Spark will re-compute the RDD and all of its dependencies, each time we call an action on the RDD.
This is expensive for iterative algorithms which need the computed dataset multiple times.
To avoid computing an RDD multiple times, Spark provides a mechanism for persisting the data in an RDD.
After the first time an action computes the RDD's contents, they can be stored in memory or disk across the cluster.
The next time an action depends on the RDD, it need not be recomputed from its dependencies.
'''

from pyspark import *
def isNotHeader(l:str):
    return not (l[0:11] == "CountryCode" and l.find("Currency")>0)
# Configure Spark
conf = SparkConf().setAppName("Create RDD")
conf = conf.setMaster("local[*]")
spark = SparkContext(conf=conf)
spark.setLogLevel("INFO")
# Logs

print("Starting country1")
country1 = spark.textFile("in/Country.csv")
country1.persist(StorageLevel.MEMORY_AND_DISK_2)
#country1.cache()
#julyFirstLogs.cache()
print("Starting country2")
country2 = spark.textFile("in/Country2.csv")
country2.persist(StorageLevel.MEMORY_ONLY)
#country2.cache()
# Union Example

print("Starting aggregatedCountry")
aggregatedCountry = country1.union(country2)
print(f"aggregatedCountry count {aggregatedCountry.count()}")
cleanLogLines = aggregatedCountry.filter(lambda line: isNotHeader(line))
print(f"cleanLogLines count {cleanLogLines.count()}")
cleanLogLines.saveAsTextFile("out/country_logs_all_hosts.csv")
#Statistics Sample

print("Starting sample")
sample = aggregatedCountry.sample(withReplacement = "true", fraction = 0.1)
sample.saveAsTextFile("out/sample_country_logs.csv")
#Intersection

print("Starting intersectionLogLines")
intersectionLogLines = country1.intersection(country2)
cleanedHostIntersection = intersectionLogLines.filter(lambda line: isNotHeader(line))
cleanedHostIntersection.saveAsTextFile("out/country_logs_same_hosts.csv")

country1.unpersist()
country2.unpersist()