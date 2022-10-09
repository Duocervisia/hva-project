from models.baseMapper import baseMapper
from models.descriptionModel import DescriptionModel


import bson

class DescriptionMapper(baseMapper):
    collection = "test"

    def save (self, descriptionModel : DescriptionModel):
        #descriptionBson = bson.BSON.encode(descriptionModel.__dict__)
        x = self.mongo.insert_one(descriptionModel.__dict__)

        print(x)
