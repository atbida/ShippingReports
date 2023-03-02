from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from . import *

def Subgraph_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df_ByStatus_1 = ByStatus_1(spark, in0)

    return df_ByStatus_1
