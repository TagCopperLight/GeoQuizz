import json
import os


class Association:
    def __init__(self, difficulty, elements):
        self.difficulty = difficulty
        self.elements = elements

    def get_elements(self):
        return self.elements


class Collection:
    def __init__(self, collection):
        self.collection = collection
        self.init = collection['init']
        del collection['init']

        self.associations = []

        for index, association in enumerate(collection['collection']):
            globals()['Association' + str(index)] = Association(association[1], association[0])
            self.associations.append(globals()['Association' + str(index)])

    def get_associations(self):
        return self.associations

    def get_association(self, name):
        for association in self.associations:
            for element in association.elements:
                if element == name:
                    return association
        return None

    def get_name(self):
        return self.init[0]


class Collections:
    def __init__(self):
        self.raw_collections = []
        self.collections = []

        self.import_collections()

        for index, collection in enumerate(self.raw_collections):
            globals()['Collection' + str(index)] = Collection(collection)
            self.collections.append(globals()['Collection' + str(index)])

    def import_collections(self):
        for filename in os.listdir('data/collections'):
            if '.json' in filename:
                with open('data/collections/' + filename, encoding='utf-8') as file:
                    self.raw_collections.append(json.load(file))
                    file.close()

    def get_collections(self):
        return self.collections

    def get_collection(self, name):
        for collection in self.collections:
            return collection if collection.init[0] == name else None