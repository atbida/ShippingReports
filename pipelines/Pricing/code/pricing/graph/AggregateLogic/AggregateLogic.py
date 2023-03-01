from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from . import *

def AggregateLogic(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df_SumAmounts_1 = SumAmounts_1(spark, in0)

    return df_SumAmounts_1
