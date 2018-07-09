
from cog.database import Cog
from cog import config
import json
import unittest


def qfilter(jsn):
    d = json.loads(jsn[1])
    return d["firstname"]

class TestDB(unittest.TestCase):

    def test_db(self):
        data = ('user100','{"firstname":"Hari","lastname":"seldon"}')
        cogdb = Cog(config)
        cogdb.create_namespace("test")
        cogdb.create_table("db_test", "test")
        cogdb.put(data)
        scanner = cogdb.scanner()
        for r in scanner:
            print r


if __name__ == '__main__':
    unittest.main()
