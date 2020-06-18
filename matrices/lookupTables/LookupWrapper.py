class LookupWrapper:

    def __init__(self, lookupDictionary:dict):
        self.lookupDictionary = lookupDictionary

    def get(self, x, y):

        # go with scores in replacement matrix. Symmetric matrix is assumed !
        value = self.lookupDictionary.get((x, y))
        if value is None:
            value = self.lookupDictionary.get((y, x))

        return value