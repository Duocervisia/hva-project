from time import time 


class DescriptionModel:
    def __init__(self):
        self._company = ""
        self._description = ""

        self._timestamp = int(time())


    def getCompany(self):
        return self._company

    def setCompany(self, value):
        self._company = value

    def delCompany(self):
        del self._company

    company = property(getCompany, setCompany, delCompany, "")

    def getDescription(self):
        return self._description

    def setDescription(self, value):
        self._description = value

    def delDescription(self):
        del self._description

    description = property(getDescription, setDescription, delDescription, "")

    def getTimestamp(self):
        return self._timestamp

    def setTimestamp(self, value):
        self._timestamp = value

    def delTimestamp(self):
        del self._timestamp

    timestamp = property(getTimestamp, setTimestamp, delTimestamp, 0)