from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from pricing.config.ConfigStore import *
from pricing.udfs.UDFs import *

def Cleanup(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("L_QUANTITY").alias("QUANTITY"), 
        col("L_EXTENDEDPRICE").alias("EXTENDEDPRICE"), 
        col("L_DISCOUNT").alias("DISCOUNT"), 
        expr("if((L_TAX = 0), 0.02D, L_TAX)").cast(DecimalType(12, 2)).alias("TAX"), 
        col("L_RETURNFLAG").alias("RETURNFLAG"), 
        col("L_DELIVERYSTATUS").alias("DELIVERYSTATUS"), 
        when(((col("L_DISCOUNT") > lit(0.06)) | col("L_RETURNFLAG").eqNullSafe(lit(True))), lit("true"))\
          .otherwise(lit("false"))\
          .alias("CLEARANCE")
    )
