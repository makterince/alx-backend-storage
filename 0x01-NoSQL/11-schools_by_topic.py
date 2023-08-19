#!/usr/bin/env python3
""" This module returns list of school with a specific topic """


def schools_by_topic(mongo_collection, topic):
    """ returns list of school with a specific topic """
    
    if mongo_collection is None:
        return None
    return mongo_collection.find({"topics": topic})
