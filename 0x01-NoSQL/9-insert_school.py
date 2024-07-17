#!/usr/bin/env python3
"""Insert into school."""


def insert_school(mongo_collection, **kwargs):
    """Insert into school."""
    d = mongo_collection.insert_one(kwargs)
    return d.inserted_id
