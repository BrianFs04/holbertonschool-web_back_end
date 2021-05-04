#!/usr/bin/env python3
""" update_topics module """


def update_topics(mongo_collection, name, topics):
    """Changes all topics of a school document based on the name"""
    query = {"name": name}
    update = {"$set": {"topics": topics}}
    return mongo_collection.update(query, update)
