#!/usr/bin/env python3
""" all module """


def list_all(mongo_collection):
    """Function that lists all documents in a collection"""
    if not mongo_collection.find():
        return []
    return list(mongo_collection.find())
