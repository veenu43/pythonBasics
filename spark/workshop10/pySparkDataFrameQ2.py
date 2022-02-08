from pyspark.sql.types import StructType, StructField,StringType,IntegerType
from pyspark.sql import SparkSession

# Start the SparkSession
spark = SparkSession.builder.appName('Statistics').getOrCreate()

# Create sparkContext
sc = spark.sparkContext

Data = [("James","Sales","SG",70000,34,10000),
        ("Michael","Sales","SG",66000,56,20000),
        ("Robert","Sales","MY",61000,30,23000),
        ("Maria","Finance","MY",60000,24,23000),
        ("Raman","Finance","USA",79000,40,24000),
        ("Scott","Finance","USA",63000,36,19000),
        ("Jen","Finance","UK",89000,53,15000),
        ("Jeff","Marketing","UK",70000,25,18000),
        ("Alice","Marketing","UK",78000,50,21000),
        ("Ada","IT","SG",83000,35,11000),
        ("Jackson","IT","MY",71000,30,21000),
        ("Cooper","IT","UK",91000,40,21000)]

# Create a RDD from the list
rdd = sc.parallelize(Data)

# a) Create a PySpark DataFrame based on the given RDD.
df = spark.createDataFrame(rdd, ['employee_name', 'department', 'country', 'salary','age','bonus'])

# b) Show data and print schema
df.show()
df.printSchema()

# c) Run groupBy() on “department” columns.
# Calculate aggregates like minimum, maximum, average, total salary for each group using min(), max(), avg() and sum() aggregate functions respectively
departmentDF = df.groupby("department")
departmentDF.max("salary").show()
departmentDF.min("salary").show()
departmentDF.avg("salary").show()
departmentDF.sum("salary").show()


# d) Run groupBy() on “country” columns.
# Calculate aggregates like minimum, maximum, average, total salary for each group using min(), max(), avg() and sum() aggregate functions respectively.
countryDF = df.groupby("country")
countryDF.max("salary").show()
countryDF.min("salary").show()
countryDF.avg("salary").show()
countryDF.sum("salary").show()