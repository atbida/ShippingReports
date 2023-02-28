from prophecy.config import ConfigBase
prophecy_spark_context = None


class Config(ConfigBase):

    def __init__(self, Database: str=None):
        self.spark = None
        self.update(Database)

    def update(self, Database: str="RETAIL"):
        global prophecy_spark_context
        prophecy_spark_context = self.spark
        self.Database = Database
        pass
