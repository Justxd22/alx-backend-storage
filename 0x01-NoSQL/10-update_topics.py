#!/usr/bin/env python3
"""Change topic."""


def update_topics(mongo_collection, name, topics):
    """Change topic."""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
