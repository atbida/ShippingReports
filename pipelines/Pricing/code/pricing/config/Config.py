from prophecy.config import ConfigBase
prophecy_spark_context = None


class Config(ConfigBase):

    def __init__(self, Database: str=None, segment: str=None, datestring: str=None):
        self.spark = None
        self.update(Database, segment, datestring)

    def update(self, Database: str="RETAIL", segment: str="BUILDING", datestring: str="1993-11-13"):
        global prophecy_spark_context
        prophecy_spark_context = self.spark
        self.Database = Database
        self.segment = segment
        self.datestring = datestring
        pass
