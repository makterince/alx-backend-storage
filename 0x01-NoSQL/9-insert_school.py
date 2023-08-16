#!/usr/bin/env python3
""" module inserts new documeent in kwargs """


def insert_school(mongo_collection, **kwargs):
    """ inserts doc in kwargs """

    if mongo_collection is None:
        return None

    inserted_document = mongo_collection.insert_one(kwargs)

    return inserted_document.inserted_id
