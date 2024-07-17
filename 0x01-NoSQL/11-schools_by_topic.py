#!/usr/bin/env python3
"""Get school with a topic."""


def schools_by_topic(mongo_collection, topic):
    """Get school with a topic."""
    return mongo_collection.find({"topics": topic})
