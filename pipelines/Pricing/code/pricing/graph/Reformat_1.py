from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from pricing.config.ConfigStore import *
from pricing.udfs.UDFs import *

def Reformat_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        expr("aes_encrypt(CAST(ORDERKEY AS STRING), '1234567890123456')").alias("MaskedOrderKey"), 
        col("ORDERKEY"), 
        col("PARTKEY"), 
        col("SUPPKEY"), 
        col("LINENUMBER"), 
        col("QUANTITY"), 
        col("EXTENDEDPRICE"), 
        col("DISCOUNT"), 
        col("TAX"), 
        col("RETURNFLAG"), 
        col("DELIVERYSTATUS"), 
        col("SHIPDATE"), 
        col("COMMITDATE"), 
        col("RECEIPTDATE"), 
        col("SHIPINSTRUCT"), 
        col("SHIPMODE"), 
        col("COMMENT"), 
        col("_c0"), 
        col("_c1"), 
        col("_c2"), 
        col("_c3"), 
        col("_c4"), 
        col("_c5"), 
        col("_c6"), 
        col("_c7"), 
        col("_c8"), 
        col("_c9")
    )
