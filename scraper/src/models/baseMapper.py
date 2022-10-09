from pymongo import MongoClient
import socket
class baseMapper(object):
    client = None
    db = None
    mongo = None

    @property
    def collection(self):
        raise NotImplementedError

    def __init__(self) -> None:
        if(self.client == None):
            self.client = MongoClient("mongodb://root:example@host.docker.internal:27017/admin")
            self.mongo = self.client.get_database()[self.collection]
