from pyspark.sql import SparkSession
# Start the SparkSession

spark = SparkSession.builder.appName("Basics Stats").getOrCreate()
# Read people.json file
df = spark.read.json('inputFile/people.json')
# showing data
df.show()
# print schema
df.printSchema()
df.columns
df.describe()
# Retrieve data
df['age']
df.select('age').show()
# Returns list of Row objects
df.head(2)
# Return multiple columns
df.select(['age','name']).show()

# Adding a new column with a simple copy
df.withColumn('newage',df['age']).show()
df.withColumnRenamed('name','given_name').show()
df.withColumn('doubleage',df['age']*2).show()