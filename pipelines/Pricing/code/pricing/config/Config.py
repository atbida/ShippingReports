from prophecy.config import ConfigBase
prophecy_spark_context = None


class Config(ConfigBase):

    def __init__(self, Database: str=None, segment: str=None, date: str=None):
        self.spark = None
        self.update(Database, segment, date)

    def update(self, Database: str="RETAIL", segment: str="BUILDING", date: str="1995-03-01"):
        global prophecy_spark_context
        prophecy_spark_context = self.spark
        self.Database = Database
        self.segment = segment
        self.date = date
        pass
