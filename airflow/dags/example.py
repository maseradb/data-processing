from pyspark.sql import SparkSession
from pyspark import SparkConf
import credentials

# Create Spark session
spark = SparkSession \
    .builder \
    .appName("Example App") \
    .getOrCreate()


# show configured parameters
print(SparkConf().getAll())

# set log level
spark.sparkContext.setLogLevel("INFO")



df = spark.read \
    .format("jdbc") \
    .option("url", f'jdbc:oracle:thin:@{credentials.DSN}?TNS_ADMIN={credentials.WALLET_LOCATION}') \
    .option("driver", "oracle.jdbc.driver.OracleDriver") \
    .option("user", credentials.USER) \
    .option("password", credentials.PASSWORD) \
    .option("dbtable", "auxiliary_table") \
    .load()

print("Tables loaded into DataFrames.")

df.show()

df.write \
    .format("jdbc") \
    .option("url", f'jdbc:oracle:thin:@{credentials.DSN}?TNS_ADMIN={credentials.WALLET_LOCATION}') \
    .option("driver", "oracle.jdbc.driver.OracleDriver") \
    .option("user", credentials.USER) \
    .option("password", credentials.PASSWORD) \
    .option("dbtable", "target_table") \
    .mode("append") \
    .save()
