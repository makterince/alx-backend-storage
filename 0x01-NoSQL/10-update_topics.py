#!/usr/bin/env python3
""" module updates the topics of a document """


def update_topics(mongo_collection, name, topics):
    """ changes all topics of a school doc based on name """

    if mongo_collection is None:
        return None
    mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}}
            )
