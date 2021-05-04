#!/usr/bin/env python3
""" schools_by_topic module """


def schools_by_topic(mongo_collection, topic):
    """Returns the list of school having a specific topic"""
    return list(mongo_collection.find({"topics": topic}))
