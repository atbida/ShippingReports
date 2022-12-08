from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pricing.config.ConfigStore import *
from pricing.udfs.UDFs import *

def ReportPrices(spark: SparkSession, in0: DataFrame):
    in0.write\
        .format("delta")\
        .option("overwriteSchema", True)\
        .mode("overwrite")\
        .saveAsTable(f"test_delta.report_shipment_prices")
