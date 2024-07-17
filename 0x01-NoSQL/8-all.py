#!/usr/bin/env python3
"""List all."""


def list_all(mongo_collection):
    """List all."""
    return mongo_collection.find()
