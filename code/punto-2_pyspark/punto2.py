import findspark
findspark.init("C:\Spark\spark-2.3.3-bin-hadoop2.7") #wherever your Spark directory is
import pyspark # only run after findspark.init()
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
df = spark.sql('''select 'spark' as hello ''')