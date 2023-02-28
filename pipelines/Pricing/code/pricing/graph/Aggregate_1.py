from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from pricing.config.ConfigStore import *
from pricing.udfs.UDFs import *

def Aggregate_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.groupBy(col("L_ORDERKEY"), col("O_ORDERDATE"), col("`O_SHIP-PRIORITY`").alias("O_SHIP-PRIORITY"))

    return df1.agg(
        col("L_ORDERKEY"), 
        sum((col("L_EXTENDEDPRICE") * (lit(1) - col("L_DISCOUNT")))).alias("REVENUE"), 
        col("`O_SHIP-PRIORITY`").alias("O_SHIP-PRIORITY")
    )
