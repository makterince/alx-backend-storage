#!/usr/bin/env python3
""" this module lists all document in a collection """


import pymongo


def list_all(mongo_collection):
    """ lists all doc in collection """

    if mongo_collection is None:
        return []

    return db.mongo_collection.find()
